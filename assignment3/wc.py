#!/usr/bin/env python
import sys
import os
import glob

def myfunction(file):
    """This function counts words, lines and characters in file
    
    Args:
        file (str): The file path to open and work upon 
    
    Returns:
        Nothing. Just prints number of lines, words, characters and file name
    """
    with open(file, 'r') as f:              #open the file
        contents = f.read()                 #read and store contents in a variable
        a = len(contents.split('\n'))       #split at \n to count lines
        b = len(contents.split())           #split at whitespace to count words
        c = len(contents)                   #length of contents shows number of characters
        print(f'Lines {a}, words {b}',       
        f'characters {c}, file {f.name}')

filename = sys.argv[1]                      #command line argument from user is stored in variable filename

if filename == '*':
    for file in os.listdir(os.getcwd()):    #list of file paths in current directory
        myfunction(file)                    

elif filename == '*.py':
    for file in glob.glob('*.py'):          #list of file paths matching the pattern
        myfunction(file)

else:
    myfunction(filename)
