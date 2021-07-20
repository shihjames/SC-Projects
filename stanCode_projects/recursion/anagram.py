"""
File: anagram.py
Name: James Shih
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time


# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
word_dict = {}                 # A list contains all the words in a dictionary.


def main():
    """
    The program will find all the anagrams of a word.
    """

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        search = input('Find anagrams for: ')
        start = time.time()
        # If the user enter -1, the program will stop.
        if search == EXIT:
            break
        read_dictionary(search)
        find_anagrams(search)
        end = time.time()
        print('Run time: ', end - start)


def read_dictionary(search):
    """
    This function will read files, and add all the words into a list.
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if word[0] in search and len(word) == len(search):
                if check_others(word, search):
                    if word[0] in word_dict:
                        word_dict[word[0]].append(word)
                    else:
                        word_dict[word[0]] = [word]


def check_others(word, search):
    for ch in word:
        if ch not in search:
            return False
    return True


def find_anagrams(s):
    print('Searching...')
    word = helper(s, '', '', [])
    for i in range(len(word)):
        print('Found: ', word[i])
        if i != len(word)-1:
            print('Searching...')
    print(len(helper(s, '', '', [])), 'anagrams:', helper(s, '', '', []))


def helper(s, ind, current_s, current_l):
    if len(current_s) == len(s):
        if has_prefix(current_s):
            if current_s not in current_l:
                current_l.append(current_s)
    else:
        for i in range(len(s)):
            # Choose
            if str(i) not in ind:
                ind += str(i)
                current_s += s[int(ind[-1])]
                # Explore
                if len(current_s) >= 2:
                    if has_prefix(current_s):
                        helper(s, ind, current_s, current_l)
                else:
                    helper(s, ind, current_s, current_l)
                # Un-choose
                ind = ind[:-1]
                current_s = current_s[:-1]
    return current_l


def has_prefix(sub_s):
    """
    This function will check whether a string is in dict_lst
    :param sub_s: str, a sting that you want to check.
    :return: boolean. Return 'True' if sub_s is in dict_lst. Return 'False' if sub_s is not in dict_lst.
    """
    for word in word_dict[sub_s[0]]:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
