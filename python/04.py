from functools import reduce

cards = []
with open('inputs/04.in','r') as f:
    for x in f.readlines():
        cards.append(x)

points = 0

for card in cards:
    info = card.strip().split(':')[1]
    (winning_numbers_text, player_numbers_text) = info.strip().split('|')

    winning_numbers = { int(x) for x in winning_numbers_text.strip().split()}
    player_numbers = [int(x) for x in player_numbers_text.strip().split()]

    winner_count = 0

    for number in player_numbers:
        if number in winning_numbers:
            winner_count += 1

    if winner_count > 0:
        points += 2**(winner_count - 1)

print(points)
# answer 21105