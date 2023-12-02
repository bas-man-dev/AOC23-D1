result = 0
# use to cast all the numbers to written out
number_as_string = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine', 
}
# use to swap any found written numbers to a digital number
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

        for k,v in number_as_string.items():
            if k in line:
                line = line.replace(k,v)
        # walking up the string getting all possible number values
        for i in range(len(line)):
            new_line = line[i:]
            # adding the values to a string (so we can index them and use with f strings later)
            for k, v in swaps.items():
                if new_line.startswith(k):
                    numbers_string += v

        # miss any blank lines, add the first and last or double any single digits

        if len(numbers_string) < 1:
            pass
        # easier to do as f strings ?
        elif len(numbers_string) > 1:
            result +=  int(f"{numbers_string[0] + numbers_string[-1]}")
        else:
            result += int(f"{numbers_string[0] + numbers_string[0]}")
    # Final result
    print(result)



