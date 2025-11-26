def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using Caesar Cipher algorithm.
    
    Args:
        text: The message to encrypt/decrypt
        shift: The shift value (0-25)
        mode: 'encrypt' or 'decrypt'
    
    Returns:
        The encrypted or decrypted text
    """
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def main():
    """Main function to run the Caesar Cipher program."""
    print("=" * 50)
    print("  --- CAESAR CIPHER ENCRYPTION/DECRYPTION ---")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '3':
            print("\nThank you for using Caesar Cipher! Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("\nInvalid choice! Please enter 1, 2, or 3.")
            continue
        
        mode = 'encrypt' if choice == '1' else 'decrypt'
        
        # Get user input
        message = input(f"\nEnter the message to {mode}: ").strip()
        
        if not message:
            print("\nError: Message cannot be empty!")
            continue
        
        # Get shift value
        while True:
            try:
                shift = int(input("Enter the shift value (0-25): ").strip())
                if 0 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 0 and 25!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Perform encryption/decryption
        result = caesar_cipher(message, shift, mode)
        
        # Display results
        print("\n" + "-" * 50)
        print(f"Original message: {message}")
        print(f"Shift value: {shift}")
        print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} message: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()