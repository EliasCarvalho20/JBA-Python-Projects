user_dict = input().split(' ')
count = {}

for letter in user_dict:
    letter = letter.lower()
    if letter in count:
        count[letter] = count[letter] + 1
    else:
        count.update({letter: 1})

for key in count.keys():
    print(key, count[key])
