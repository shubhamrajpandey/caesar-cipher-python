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