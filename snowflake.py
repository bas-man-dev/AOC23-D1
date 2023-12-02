from collections import deque
import re

result = 0

swaps = {
    'nine': '9',
    'eight':'8',
    'seven': '7',
    'six': '6',
    'five': '5',
    'four': '4',
    'three': '3',
    'two': '2',
    'one': '1',
}

# Load file so we can work through all the data
with open("data.txt") as my_file:
    for line in my_file:
        numbers_string = ''
        line = line.strip()
        print(line)

        for k,v in swaps.items():
            if k in line:
                #if line.endswith(k):
                #    line = line.replace(k,v)
            
                line = line.replace(k,v)
        print(line)
        
        number_list = re.findall("\d+", line)
        print(f"num_lis{number_list}")

        for i in number_list:
            numbers_string += i
        print(f"num_string{numbers_string}")
        
        if len(numbers_string) < 1:
            pass 
        elif len(numbers_string) > 1:
            more_than = (int(f"{numbers_string[0] + numbers_string[-1]}"))
            print(f"more{more_than}")
            result +=  more_than
        else:
            single = (int(f"{numbers_string[0] + numbers_string[0]}"))
            print(f"single{single}")
            result += single
    
    print(result)
            


