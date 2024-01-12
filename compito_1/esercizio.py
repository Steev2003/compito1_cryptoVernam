alph = 'abcdefghijklmnopqrstuvwxyz '
# custom error
class SubCipherError(Exception):
    '''Error executin Substitution Cipher script'''

'''
word:    babele
chiave:  chiave
cifrato: dhjegi

'''
#funcrion to substitute 
def substitute(in_str):
    # check word length
    word_len = len(in_str)
    in_key = read_file('key.txt')
    key = in_key[:word_len]
    return key
          


# function to read a file 
def read_file(name):
      try:
            with open(name, 'r') as in_file:
                  read_str = in_file.read()
      except IOError as e:
            err_str = ' cannot read file " ' + name 
            err_str = '": '+  str(e)
            raise SubCipherError(err_str)
      return read_str.strip('\n')

def write_file(name,in_write):
      try:
            with open(name, 'w') as in_file:
                 in_file.write(in_write)
      except IOError as e:
            err_str = ' cannot write file " ' + name 
            err_str = '": '+  str(e)
            raise SubCipherError(err_str)
      

def encrypt():
    out_str = ''
    in_str = input("Type a word to encrypt: ")
    key = substitute(in_str)

    for i in range(len(in_str)):
        char0 = in_str[i]
        char1 = key[i % len(key)]  # Usa l'operatore modulo per ottenere una chiave ciclica
        if char0 in alph:
            char0_position = alph.index(char0)
            char1_position = alph.index(char1)
            sum_pos = char0_position + char1_position
            out_str += alph[sum_pos]

    print(out_str)
    write_file('ciphertext.txt',in_str + ' => ' + out_str)


# dechipher process
def decrypt():
      out_str = ''
      in_str = input("Type a word to decrypt: ")
      key = substitute(in_str)

      for i in range(len(in_str)):
            char0 = in_str[i]
            char1 = key[i % len(key)]  # Usa l'operatore modulo per ottenere una chiave ciclica
            if char0 in alph:
                  char0_position = alph.index(char0)
                  char1_position = alph.index(char1)
                  sum_pos = char0_position - char1_position
                  out_str += alph[sum_pos]

      print(out_str)
      write_file('ciphertext.txt',in_str + ' => ' + out_str)


# main

prompt = '''
What do you want to do?
1 -> encrypt 
2 -> decript
0 -> quit
=>  '''     
while True:
      choice =  input(prompt)
      try: 
            if choice == '1':
                  encrypt()
            elif choice == '2':
                  decrypt()
            elif choice == '0':
                  exit()
            else:
                  print('invalid choice, try again')
      
      except SubCipherError as e:
            print(e)
