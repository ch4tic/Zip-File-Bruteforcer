#!/usr/bin/python3

# importing some modules
import time
import os
import zipfile

def main():
    # opening wordlist file in rb mode since file can have special characters
    with open(wordlist, 'rb') as file: 
        for line in file: 
            for word in line.split():
                try: 
                    filename.extractall(pwd=word) # extracting the zip file with found password 
                    print("\n") # printing a new line 
                    time.sleep(.5) # time delay
                    print("Password: ", word.decode()) # outputing the found password 
                    return True
                except: 
                    continue 
        return False

os.system("clear") # clearing the screen 
# printing a banner on start 
print("-----------------------")
print(" Zip File Brute-forcer ")
print("-----------------------")
time.sleep(1)
wordlist = input("Wordlist: ")
time.sleep(.5) # time delay
zip_file = input("Zip file: ")
filename = zipfile.ZipFile(zip_file) # initializing the zipfile object with user's filename 

if main() == False:
    print("Password not found!")
