strings = []
with open('inputs/01.in','r') as f:
    for x in f.readlines():
        strings.append(x)

total_calibration = 0

for string in strings:
    just_numbers = [char for char in string if char.isdigit()]
    total_calibration += 10 * int(just_numbers[0])
    total_calibration += int(just_numbers[-1])

print(total_calibration)