# AOC 2023 Day 1

# ----------------------------
# PART 1
# ----------------------------

def call_values(line):
    # adds char to list (digits) if it is a number
    digits = [char for char in line if char.isdigit()]
    # assigns first element of list to the variable "first_digit"
    first_digit = digits[0]
    last_digit = digits[-1]
    # concatenates both variables and converts them into integers
    return int(first_digit + last_digit)


total_call = 0
with open("1.calibration.txt", 'r') as file:  # assigns contents of text to "file"
    for line in file:  # iterates over each line in the file
        result = call_values(line)
        total_call += result
print(f"Total Calibration Value: {total_call}")


# ----------------------------
# PART 2
# ----------------------------

num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def call_values(line):
    digits = []  # stores numeric values
    i = 0  # counter to keep track of current position in line

    while i < len(line):  # iterates over each char in line
        matched = False  # var keeps track of wether a match was found in current line
        for key in num_dict:
            # checks if current position in line (i), starts with current key
            if line.startswith(key, i):
                # if true, value of key is added to digits list
                digits.append(num_dict[key])
                i += 1  # moves to next char
                matched = True  # changed to True: indicates match was found in current iteration
                break  # Break out of for loop

        # If no key is matched and the character is a digit, append the digit
        if not matched:
            if line[i].isdigit():  # checks if current position is a digit
                # converts char at position i into an int and appends it to digits list
                digits.append(int(line[i]))
            i += 1  # Move to the next char in line

    first_digit = digits[0]
    last_digit = digits[-1]
    return int(str(first_digit) + str(last_digit))


total_call = 0

with open("1.calibration.txt", 'r') as file:
    for line in file:
        result = call_values(line)
        total_call += result

print(f"Total Calibration Value: {total_call}")
