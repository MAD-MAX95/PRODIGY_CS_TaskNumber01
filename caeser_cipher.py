import random
import string

char=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(char)
key=chars.copy()

random.seed(42) #random.seed is used to ensure the key is shuffled same way every time u run the script
random.shuffle(key)

#ENCRYPT
def encrypt(plain_text):
  cipher_text=""
#Conversation of original message to encrypt message
  for letters in plain_text:
    if letters in chars:
      index=chars.index(letters)
      cipher_text += key[index]
    else:
     cipher_text += letters #if character is not in letter leavr it as it is 
  return cipher_text


#DECRYPT
def decrypt(cipher_text):
  plain_text=""
  for letters in cipher_text:
      if letters in chars:
        index=key.index(letters)
        plain_text += chars[index]
      else:
        plain_text += letters
  return plain_text



print()
print('****CAESER CIPHER METHOD****')
print()


print('Do you want to Encrypt or Decrypt?')
user_input=input('e/d :').lower()

if  user_input == 'e':
   print('ENCRYPTION MODE IS SELECTED')
   text=input('ENTER MESSAGE TO ENCRYPT :')
   cipher_text=encrypt(text)
   print(f'CIPHER TEXT :{cipher_text}')


elif user_input == 'd':
   print('DECRYPTION MODE IS SELECTED')
   text=input('ENTER MESSAGE TO DECRYPT :')
   Plain_text=decrypt(text)
   print(f'PLAIN TEXT :{Plain_text}')

else:
  print("Invalid input ! Please enter  'e' for encrypt or 'd' for decrypt")  
