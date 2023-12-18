def get_number(line):
    digits = [c for c in line if c.isdigit()]
    return int( str(digits[0]) + str(digits[-1]) ) 

with open('input.txt') as f:
    sum = 0
    for line in f:
        sum += get_number(line)
    print(sum)