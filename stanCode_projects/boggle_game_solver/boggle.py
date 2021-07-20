"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	board = {}
	for i in range(4):
		row = input(str(i+1) + " row of letters: ")
		if check(row):
			board[i] = row.split(' ')
	start = time.time()
	all_char = get_all_char(board)
	w_dict = read_dictionary(all_char)
	cur_l = boggle(w_dict, board)
	print('There are', str(len(cur_l)), 'word(s) in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(w_dict, board):
	cur_l = []
	for x in range(4):
		for y in range(4):
			# List of coordinates of a letter. (0, 0) to (3, 3)
			coordinate = []
			cur_s = ''
			coordinate.append((x, y))
			cur_s += board[x][y]
			cur_l = boggle_helper(w_dict, board, x, y, coordinate, cur_s, cur_l)
	return cur_l


def boggle_helper(w_dict, board, x, y, coordinate, cur_s, cur_l):
	if len(cur_s) == 4:
		if cur_s not in cur_l:
			for key in w_dict:
				if cur_s in w_dict[key]:
					cur_l.append(cur_s)
					print('Found: ', cur_s)
					for word in w_dict[cur_s[0]]:
						if len(word) > len(cur_s):
							if word.startswith(cur_s):
								longer(w_dict, board, x, y, coordinate, cur_s, cur_l)
	else:
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 0 <= i < 4 and 0 <= j < 4:
					if (i, j) not in coordinate:
						# Choose.
						coordinate.append((i, j))
						cur_s += board[i][j]
						# Explore.
						if len(cur_s) > 1:
							if has_prefix(cur_s, w_dict):
								boggle_helper(w_dict, board, i, j, coordinate, cur_s, cur_l)
						# Un-choose.
						coordinate.pop()
						cur_s = cur_s[:-1]
	return cur_l


def longer(w_dict, board, x, y, coordinate, cur_s, cur_l):
	if len(cur_s) > 4:
		if cur_s not in cur_l:
			for key in w_dict:
				if cur_s in w_dict[key]:
					cur_l.append(cur_s)
					print('Found: ', cur_s)
	else:
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 0 <= i < 4 and 0 <= j < 4:
					if (i, j) not in coordinate:
						# Choose.
						coordinate.append((i, j))
						cur_s += board[i][j]
						# Explore.
						if len(cur_s) > 1:
							if has_prefix(cur_s, w_dict):
								longer(w_dict, board, i, j, coordinate, cur_s, cur_l)
						# Un-choose.
						coordinate.pop()
						cur_s = cur_s[:-1]
	return cur_l


def check(row):
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


def get_all_char(board):
	all_char = []
	for key in board:
		all_char += board[key]
	return all_char


def read_dictionary(all_char):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d = {}
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				if check_others(word, all_char):
					if word[0] in d:
						d[word[0]].append(word)
					else:
						d[word[0]] = [word]
	return d


def check_others(word, all_char):
	for char in word:
		if char not in all_char:
			return False
	return True


def has_prefix(sub_s, w_dict):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param w_dict: (dict) A dict contains words in the dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if sub_s[0] not in w_dict:
		return False
	for word in w_dict[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
