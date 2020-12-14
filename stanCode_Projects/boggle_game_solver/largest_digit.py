"""
File: largest_digit.py
Name: James Shih
----------------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
count = 0


def main():
	"""
	Given a number, the program will find the largest digit of the number by a recursive algorithm.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function will execute a helper function to find the largest digit recursively.
	:param n: int, input number.
	:return largest: int, the largest digit of the number.
	"""
	global count
	# Make the input number positive.
	if n < 0:
		n *= -1
	largest = find_largest_helper(n, 0)
	print('Count: ', count)
	count = 0
	return largest


def find_largest_helper(n, largest):
	"""
	This function will recursively find the largest digit of an input number.
	:param n: int, input number.
	:param largest: int, initialized to zero.
	:return: int, the largest digit of the number.
	"""
	global count
	count += 1
	# If the input number is smaller than 1, return
	if n < 1:
		return largest
	else:
		# If the remainder is larger than largest, reassign largest as the remainder.
		if n % 10 > largest:
			largest = n % 10
		return find_largest_helper(int(n/10), largest)


if __name__ == '__main__':
	main()
