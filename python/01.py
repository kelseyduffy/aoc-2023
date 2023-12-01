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
# answer: 55123

number_words = [
    ('twone','21'),
    ('eightwo','82'),
    ('oneight','18'),
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
    ('ten', '10'),
    ('eleven', '11'),
    ('twelve', '12'),
    ('thirteen', '13'),
    ('fourteen', '14'),
    ('fifteen', '15'),
    ('sixteen', '16'),
    ('seventeen', '17'),
    ('eighteen', '18'),
    ('nineteen', '19'),
    ('twenty', '20'),
    ('thirty', '30'),
    ('forty','40'),
    ('fifty','50'),
    ('sixty','60'),
    ('seventy','70'),
    ('eighty','80'),
    ('ninety','90'),
]

total_calibration = 0

for string in strings:
    replaced = string
    for (word, number) in number_words:
        replaced = replaced.replace(word, number)

    just_numbers = [char for char in replaced if char.isdigit()]
    total_calibration += 10 * int(just_numbers[0])
    total_calibration += int(just_numbers[-1])

print(total_calibration)
# 54851 is too low
# 55211 is too low
# answer: 55260