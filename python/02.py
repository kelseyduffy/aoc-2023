games = []
with open('inputs/02.in','r') as f:
    for x in f.readlines():
        games.append(x)

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total_ids = 0
total_powers = 0

for game in games:

    mins = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    
    ruled_out = False

    (id, result) = game.split(':')
    
    pulls = result.strip().split(';')
    
    for pull in pulls:
        counts = pull.strip().split(',')

        for count in counts:
            (num, color) = count.strip().split(' ')

            if int(num) > mins[color]:
                mins[color] = int(num)

            if int(num) > limits[color]:
                ruled_out = True

    if not ruled_out:
        total_ids += int(id.strip().split(' ')[1])

    total_powers += mins['blue'] * mins['green'] * mins['red']

print(total_ids)
# answer: 2593

print(total_powers)
# answer: 54699
