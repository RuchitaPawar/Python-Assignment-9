import os

def main():
 print("-------------  accept file name from user and open that file and display the contents of that file on screen. ----------------")
 fileName = input("Enter file name :");

 exists = os.path.isfile(fileName)

 if(exists):
  fd = open(fileName,'r')
  print("Contents of Whole file")
  print(fd.read())
  fd.close()

 else:
  print("File not exists")

if __name__ == "__main__":
    main();




