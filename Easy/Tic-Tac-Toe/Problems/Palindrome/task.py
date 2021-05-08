word = input()
cut = int(len(word) / 2)
palin = word[cut:][::-1] == word[:cut]
print("Palindrome" if palin else "Not palindrome")
