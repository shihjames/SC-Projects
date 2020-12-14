"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100


def main():
	"""
	This program will ask user to enter several temperatures and
	the exit code is -100. After that, the program will show the value of
	the highest temperature, the lowest temperature, average temperature
	and how many cold days from all the input temperature.
	"""
	print('stanCode "Weather Master 4.0"!')
	# Ask for first temperature input.
	temp = float(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	# If the first input is EXIT Code, the program will stop.
	if temp == EXIT:
		print('No Temperature was entered')
	else:
		# Assign some variables to the first input.
		maximum = temp
		minimum = temp
		temp_sum = temp
		# Variable 'count' will count how many times did the user enter a number.
		count = 1
		# Variable 'Cold_day' will count how many cold days (temperature below 16 degree).
		if temp < 16:
			cold_day = 1
		else:
			cold_day = 0
		while True:
			new_temp = float(input('Next Temperature: (or -100 to quit)? '))
			# If user input -100 (Exit code), the program will start to print the result.
			if new_temp == EXIT:
				break
			elif new_temp > maximum:
				maximum = new_temp
				if new_temp < 16:
					cold_day += 1
				count += 1
				temp_sum = (temp_sum + new_temp)
			elif new_temp < minimum:
				minimum = new_temp
				if new_temp < 16:
					cold_day += 1
				count += 1
				temp_sum = (temp_sum + new_temp)
			else:
				count += 1
				if new_temp < 16:
					cold_day += 1
				temp_sum = (temp_sum + new_temp)
		print('Highest Temperature: ' + str(maximum))
		print('Lowest Temperature: ' + str(minimum))
		print('Average: ' + str(temp_sum / count))
		print(str(cold_day) + ' Cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
