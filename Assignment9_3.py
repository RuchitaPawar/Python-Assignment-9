import os
import sys

def main():
 print("----------  accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. ------------")
 print("---------- Accept file name through command line arguments. ----------")
 print()

 fileName = sys.argv[1];
 exists = os.path.isfile(fileName)

 if(exists):
   fd = open(fileName,'r')
   f = open("Demo2.txt", "w")

   f.write(fd.read())
   fd.close()
   f.close()

   print("Data copied successfully")

 else:
  print("File not exists")


if __name__ == "__main__":
    main();


















