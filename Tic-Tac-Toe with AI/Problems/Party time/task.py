new_list = []
while True:
    string = input()
    if '.' not in string:
        new_list.append(string)
    else:
        break


print(new_list)
print(len(new_list))
