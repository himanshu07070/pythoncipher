#caesar cipher hacker
message= 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#loop through every possible key
for key in range(len(LETTERS)):
#it is important to set translated to the blank string so that the 
#previous iteration's value for trranslated is clear.
    translated=' '
#the rest of the program is the same as the original Caesar program:
#run the encryption /decryption code on each symbol in the message
    for symbol in message:  
        if symbol in LETTERS:
           num=LETTERS.find(symbol)
           num =num-key
#handle the wrap-around if num is 26 or larger or less than 0
           if num<0:
                num=num+ len(LETTERS)
           translated= translated + LETTERS[num]
        else:
            #just add the symbol encrypting/ decrypting
            translated= translated+ symbol
#display the current key being tested , along with its decryption
    print('key #%s: %s' %(key,translated))
          
            
          
          #key =13