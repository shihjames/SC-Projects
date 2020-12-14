"""
File: caesar.py
Name: James Shih
----------------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Execute the decipher function and print out the deciphered string.
    """
    ans = decipher()
    print(ans)


def decipher():
    """
    This function will first ask for two inputs (A secret number and a ciphered string).
    After getting these inputs, this function will start deciphering and finally shows the
    deciphered string.
    :return: str,  deciphered string
    """
    secret_num = int(input('Secret number: '))
    ciphered_str = input("What's the ciphered string? ").upper()
    deciphered_str = ''
    for ch in ciphered_str:
        if ch.isalpha():
            # Two conditions
            if ALPHABET.find(ch) + secret_num >= 26:
                deciphered_str += ALPHABET[ALPHABET.find(ch) + secret_num - 26]
            else:
                deciphered_str += ALPHABET[ALPHABET.find(ch) + secret_num]
        else:
            deciphered_str += ch
    return deciphered_str


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
