import re

"""
Regex operation matches

. - Any character except new line
\d - Digit (0-9)
\D - Not a Digit (0-9)
\w - Word Character (a-z, A-Z, 0-9, _)
\W - Not a Word Character
\s - Whitespace (space, tab,newline)
\S - Not whitespace (space,tab,newline)
\b - Word Boundary  #indicated by whitespace or non-alphanumeric character such as -
\B - Not a word Boundary
^ - Beginning of a String
$ - End of a string
[] - Matches characters in brackets
[^ ] - Matches characters NOT in

Quantifiers:
*  - 0 or more
*  - 1 or more
? - 0 or one
{3}  - Exact Numbers
(3,4) range of numbers (min,max
"""
# using a '.' allows you to match everything



text_to_search= """abcdefghijklmnopqrstuvwxyz' \
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
               '123456789' \
               'Ha HaHa' \
               'coreyms.com' \
               'MetaCharacters (need to be escaped): . ^ $ * + ? { } [ ] \ | ( )' \
               '321-555-4321' \
               '123.555.1234' \
               '800.555.1234' \
               '400.555.1234' \
               '' \
               '' \
               '' \
               'Mr. Schafer' \
               'Mr. Smith' \
               'Ms. Davis' \
               'Mrs. Robinson' \
               'Mr. T' \
               'cat' \
               'mat' \
               'pat' \
               'bat'
               """

sentence= 'Start a sentence and then bring it to an end'

#pattern= re.compile(r'coreyms\.com')  #find this particular string in order and it is case-sensitive. Literal search

pattern= re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  #pattern for digits

pattern= re.compile(r'\d\d\d[-\.]\d\d\d[-\.]\d\d\d\d')  #only match where there is a dash or a dot and not any other character

pattern= re.compile(r'[8-9]00[-\.]\d\d\d[-\.]\d\d\d\d')  #only match where there is all of above and but only start with 800 number.

pattern = re.compile(r'[1-5]') #match numbers

pattern = re.compile(r'[a-zA-z]') #match letters

pattern = re.compile(r'[^a-zA-z]') #match everything not a lowercase or uppercase letter

pattern = re.compile(r'[^b]at') #want to match the words cat mat pat and all three letter words ending in 'at' but not bat. match any single not an A then followed by 'at'

pattern = re.compile(r'\d{3}[-\.]\d{3}[-\.]\d{4}')  #match 3 digits and then - or '.'

pattern = re.compile(r'Mr\.?\s[A-Z]\w')  #match Mr with a period but the period is optional.  Then match the white space after and then the rest of the letters a-z.

#pattern = re.compile(r'Mr[\.?\s[a-zA-z]')

matches = pattern.finditer(text_to_search) #returns an iterator that contains all the matches with a span and match itself.
#span is beginning and end index of match.

for match in matches:
    print(match)

#print(text_to_search[0:3])
#print(text_to_search)