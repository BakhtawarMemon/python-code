import re

def my_highlighter(syntax_file, theme_file, sourcefile_to_color):
    """This function colors parts of a file that matches with specified patterns (regex).

    Args:
        syntax_file (str): The (.synatx) file have lines of the form regex : name 
        where regex is a string specifying a regex, and name is some arbitrary 
        alphabetical string giving some name to the thing specified by the regex.
        
        theme_file (str): The (.theme) file have lines of the form name : color_sequence
        where name is one of the names specified in the matching .synatx file and
        color_sequence is some bash color sequence.

        sourcefile_to_color (str): The file you want to color

    Returns:
        Prints the colored version of the provided file onto the terminal.
    """
    
    with open(syntax_file,"r") as syntax:
        syntax_list = []                # create an empty list, syntax_list
        for line in syntax:             # for every line in the syntax file
            s = line.split(" ")         # split the line at space
            syntax_list.append(s[0])    # and append regex into syntax_list

    with open(theme_file,"r") as theme:
        theme_list = []
        for line in theme:
            t = line.split(";")
            theme_list.append(t[1])

    with open(sourcefile_to_color,"r") as source_file:
        text = source_file.read()               # store full text as a single string
    
    for i in range(len(syntax_list)):         # for all the regexes in the syntax line  
        regex = syntax_list[i]                # extract regex
        color = int(theme_list[i])            # extract color
        
        # substitute the text that matched the regex with the colored text
        text = re.sub(regex, "\033[{}m".format(color) + r"\1" + "\033[0m", text) 

    return print(text)

if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--syntax_file', type=str, help='Syntax file e.g., python.syntax', required = True) 
    parser.add_argument('-t', '--theme_file', type=str, help='Theme file, e.g., python.theme', required = True)
    parser.add_argument('-c', '--sourcefile_to_color', type=str, help='Demo file that you want to color, e.g., python.demo', required = True) 


    args = parser.parse_args()

    my_highlighter(args.syntax_file, args.theme_file, args.sourcefile_to_color)
