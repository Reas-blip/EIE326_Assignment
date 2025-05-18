def caesar_cipher(text, key, decrypt=False):
    # Use complement for decryption
    if decrypt:
        key = (26 - key) % 26
    
    result = ""
    for char in text:
        if char.isalpha():
            # Determine base for case (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Encrypt or decrypt
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            # Non-alphabet characters are added as-is
            result += char
    return result

# Example usage
message = "Hello, World!"
key = 3
encrypted = caesar_cipher(message, key)
decrypted = caesar_cipher(encrypted, key, decrypt=True)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
