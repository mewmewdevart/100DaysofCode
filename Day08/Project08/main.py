alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if (char.isalpha()): # if the caracter is alphabet
            index = (alphabet.index(char) + shift) % 26 # 26 letters of alphabet
            cipher_char = alphabet[index]
            cipher_text += cipher_char
        else:
            cipher_text += char
    print(f"The encrypted text is : {cipher_text}")

encrypt(text, shift)


