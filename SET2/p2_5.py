import string

NUMBERS = [0,1,2,3,4,5,6,7,8,9]
ALPHABET = []

def get_alphabet():
    alphabet = []
    for cript, letter in enumerate(string.ascii_lowercase):
        alphabet.append([letter, cript])   

        ALPHABET.append(letter)
    
    return alphabet

def process_alphabet(alphabet, shift):

    count = 0
    inverted_count = 25

    for i in range(0, 26):
        if shift < 0:
            if (alphabet[i][1] + shift) < 0:
                alphabet[i][1] = inverted_count
                inverted_count -= 1

                if inverted_count < 0:
                    count = 25
            else: 
                alphabet[i][1] = alphabet[i][1] + shift

        else:
            if (alphabet[i][1] + shift) > 25:
                alphabet[i][1] = (alphabet[i][1] + shift) % 10

            else:
                alphabet[i][1] = alphabet[i][1] + shift
    return alphabet

def caesar_cipher(message, shift):

    alphabet = get_alphabet()
    message = message.lower()
    ciphered_alphabet = process_alphabet(alphabet, shift)
    ciphered_message = ""

    for letter in message:
        if letter not in ALPHABET and not letter.isdigit():
            ciphered_message = ciphered_message + letter
        
        elif letter.isdigit():
            letter = str((int(letter) + shift) % 10)
            ciphered_message = ciphered_message + letter

        else:
            code = dict(zip(string.ascii_lowercase, list(range(26))))[letter]
            n = (code + shift) % 25
            letter = dict(zip(list(range(26)), string.ascii_lowercase))[n]
            ciphered_message = ciphered_message + letter
    print(ciphered_message)

caesar_cipher("hot dogs are 5.00 here?!?",2)

