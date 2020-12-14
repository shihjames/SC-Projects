"""
File: anagram.py
Name: James Shih
----------------------------------------
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

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
dict_lst = []                 # A list contains all the words in a dictionary.


def main():
    """
    The program will find all the anagrams of a word.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        search = input('Find anagrams for: ')
        # If the user enter -1, the program will stop.
        if search == EXIT:
            break
        print('Searching...')
        find_anagrams(search)


def read_dictionary():
    """
    This function will read files, and add all the words into a list.
    """
    global dict_lst
    with open(FILE, 'r') as f:
        for line in f:
            # Adding words without any whitespaces.
            dict_lst.append(line.strip())


def find_anagrams(s):
    """
    This function will execute the function read_dictionary and than execute
    a helper function. Finally, the helper function will return a list, and it
    will check if any word in the list is in the dict_lst.
    :param s: str, the word you want to search.
    """
    global dict_lst
    anagram_lst = []
    read_dictionary()
    current = find_anagrams_helper(s, '', '', [], '')
    for ele in current:
        if ele in dict_lst:
            print('Found: ', ele)
            print('Searching...')
            anagram_lst.append(ele)
    print(len(anagram_lst), 'anagrams: ', anagram_lst)


def find_anagrams_helper(s, index_str, anagram, current, current_s):
    """
    This function will recursively find all words that contain same character but in different order.
    :param s: str, input string.
    :param index_str: str, saving indexes.
    :param anagram: str, final string which has same length as s.
    :param current: list, list of anagrams.
    :param current_s: str, current string.
    :return current: list, contains all words with different order.
    """
    if len(index_str) == len(s):
        for i in range(len(index_str)):
            anagram += s[int(index_str[i])]
            # Add anagrams into the list 'current'.
        if anagram not in current:
            current.append(anagram)
    else:
        for index in range(len(s)):
            if str(index) not in index_str:
                # Choose.
                index_str += str(index)
                current_s += s[int(index_str[-1])]
                # Explore.
                if has_prefix(current_s):
                    find_anagrams_helper(s, index_str, anagram, current, current_s)
                # Un-choose.
                index_str = index_str[:-1]
                current_s = current_s[:-1]
    return current


def has_prefix(sub_s):
    """
    This function will check whether a string is in dict_lst
    :param sub_s: str, a sting that you want to check.
    :return: boolean. Return 'True' if sub_s is in dict_lst. Return 'False' if sub_s is not in dict_lst.
    """
    global dict_lst
    for ele in dict_lst:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
