import pandas as pd
from colorama import Fore
import os

# Start
print("Duplicate Remover for Emails")
print("Files Must Be Stored Inside csvFiles \n")
print("EX - CSV FORMAT")
print("\t EMAIL")
print("\t test@email.com\n")

print(Fore.RED +"\tcased Sensitive *")
column = input(Fore.WHITE +"\tColumn Name : ")

# Variables
filteredCsv = {
    column: [],
}

print("\nMain File")
print("\tThe original csv file")
print(Fore.RED +"\tcased Sensitive *")
fileOne = input(Fore.WHITE +"\t\tFile Name : ")

print("\nSecond file")
print("\tThe file that contains the text to be remove from the Main File")
print(Fore.RED +"\tcased Sensitive *")
fileTwo = input(Fore.WHITE +"\t\tFile Name : ")

# Functions
def readFile(file):
    file_Data = pd.read_csv(fr"{file}.csv")
    file_List = file_Data[column].to_list()
    return file_List

try:
# File One
    fileOne_List = readFile(fileOne)

# File Two
    fileTwo_List = readFile(fileTwo)

# Algo
    [fileOne_List.remove(EmailTwo) for EmailTwo in fileTwo_List for EmailOne in fileOne_List if EmailTwo == EmailOne]
    fileOne_List.sort()
    filteredCsv[column] = fileOne_List

    data = pd.DataFrame(filteredCsv)
    
    if not os.path.exists("filtered"):
        os.makedirs("filtered")

    data.to_csv(fr"filtered\\Filtered.csv", index=False)

    print("\nFilter Complete | File is Located in Filtered Folder")
except NameError:
    print(f"\nName Error | Error : {NameError}")
except FileNotFoundError: 
    print(f"\nFile Not Found | Error : {FileNotFoundError}") 
except PermissionError:
    print(f"\nPermission Problem | Error : {PermissionError}")
except IsADirectoryError:
    print(f"\nDirectory Problem | Error : {IsADirectoryError}")
except KeyError:
    print(f"\nColumn Not Found | Error : {KeyError}")

input("\n Press enter to close...")
# End
    