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

for game in games:
    
    ruled_out = False

    (id, result) = game.split(':')
    
    pulls = result.strip().split(';')
    
    for pull in pulls:
        counts = pull.strip().split(',')

        for count in counts:
            (num, color) = count.strip().split(' ')

            if int(num) > limits[color]:
                ruled_out = True

    if not ruled_out:
        total_ids += int(id.strip().split(' ')[1])

print(total_ids)
# answer: 2593
