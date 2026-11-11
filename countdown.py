"""
By : David Hornaday
Python
countdown.py. takes a number from the user and counts down from it
"""

import time

WAIT_TIME = 1

def number_to_countdown():
    """
    Takes a input from the user and checks if it is a vaild number

    :return: The number to countdown from
    :rtype: int
    """
    able = False
    while not able:
        try:
            num = int(input("Enter a Number to countdown from in seconds:\t"))
            able = True
        except ValueError:
            print("Please Enter a number")
    return num

def countdown(num):
    """
    Uses the number from the a countes down the number until 0

    :param: The users number
    """
    while num > 0:
        print(num)
        num -= 1
        time.sleep(WAIT_TIME)
    print("GOOO!!!!")

def main():
    again = False
    while not again:
        num = number_to_countdown()
        countdown(num)
        try:
            loop = input("Would You want to do another Countdown (y/n):\t").lower()
            if loop != 'y':
                print("END")
                again = True
        except ValueError:
            print("Enter y or n to continue")

if __name__ == "__main__":
    main()