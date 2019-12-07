import hashlib
import os
import sys


def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def DisplayCheckSum(path):
    file_hash = hashfile(path)
    return file_hash

def main():
    print("----------- Accept two file names from user and compare contents of both the files. If both the files contains same contents then display success otherwise display failure.")
    print("----------- Accept names of both the files from command line.")
    print()


    fileName1 = sys.argv[1];
    exists1 = os.path.isfile(fileName1)

    fileName2 = sys.argv[2];
    exists2 = os.path.isfile(fileName2)

    if(exists1 and exists2):
        flie1Size = DisplayCheckSum(fileName1)
        flie2Size = DisplayCheckSum(fileName2)

        if(flie1Size == flie2Size):
            print("Success")
        else:
            print("Failure")

    else:
        print("file not exists")


if __name__ == "__main__":
    main();




