def cracking_cipher(ciphertext):
    print("")
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ciphertext.upper()
    
    for key in range(1, 26):
        decrypted = ''
        for alphabet in ciphertext:
            if alphabet in alphabets:
                index = alphabets.index(alphabet)
                new_index = (index - key) % 26
                decrypted += alphabets[new_index]
            else:
                decrypted += alphabet
        print(f'Key {key}: {decrypted}')
                    
    

cipher_text = input("Enter Cipher Text: ")
cracking_cipher(cipher_text)