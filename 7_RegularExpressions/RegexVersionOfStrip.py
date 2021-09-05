import re

str = input('Enter the string you want to strip:')
charToStrip = input('Enter chars to be stripped:')

#....... Section 3.2.1 Issue #32 .......
def RegexVersionOfStrip(s, chars=None):
    if not chars:
        lStrip = re.compile(r'^\s*')    #String starting with whitespace
        rStrip = re.compile(r'\s*$')   #String ending with whitespace
    else:
        lStrip = re.compile(r'^[' + re.escape(chars) + r']*')
        rStrip = re.compile(r'[' + re.escape(chars) + r']*$')
    s = re.sub(lStrip, '', s)  #replacing lStrip with '' in s
    s = re.sub(rStrip, '', s)  #replacing rStrip with '' in s
    return s

print(RegexVersionOfStrip(str, charToStrip))
