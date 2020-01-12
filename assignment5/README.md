# 5.1 and 5.2
## Files: 
- highlighter.py 
- python.syntax 
- python.theme 
- python2.theme 
- demo.py

The script ```highlighter.py``` requires user to provide three arguments from command line namely *synatx file*, *theme file* and *source file to color* and passes these to function ```my_highlighter(syntax_file, theme_file, sourcefile_to_color)```. The function processes the arguments and returns 
the colored version of the source file depending on the parts of the file that matched with the regexes specified in the  syntax file.

**Example usage**

    python highlighter.py -h

    python highlighter.py --help

    python highlighter.py -s python.syntax -t python.theme -c demo.py

    python .\highlighter.py -s .\python.syntax -t .\python2.theme -c .\demo.py

# 5.3

## Files
- cplusplus.syntax
- cplusplus.theme
- demo.cpp

**Example usage**

    python highlighter.py -s cplusplus.syntax -t cplusplus.theme -c demo.cpp

# 5.4

The script ```grep.py``` requires user to provide two arguments from the command line namely *regex* and a *demo file*. It will return the lines in the demo file that matched with the regex. User can provide arbitrary number of regexes (maximum: 6). If you want matched lines/parts of file to be colored call it with ```--highlight on```

## Files
- grep.py
- grep.demo

**Example usage**
    
    python grep.py -r [abc] -f grep.demo
    python grep.py -r [abc] -f grep.demo --highlight on
    python grep.py -r '[abc]' '\bAn\b' -f grep.demo --highlight on
    python grep.py -r [abc] \bTo\b \An\b -f grep.demo --highlight on

The script ```grep.py``` creates four extra files inside it.
- grep.syntax
- grep.theme
- grep.match
- grep_unique.match

# 5.5 and 5.6

The script ```diff.py``` requires user to provide two arguments from command line namely *original file* and *modified file*. The script compares both the files and outputs what is different in modified file from original file on the console.

## File
- diff.py
- original.txt
- modified.txt
- diff.syntax
- diff.theme

**Example usage**

    python diff.py -o original.txt -m modified.txt

The script ```diff.py``` creates one extra file
- diff_output.txt
