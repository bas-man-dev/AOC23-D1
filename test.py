import re

result = 0

swap = {'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',}

with open(data.txt) as file:
     for line in file:
         numbers_string = ''
         line = line.strip()

