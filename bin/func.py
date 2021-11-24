
from os import truncate


def removeWhitespace(string : str) -> str:          
    string = string.replace(f' ','')
    string = string.replace(f'\t','')
    string = string.replace(f'\n','')
    return string

def removeTo(string : str, word : str):
    
    while(True):
        
        pass

def doCharsAppearInStr(string : str, chars : str) -> bool:
    posChar = 0
    for i in string:
        if chars[posChar] == i:                                     
            posChar += 1 
        if posChar == len(chars):
            return True
    else: return False

def doWordsAppearInStr(string : str, *words : str) -> bool:
    if not string:
        return False
    
    inStringPos = 0
    inWordsPos = 0

    while(True):
        if string[inStringPos] == words[inWordsPos][0]:
            for char in words[inWordsPos]:
                if char != string[inStringPos]:
                    break
                inStringPos += 1

            else: inWordsPos += 1

        inStringPos += 1
        if len(string) == inStringPos: return False
        if len(words) == inWordsPos: return True
