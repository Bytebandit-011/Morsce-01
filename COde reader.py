MORSE_CODE_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def encode_to_morse(message):
    encoded_message = ''
    for char in message.upper():
        if char in MORSE_CODE_MAP:
            encoded_message += MORSE_CODE_MAP[char] + ' '
    return encoded_message

def decode_from_morse(morse_code):
    decoded_message = ""
    morse_code_words = morse_code.split("  ")

    for word in morse_code_words:
        word_chars = word.split(" ")
        for char in word_chars:
            for key, value in MORSE_CODE_MAP.items():
                if value == char:
                    decoded_message += key
        decoded_message += " "

    return decoded_message.strip()

def main():
    while True:
        choice = input("Choose an option:\n1. Encode to Morse code\n2. Decode from Morse code\n3. Quit\n")

        if choice == '1':
            message = input("Enter a message to encode: ")
            encoded_message = encode_to_morse(message)
            print(encoded_message)
        elif choice == '2':
            morse_code = input("Enter Morse code to decode: ")
            decoded_message = decode_from_morse(morse_code)
            print(decoded_message)
        elif choice == '3':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
