def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text):
    texts = []
    for x in range(26):
        texts.append(caesar_cipher_encrypt(text, x))
    return texts
