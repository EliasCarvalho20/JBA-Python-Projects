income = int(input())

def show_taxes(cash, porc=None):
    print("The tax for {} is {}%. That is {} dollars!"
          .format(cash, round(porc * 100), round(cash * porc)))

if income < 15528:
    show_taxes(income, 0)
elif income < 42708:
    show_taxes(income, 0.15)
elif income < 132407:
    show_taxes(income, 0.25)
else:
    show_taxes(income, 0.28)
