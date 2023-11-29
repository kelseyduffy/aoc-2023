nums = []
with open('inputs/test.in','r') as f:
    for x in f.readlines():
        nums.append(int(x))

print(sum(nums))

freqs = { 0 }
freq = 0
found = False

while not found:
    for num in nums:
        new_freq = freq + num
        if new_freq in freqs:
            print (new_freq)
            found = True
            break

        freqs.add(new_freq)
        freq = new_freq