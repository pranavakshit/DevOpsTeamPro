def encrypt_text(original_text):
    encrypted_text = "".join(chr(ord(char) + 17) for char in original_text)
    return encrypted_text

original_message = input("Enter encrypted text: ")
encrypted_message = encrypt_text(original_message)
print("Encrypted message:", encrypted_message)


#Kushagra
def decrypt_text(encrypted_text):
    decrypted_text = "".join(chr(ord(char) - 17) for char in encrypted_text)
    return decrypted_text 

encrypted_message = input("Enter encrypted text: ")
decrypted_message = decrypt_text(encrypted_message)
print("Decrypted message:", decrypted_message)
