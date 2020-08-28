ingred = [200, 50, 15]
amount = [int(input("Write how many ml of water the coffee machine has: ")),
          int(input("Write how many ml of milk the coffee machine has: ")),
          int(input("Write how many grams of coffee beans the coffee machine has: "))]
capacity = [amount[0] // ingred[0], amount[1] // ingred[1], amount[2] // ingred[2]]

cups = int(input("Write how many cups of coffee you will need: "))
cups_max = min(capacity[0], capacity[1], capacity[2])

if cups_max > cups:
    print(f"Yes, I can make that amount of coffee (and even {cups_max - cups} more than that)")
elif cups > cups_max:
    print(f"No, I can make only {cups_max} cups of coffee")
else:
    print("Yes, I can make that amount of coffee")