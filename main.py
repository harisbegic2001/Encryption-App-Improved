def encryption(message, shift):
    varijabla = ""
    for i in range(len(message)):
            mala = ord(message[i])
            mala += shift
            varijabla += chr(mala)
    print(f"Your encrypted message is: {varijabla}")

def decryption(message, shift):
    varijabla = ""
    for i in range(len(message)):
            mala = ord(message[i])
            mala -= shift
            varijabla += chr(mala)
    print(f"Your decrypted message is: {varijabla}")



while True:
    enc_dec = input("Type \"encode\" if you want to encrypt, type \"decode\" if you want to decrypt the message: ").lower()


    if enc_dec == "encode":
        message_enc = input("Type the message: ")
        shift_enc = int(input("Type in the shifter number: "))
        encryption(message_enc, shift_enc)
        choose = input("If you want to continue to use our app type \"yes\" if don't, type \"no\": ").lower()
        if choose == "yes":
            continue
        elif choose == "no":
            break
    
    elif enc_dec == "decode":
        message_dec = input("Type the message: ")
        shift_dec = int(input("Type in the shifter number: "))
        decryption(message_dec, shift_dec)
        choose = input("If you want to continue to use our app type \"yes\" if don't, type \"no\": ").lower()
        if choose == "yes":
            continue
        elif choose == "no":
            break
print("Thank you for using our app")