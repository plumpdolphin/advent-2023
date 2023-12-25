def part1():
    # Temporarily open file handle to save lines to array
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')

    # Get all digits for all lines as list comprehension
    digits = [
        [int(c) for c in line if c.isdigit()]
        for line in lines
    ]

    # Iterate list of digit arrays to calculate the calibration values.
    # Then, sum on the resulting array of integers
    return sum(
        [
            (d[0] * 10) + d[-1] 
            for d in digits
        ]
    )



def part2():
    # Same as before, loading lines in all at the start
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
    
    # Calculate the number for each line
    total = 0
    for line in lines:

        # Keep track of all known digits
        digits = []
        words = [
            'one', 'two', 'three',
            'four', 'five', 'six',
            'seven', 'eight', 'nine',
        ]

        for i, c in enumerate(line):
            # If character is a number
            if c.isdigit():
                digits.append(c)
                continue

            # Check if it is a word
            for j, word in enumerate(words):
                if line[i : i + len(word)] == word:
                    digits.append(str(j + 1))
        
        # Calculate number from first and last found digit
        line_val = int(digits[0] + digits[-1])

        # Add resulting value to the total sum
        total += line_val

    # Return resulting sum total
    return total



# Just to run the code above!
print(part1())
print(part2())