"""
    1. The login function asks the user for the username and password.
    2. The login function accepts an username and password argument.
    3. It verifies if the username and password are valid and allows the user to access the program.
    4. Else it loops back and asks the user to re-enter the username and password.
    note: more info in the diagrams at the docs
"""
def login(database, username, password):
    if username not in database:
        print("Invalid Username\n")
        return False
    else:
        if password == cryptography(database[username], "decrypt"):
            return True
        else:
            print("Invalid Password\n")
            return False

"""
    1. The cryptography function is used for encrypting and decrypting text.
    2. The textInput is a parameter that is for accepting plaintext or ciphertext.
    3. The mode parameter determines whether to encrypt the text or decrypt it.
"""
def cryptography(textInput, mode="encrypt"):
    key = "Prologi"
    textOutput = ""
    i = 0

    if (mode != "encrypt") and (mode != "decrypt"):
        print("Error: invalid mode")
        return None

    for character in textInput:
        characterValue = ord(character)
        if character.isalpha():
            if i > (len(key) - 1):
                i = 0

            k = key[i]
            cipherValue = 0
            keyValue = ord(k)

            if (mode == "encrypt"):
                if character.isupper():
                    if k.isupper():
                        cipherValue = ((characterValue - ord('A')) + (keyValue - ord('A'))) % 26 + ord('A')
                    elif k.islower():
                        cipherValue = ((characterValue - ord('A')) + (keyValue - ord('a'))) % 26 + ord('a')

                elif character.islower():
                    if k.isupper():
                        cipherValue = ((characterValue - ord('a')) + (keyValue - ord('A'))) % 26 + ord('A')
                    elif k.islower():
                        cipherValue = ((characterValue - ord('a')) + (keyValue - ord('a'))) % 26 + ord('a')
            else:
                if character.isupper():
                    if k.isupper():
                        cipherValue = ((characterValue - ord('A')) - (keyValue - ord('A'))) % 26 + ord('A')
                    elif k.islower():
                        cipherValue = ((characterValue - ord('A')) - (keyValue - ord('a'))) % 26 + ord('a')

                elif character.islower():
                    if k.isupper():
                        cipherValue = ((characterValue - ord('a')) - (keyValue - ord('A'))) % 26 + ord('A')
                    elif k.islower():
                        cipherValue = ((characterValue - ord('a')) - (keyValue - ord('a'))) % 26 + ord('a')

            characterLetter = chr(cipherValue)
            textOutput += characterLetter

            i += 1

        else:
            textOutput += character

    return textOutput
