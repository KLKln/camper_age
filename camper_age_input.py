"""
Program: camper_age_input.py
Author: Kelly Klein
Last date modified: 6/2/2020
this program will take input from user for the age
    of a in years child and return age in months
"""


def convert_to_months(years):
    return int(years) * 12


if __name__ == '__main__':
    years = input('Enter age of child: ')
    months = convert_to_months(years)
    print("The child is", months, "months old")
