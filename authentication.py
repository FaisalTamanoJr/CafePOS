def login():
    pass


def encrypt(plaintext):

    # Basic encryption algorithm (will change/modify in the future)
    ciphertext = ""
    for character in plaintext.upper():
        if character.isalpha() == True:
            cipherascii = ord(character)
            shift = ((1 + (cipherascii - ord('A')))) % 26 + ord('A')
            ciphertext += chr(shift)

    return ciphertext


def decrypt():
    pass
