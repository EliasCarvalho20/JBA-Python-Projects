phrase = input().split()
word = list()

for p in phrase:
    if p.endswith('s'):
        word.append(p)

print("_".join(word))
