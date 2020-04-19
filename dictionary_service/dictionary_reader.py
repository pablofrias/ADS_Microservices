# Read/Search words from dictionary
import re

def search(word):
    sentiment = [
        {
            'word': word.strip(),
            'value': 0
        }
    ]

    with open("./data/AFINN-111.txt") as dictionary:
        for line in dictionary:
            w,value = re.split("\t", line)
            if word == w :
                sentiment = [
                    {
                        'word': w.strip(),
                        'value': int(value.strip())
                    }
                ]
                break
    
    return sentiment