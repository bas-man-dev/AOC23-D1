from collections import deque
import re

result = 0

# Load file so we can work through all the data
with open("data.txt") as my_file:
    for line in my_file:
        numbers_string = ''
        line = line.strip()
        number_list = re.findall("\d+", line)

        for i in number_list:
            numbers_string += i
        
        if len(numbers_string) < 1:
            pass 
        elif len(numbers_string) > 1:
            result += (int(f"{numbers_string[0] + numbers_string[-1]}"))
        else:
            result += (int(f"{numbers_string[0] + numbers_string[0]}"))
    
    print(result)
            


