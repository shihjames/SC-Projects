"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The program will first ask for a input DNA sequence, then it will build
    the complement strand of the input DNA sequence. Finally, the program will
    print out the complement strand.
    """
    dna = input('Please enter a DNA sequence: ').upper()
    new_dna = build_complement(dna)
    print('The complement of ' + str(dna) + str(' is ') + str(new_dna))


def build_complement(dna):
    """
    This function can build a complement strand of a certain DNA sequence.
    :param dna: str, a DNA sequence you want to manipulate.
    :return: str, a complement sequence of the parameter.
    """
    ans = ''
    for nb in dna:
        if nb == 'A':
            ans += 'T'
        elif nb == 'T':
            ans += 'A'
        elif nb == 'C':
            ans += 'G'
        elif nb == 'G':
            ans += 'C'
    return ans


if __name__ == '__main__':
    main()
