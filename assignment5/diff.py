import re
import argparse
from highlighter import my_highlighter

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--original_file', type=str, 
                    help='This is the original file e.g., original.txt', required = True)
parser.add_argument('-m', '--modified_file', type=str, 
                    help='This is the modified file e.g., modified.txt', required = True)

args = parser.parse_args()

modified_list = []                                
with open(args.modified_file, "r") as modified:
    for l in modified:                  # for each line in modified file
        line = l.strip()                # strip leading or trailing whitespace 
        modified_list.append(line)      # and append it to list variable

original_list = []
with open("diff_output.txt", "w") as out:
    with open(args.original_file, "r") as original:
        for l in original:
            line = l.strip()
            if line in modified_list:       
                original_list.append(line)
                # print("0  " + line)
                out.write("0  " + line + "\n")
            else:
                original_list.append(line)
                # print("-  " + line)
                out.write("-  " + line + "\n")

    for i in modified_list:
        if i not in original_list:
            # print("+  " + i)
            out.write("+  " + i + "\n")

my_highlighter("diff.syntax", "diff.theme", "diff_output.txt")