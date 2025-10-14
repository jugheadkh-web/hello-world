import string

# All printable characters (letters, digits, punctuation, whitespace, etc.)
characters = string.printable
num_chars = len(characters)

# Get input from the user
cipher_text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value (shift amount): "))

# Perform decryption
plain_text = ''
for ch in cipher_text:
    if ch in characters:
        old_index = characters.index(ch)
        new_index = (old_index - distance) % num_chars
        plain_text += characters[new_index]
    else:
        plain_text += ch

# Output the decrypted text
print("\nDecrypted text:")
print(plain_text)
