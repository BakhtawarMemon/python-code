import re
import argparse
from highlighter import my_highlighter

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--regex', type=str, help="This is the regex pattern\
                    you want to match in your file. Can take multiple regexes", 
                    required = True, nargs="+") 
parser.add_argument('-f', '--filename', type=str, help='This is the file you want to find the\
                    pattern in e.g., grep.demo', required = True)
parser.add_argument('--highlight', help='', default="off", choices=["on"], required = False) 


args = parser.parse_args()
regex = args.regex ; file_name = args.filename ; color = args.highlight
color_length = len(regex)       #number of colors will be same as number of regexes


with open("grep.syntax", "w+") as syntax:           # creating/opening a .syntax file
    for r in regex:                                 # and writing regexes provided
        syntax.write("({}) : regex\n".format(r))    # by the user into that file

with open("grep.theme", "w+") as theme:             # creating/opening a .theme file
    colors = [33,34,35,92,93,94,95]                 # colors for different regexes
    for c in range(color_length):                   # assigning colors to regexes provided
        theme.write("regex: 0;{}\n".format(colors[c])) # by the user and writing these in file

with open("grep.match","w") as match:               #creating/openinng a .match file
    with open(file_name,"r") as my_file:            #reading sourcefile
            for line in my_file:                    #for each line in source file
                for pattern in regex:               #for each pattern in regex
                    if re.search(pattern,line):     #if pattern matched
                        match.write(line + "\n")    #write the line

"""
If two or more regexes appear in the same line, the line will be 
printed the number 'regex' times. For instance, if three different 
regexes appear in the same line, the line is printed three times.   
"""

# To avoid same line being printed many times
match = ""
lines_seen = set() #holds lines already seen
output_file = open("grep_unique.match", "w")
for line in open("grep.match", "r"):
    if line not in lines_seen: #not a duplicate
        output_file.write(line)
        match+=line
        lines_seen.add(line)
output_file.close()

if color == "on":
    my_highlighter("grep.syntax","grep.theme", "grep_unique.match")
else:
    print(match)

