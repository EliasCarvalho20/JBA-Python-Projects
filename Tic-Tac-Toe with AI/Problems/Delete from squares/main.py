input_key = int(input())
if squares.get(input_key) is None:
    print("There is no such key")
else:
    print(squares.pop(input_key))
print(squares)
