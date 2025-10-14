import string

# All printable characters (letters, digits, punctuation, whitespace, etc.)
characters = string.printable  # 100+ characters
num_chars = len(characters)

# Get input from the user
plain_text = input("Enter a line of text to encrypt: ")
distance = int(input("Enter the distance value (shift amount): "))

# Perform encryption
cipher_text = ''
for ch in plain_text:
    if ch in characters:
        old_index = characters.index(ch)
        new_index = (old_index + distance) % num_chars
        cipher_text += characters[new_index]
    else:
        # Just in case a non-printable character sneaks in
        cipher_text += ch

# Output the encrypted text
print("\nEncrypted text:")
print(cipher_text)
