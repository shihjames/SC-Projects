"""
File: boggle.py
Name: James Shih
----------------------------------------
Boggle is a letter game with a square board of 16 random letters.
The goal of the game is to find words that can be formed from adjacent letters on the board.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dict_lst = []  # A list contains all words in FILE.
words = []     # A list of words that are found in boggle.
score = 0	   # The total points did the player gets.


def main():
	"""
	This program is a game called boggle. The user will need to input four rows of letter first,
	and then the user will need to find words that actually exist in the dictionary. After input
	all the answers, the program will show the correct answers and show how many right answers
	and points did the player get.
	"""
	global words, score
	ans = []
	# Input 4 rows to construct a 2D list.
	four_by_four = input_rows()
	# Input player's answers.
	while True:
		answer = input('Your answer (any number to quit): ').lower()
		# Complete answering by input a digit.
		if answer.isdigit():
			break
		ans.append(answer)
	print('Your answer: ', ans)
	# If the 2D list is None, means that the format is wrong.
	if four_by_four is not None:
		words = boggle(four_by_four)
		print('There are', str(len(words)), 'word(s) in total.')
	# Show correct answers and total scores.
	for ele in ans:
		if ele in words:
			score += len(ele)
			print('You found', ele, '!!!')
	print('Your Score: ', score)


def input_rows():
	"""
	This function is used to deal with the input of four rows.
	:return: 2D list, if the format is correct. None, if illegal format.
	"""
	# Create a 2D list.
	four_by_four = [[], [], [], []]
	# Input 4 rows.
	for i in range(1, 5):
		row = input(str(i) + ' row of letters: ')
		# Check if any illegal format exists.
		if input_error(row):
			for ch in row:
				if ch.isalpha():
					ch.lower()
					four_by_four[i-1].append(ch)
		# If input error return False, this function will return None.
		else:
			print('Illegal input')
			return None
	# Successfully creating a 2D list.
	return four_by_four


def input_error(row):
	"""
	This function is used to check if any illegal format exists.
	:param row: str, containing 4 letters with spaces between.
	:return: True, if format correct. False, if illegal format.
	"""
	# Check the length.
	if len(row) != 7:
		return False
	# Check whether the letters and spaces are in right order.
	for i in range(7):
		if i % 2 != 0:
			if row[i] != ' ':
				return False
		if i % 2 == 0:
			if not row[i].isalpha():
				return False
	return True


def boggle(lst):
	"""
	This function will find all the possible words, which exist in both the dictionary and the boggle interface.
	:param lst: 2D list, containing 4 rows of string.
	:return: words, list of all words found in both the dictionary and the boggle interface.
	"""
	global words
	# Read the FILE.
	read_dictionary()
	# Scan through all the letter in the boggle interface.
	for x in range(4):
		for y in range(4):
			# List of coordinates of a letter. (0, 0) to (3, 3)
			coordinate = []
			current_s = ''
			coordinate.append((x, y))
			current_s += lst[x][y]
			words = boggle_helper(x, y, lst, coordinate, current_s)
	return words


def boggle_helper(x, y, lst, coordinate, current_s):
	"""
	This is a helper function of the function helper, and it will recursively find all the possible words
	in the boggle interface and check if the words are in the dictionary as well.
	:param x: int, the x-coordinate of the letter in the boggle interface.
	:param y: int, the x-coordinate of the letter in the boggle interface.
	:param lst: 2D list, containing 4 rows of string.
	:param coordinate: tuple, containing x and y coordinate of a certain letter in the boggle interface.
	:param current_s: str, the current letter selected in the boggle surface
	:return: words, list of all words found in both the dictionary and the boggle interface.
	"""
	global words
	prefix = []
	# Base case occurs when the length is bigger than 4.
	if len(current_s) >= 4:
		if current_s in dict_lst:
			if current_s not in words:
				print('Found: ', current_s)
				words.append(current_s)
				for ele in dict_lst:
					if ele.startswith(current_s):
						if len(ele) > len(current_s):
							prefix.append(ele)
				# If there are other words started with 'current_s', it will continue to extend the word.
				if len(prefix) >= 1:
					longer_words(x, y, lst, coordinate, current_s, prefix)
	# Recursive case.
	else:
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 0 <= i < 4 and 0 <= j < 4:
					if (i, j) not in coordinate:
						# Choose.
						coordinate.append((i, j))
						current_s += lst[i][j]
						# Explore.
						if has_prefix(current_s):
							boggle_helper(i, j, lst, coordinate, current_s)
						# Un-choose.
						coordinate.pop()
						current_s = current_s[:-1]
	return words


def longer_words(x, y, lst, coordinate, current_s, prefix):
	"""
	This is the function used to deal with words that its length is longer than 4.
	:param x: int, the x-coordinate of the letter in the boggle interface.
	:param y: int, the x-coordinate of the letter in the boggle interface.
	:param lst: 2D list, containing 4 rows of string.
	:param coordinate: tuple, containing x and y coordinate of a certain letter in the boggle interface.
	:param current_s: str, the current letter selected in the boggle surface
	:param prefix: list, a list contains longer words started with current_s, other than current_s.
	"""
	if len(current_s) > 4:
		if current_s in prefix:
			if current_s not in words:
				print('Found: ', current_s)
				words.append(current_s)
	else:
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 0 <= i < 4 and 0 <= j < 4:
					if (i, j) not in coordinate:
						coordinate.append((i, j))
						current_s += lst[i][j]
						longer_words(i, j, lst, coordinate, current_s, prefix)
						coordinate.pop()
						current_s = current_s[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict_lst
	with open(FILE, 'r') as f:
		for line in f:
			info = line.strip()
			dict_lst.append(info)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global dict_lst
	for ele in dict_lst:
		if ele.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
