from word_alphabet import alphabet


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(string_text, numbers_shift):
    cipher_text = ""
    for letter in string_text:
        position = alphabet.index(letter)
        new_position = position + numbers_shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encode text is {cipher_text}")


encrypt(text, shift)
