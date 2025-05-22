def welcome():
    # This function prints a welcome message for the Caesar Cipher program.
    print("Welcome to the Caesar Cipher\n"
          "This program encrypts and decrypts text using the Caesar Cipher.")
    
def enter_message():
    # This function prompts the user to choose between encryption and decryption, and then takes the message and shift number as input.
    
    # While loop to handle invalid input for mode (encryption or decryption)
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        mode = mode.lower()
        if mode == 'e':
            text = input("What message would you like to encrypt: ")
            break
        elif mode == 'd':
            text = input("What message would you like to decrypt: ")
            break
        else:
            print("Invalid choice.")
            continue

    # While loop to handle invalid input for the shift number
    while True:
        shift = input("What is the shift number: ")
        if shift.isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid shift. Please enter a valid number.")
    message = text.upper()
    return mode, message, shift

def encrypt(message, shift):
    '''
    This function encrypts the given message using the Caesar Cipher algorithm.
    '''
    encrypted_message = ''
    for char in message.upper():
        if char.isalpha():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    '''
    This function decrypts the given message using the Caesar Cipher algorithm.
    '''
    decrypted_message = ''
    for char in message:
        if char.isalpha():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypted_message += char
    return decrypted_message
