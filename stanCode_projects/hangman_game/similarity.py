"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The program will first ask for two inputs (A long DNA sequence and a short DNA
    sequence you want to match), then the program will find out which part of the long
    DNA sequence is the best match of the short DNA sequence.
    """
    long_sequence = input('Please give me a DNA sequence to search: ').upper()
    short_sequence = input('What DNA sequence would you like to match? ').upper()
    # Variable match shows how many base in the long sequence matches the short sequence.
    match = 0
    # Variable maximum shows the maximum of matches between each loop.
    maximum = 0
    # Variable homology shows the index of the first base of certain part of the long sequence.
    homology = 0
    find_similarity(long_sequence, short_sequence, match, maximum, homology)


def find_similarity(long_sequence, short_sequence, match, maximum, homology):
    """
    This function can find which part of the long DNA sequence best matches the short DNA sequence and it finally shows
    the similarity and the best-matching strand.
    """
    for i in range(len(long_sequence)-len(short_sequence)+1):
        for j in range(len(short_sequence)):
            if long_sequence[i+j] == short_sequence[j]:
                match += 1
        # If the number of match is bigger than maximum, assign maximum to match and assign homology to i.
        if match > maximum:
            maximum = match
            homology = i
        match = 0
    print('The best match is ' + str(long_sequence[homology:homology+len(short_sequence)]))
    print('The similarity is: ' + str(100 * (maximum / len(short_sequence))) + '%')


if __name__ == '__main__':
    main()
