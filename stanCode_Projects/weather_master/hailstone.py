"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program will first ask user input a number (integer), then it
    will simulate the execution of the Hailstone sequences of that input.
    Every round the program will check whether the number is even or
    odd to decide how to modify the number, until the number reach 1.
    """
    print('This program computes Hailstone sequences')
    # Variable 'count' will count how many step to reach 1.
    count = 0
    # Variable 'maximum' will finally be the biggest number in each Hailstone sequence.
    maximum = 0
    # Input an integer, if input a float, the program will do floor division then change it to an integer.
    num = int(float(input('Enter an integer: ')) // 1)
    # The program will check whether input is at least 1.
    if num <= 0:
        print('Input must be at least 1')
    else:
        # If the first input is 1, the program stops.
        if num == 1:
            print('It took ' + str(count) + ' step(s) to reach 1')
        else:
            # The while loop will keep running until the number reach 1.
            while num != 1:
                # If the number is even.
                if num % 2 != 0:
                    print(str(int(num)) + ' is odd, so I make 3n+1: ' + str(int(3 * num + 1)))
                    if num > maximum:
                        maximum = num
                    # Reassign the number.
                    num = 3 * num + 1
                    count += 1
                # If the number is odd.
                else:
                    print(str(int(num)) + ' is even, so I take half: ' + str(int(num / 2)))
                    if num > maximum:
                        maximum = num
                    # Reassign the number.
                    num = num / 2
                    count += 1
            # Print the results: Steps used and the biggest number in the Hailstone sequences.
            print('It took ' + str(count) + ' step(s) to reach 1')
            print('The biggest number in the Hailstone sequences is: ' + str(int(maximum)))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
