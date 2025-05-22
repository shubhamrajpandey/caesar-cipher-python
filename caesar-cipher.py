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
def process_file(filename, mode, shift):
    '''
    This function reads messages from a file, performs encryption or decryption,and returns the list of processed messages.
    '''
    #empty list to store message
    messages = []

    # Reading each line from the file
    with open(filename, 'r') as file:#the file open with in a read mode
        for line in file:
            message = line.strip().upper()
            #to remove the whitespace characters from the letter variable read
            if mode == 'e':
                messages.append(encrypt(message, shift))
                 #Encrypt the message and appends in  the message list previously made.
                print(messages)
            elif mode == 'd':
                messages.append(decrypt(message, shift))
                #Decrypt the message and appends in  the message list previously made.
                print(messages)
            else:
                print("Invalid mode: {}".format(mode))
                return None

    return messages

def is_file(filename):
    # This function checks if a file with the given filename exists.
    try:
        with open(filename, 'r'):
            return True
    except FileNotFoundError:
        return False
    
#Each message is written to a new line in the file.
def write_messages(messages):
    # This function writes messages to the 'results.txt' file.
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    # This function prompts the user to choose between encrypting/decrypting a message
    # from the console or a file.

    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        mode=mode.lower()
        if mode in ['e', 'd']:
            break
        print("Invalid mode. Please enter 'e' for encryption or 'd' for decryption.")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        print("Invalid source. Please enter 'f' for file or 'c' for console.")

    if source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            print("Invalid filename. Please enter a valid filename.")
        message = None
    else:
        filename = None
        message = input("What message would you like to {}: ".format('encrypt' if mode == 'e' else 'decrypt'))
        message = message.upper()

    while True:
        try:
            shift = int(input("What is the shift number: "))
            break
        except ValueError:
            print("Invalid shift. Please enter a valid number.")

    return mode, message, filename, shift