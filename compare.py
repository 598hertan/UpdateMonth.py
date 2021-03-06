#!/usr/bin/python2

from sys import argv


def find_match(a, b):  # Compare two lists and returns any matches
    temp = []

    for i in a:
        for j in b:
            if i == j:
                temp.append(i)
    return "\n".join(temp)


def main():

    if len(argv) == 4:
        script, file1, file2, file3 = argv

        with open(file1, "r") as filehandle:  # open the file1, read its contents
            indata1 = filehandle.read().splitlines()
            filehandle.close()

        with open(file2, "r") as filehandle:  # open the file2, read its contents
            indata2 = filehandle.read().splitlines()
            filehandle.close()

        print(find_match(indata1, indata2))  # prints any matches in the interpreter

        with open(file3, "w") as filehandle:  # output a file with the matches
            filehandle.write(find_match(indata1, indata2))
            filehandle.close()

        print("{} create".format(file3))

    else:
        print("You did not identify 2 files to compare and a file to output.")




if __name__ == "__main__": main()
