import re

def regex_strip(s, char=None):


    if not char:
        strip_left = re.compile(r'^\s*')
        strip_right = re.compile(r'\s*$')

        s = re.sub(strip_left, "", s)
        s = re.sub(strip_right, "", s)

    else:
        strip_char = re.compile(char)
        s = re.sub(strip_char, "", s)
    return s

if __name__ == '__main__':
    string_to_be_stripped = input("Enter string to stripped: ")
    char_to_be_removed = input("Enter character to removed, if none press enter: ")
    print(regex_strip(string_to_be_stripped, char_to_be_removed))