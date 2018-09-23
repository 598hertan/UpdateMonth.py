#!/usr/bin/python35

from sys import argv

"""
Author: James Hertan
09/03/2015

DESCRIPTION: Open a text file of dates, read the list of dates, update the list of dates by incrementing the month by one.
"""
from sys import argv
import pyperclip

def update_month(string):
    """
    Input a string in MM/DD/YYYY format; Returns an updated string incrementing the month by 1
    """

    new_month = int(string.split("/")[0]) + 1  # takes the month, increments the month by one
    new_day = int(string.split("/")[1])
    new_year = int(string.split("/")[2])


    if new_month == 13:
        new_month = 1
        new_year += 1

    return str(new_month) + "/" + str(new_day) + "/" + str(new_year)

def update_dates(list):
    """takes a list of dates and outputs a revised list with updated months"""
    new_list = []

    for i in list:
        item = update_month(i)
        new_list.append(item)
    return "\n".join(new_list)

def generate_dates_file(file_name):
    """
    NOT USED
    :param file_name: Takes a file with a list of dates
    :return: rewrites the file with an updated list of dates increment the month by 1
    """

    try:
        with open(file_name, "r+") as fh:  # open the file, creates a list of dates, prints the updated months list
            indata = fh.readlines()
            new_dates = update_dates(indata)
            print (new_dates)
            pyperclip.copy(new_dates)
    except FileNotFoundError:
        print("{} not found!".format(file_name))
    else:
        with open(file_name, "w") as fh:  # opens the file, writes the updated list of dates
            fh.write(new_dates)

def print_dates(my_l):
    """Print a list of dates to the terminal"""
    for date in my_l:
        print(date)

def get_updated_dates():
    """Primary program: Takes the clipboard and generates a new list of dates with an incremented month to copy to the clipboard"""

    updated_content = []
    content = pyperclip.paste()
    # print(content)

    for date in content.split("\n"):
        try:
            # print(date)
            new_date = update_month(date)
            # print("New date {}".format(new_date))
            updated_content.append(new_date)
        except ValueError:
            print("Skipping '{}'.Program failed to recognize this value.".format(str(date)))

    print_dates(updated_content)
    pyperclip.copy("\n".join(updated_content))

def main():
    get_updated_dates()
    
if __name__ == "__main__": main()
