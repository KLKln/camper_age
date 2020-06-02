"""
Program: camper_age_input.py
Author: Kelly Klein
Last date modified: 6/2/2020
this program will...
"""


def convert_to_months(x=input('Enter age of child: ')):

    age = int(x)
    age_in_months = age * 12
    print("The child is", age_in_months, "months old")


convert_to_months()


#if __name__ == '__main__':
