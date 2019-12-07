import os
import sys


def main():

    print("------ Accept file name and one string from user and return the frequency of that string from file. --------")
    print()

    fileName1 = sys.argv[1];
    exists1 = os.path.isfile(fileName1)

    str = sys.argv[2];

    if(exists1):
        icnt = 0

        with open(fileName1, 'r') as f:
            for line in f:
                words = line.split()
                for i in words:
                    if (i == str):
                        icnt = icnt + 1
        print("Occurrences of the word ",str,icnt)
    else:
        print("File not exists")



if __name__ == "__main__":
    main();







