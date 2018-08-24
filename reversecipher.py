#encryption

message='Three can keep a secret, if two of them are dead.'
translated=' '
i=len(message)-1
while i>=0:
    translated = translated + message[i]
    i=i-1
print(translated)


#decryption
mess='.daed era meht fo owt fi ,terces a peek nac eerhT'
translate=' '
i=len(mess)-1
while i>=0:
    translate+=mess[i]
    i-=1
print(translate)


#encryption
mes=input("enter any message")
trans=' '
i=len(mes)-1
while i>=0:
    trans = trans + mes[i]
    i=i-1
print(trans)

