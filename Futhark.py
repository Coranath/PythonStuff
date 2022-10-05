#Futhark

import string

FuthDict = {
    'f':'\u16A0', 'u':'\u16A2', 'th':'\u16A6', 'a':'\u16A8', 'r':'\u16B1', 'k':'\u16B2',
    'g':'\u16B7', 'w':'\u16B9', 'h':'\u16BA', 'n':'\u16BE', 'i':'\u16C1', 'j':'\u16C3',
    'e':'\u16D6', 'p':'\u16C8', 'z':'\u16C9', 's':'\u16CA', 't':'\u16CF', 'b':'\u16D2',
    'm':'\u16D7', 'l':'\u16DA', 'b':'\u16D2', 'ng':'\u16DC', 'd':'\u16DE', 'o':'\u16DF', 'v':'\u16A0'}
"""I skipped eiwaz character since it is pronounced as the long e, and the first character is both f and v.
    Other than that there're a few like the thorn character that is a dipthong in english, and the ng.
    As of now neither "dipthong"s are functional.
"""

english = input('Please enter a string to be converted: ')

words = english.lower().split()

futhark = ''

for word in words:
    newWord = ''
    
    for i, letter in enumerate(word):

        if letter not in string.ascii_lowercase:
            continue

        try:
        
            #print(f'{letter} is letter #{i} in {word}, its Futhark equivalent is: {FuthDict[letter]}')

            newWord += FuthDict[letter]

        except:

            print(f'{letter} has no Futhark equivalent!')

            newWord += letter

    futhark += newWord + ' ' 
        
print(f'The phrase: {english} is written: {futhark} in Futhark')




