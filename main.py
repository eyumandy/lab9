from encode import *

def main():
  while True:
    menu()
    choice = input('Please enter an option: ')
    if choice == '1':
      password = input('Please enter your password to encode: ')
      enc_pass = encode(password)
      print('Your password has been encoded and stored!')
    if choice =='2':
      dec_pass = decode(enc_pass)
      print(f'The encoded password is {enc_pass}, and the original password is {dec_pass}.')
    if choice == '3':
      break
def menu():
  print('Menu')
  print('-------------')
  print('1. Encode')
  print('2. Decode')
  print('3. Quit')

if __name__ == '__main__': main()