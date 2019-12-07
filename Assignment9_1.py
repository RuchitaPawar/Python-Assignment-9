import os

def main():
 print("--------- Accepts file name from user and check whether that file exists in current directory or not ------")

 fileName = input("Enter file name :");
 isFile = os.path.isfile(fileName)

 if (isFile):
     absPath = os.path.isabs(fileName)

     if absPath == False:
        absPath = os.path.abspath(fileName)

     curDir = os.getcwd()
     # Join path of current working directory and file name
     curDir = os.path.join(curDir,fileName)
     if(absPath == curDir):
        print(fileName)
 else:
      print("This file is not present")

if __name__ == "__main__":
    main();




