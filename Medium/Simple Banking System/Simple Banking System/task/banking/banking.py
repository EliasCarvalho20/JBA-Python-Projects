from sys import exit
from random import randrange
from .database import *
from typing import Union


def generate_random_card() -> tuple:
    card_number = [4, 0, 0, 0, 0, 0]
    card_number += [randrange(10) for _ in range(9)]
    card_pin = [randrange(10) for _ in range(4)]
    return card_number, card_pin


def luhn_algorithm(args: Union[list, str]) -> bool:
    if type(args) == str:
        check_number = list(map(int, args))
    else:
        check_number = args[:]
        check_number.append(0)

    odd_sum = sum(check_number[-1::-2])
    even_sum = sum([sum(divmod(2 * n, 10)) for n in check_number[-2::-2]])

    return (odd_sum + even_sum) % 10


def create_card() -> tuple:
    card_number, card_pin = generate_random_card()
    checksum = luhn_algorithm(card_number)

    card_pin = ''.join(str(n) for n in card_pin)
    card_number = ''.join(str(n) for n in card_number)
    card_number += str((10 - checksum) % 10)

    add_account(connection, card_number, card_pin)
    return card_number, card_pin


def show_card(card_info: tuple) -> None:
    print("\nYour card have been created")
    print(f"Your card number:\n{card_info[0]}")
    print(f"Your card PIN:\n{card_info[1]}")


def login() -> None:
    check_card = input("\nEnter your card number:\n")
    check_pin = input("Enter your PIN:\n")
    cards = get_account_by_card(connection, check_card, check_pin)

    if cards:
        print("\nYou have successfully logged in!")
        account_options(cards)
    else:
        print("\nWrong card number or PIN!")


def account_options(cards: tuple) -> None:
    while (user_input := int(input(OPTIONS['OPTIONS']))) != 5:

        if user_input == 0:
            exit_program()
        elif user_input == 1:
            balance = get_balance(connection, cards[1])
            print(f"\nBalance: {balance[0]}")
        elif user_input == 2:
            amount_to_add = get_amount_balance()
            add_income(connection, cards[1], amount_to_add)
        elif user_input == 3:
            can_transfer(cards)
        elif user_input == 5:
            print("\nYou have successfully logged out!")
        elif user_input == 4:
            print("\nThe account has been closed!")
            deleted_account(connection, cards[1])
            break


def can_transfer(cards: tuple) -> bool:
    print("\nTransfer")
    verify_card = input("Enter card number:\n")

    if luhn_algorithm(verify_card) != 0:
        print("Probably you made mistake in the card number. Please try again!")
        return False
    elif verify_card == cards[1]:
        print("You can't transfer money to the same account!")
        return False
    elif not verify_account(connection, verify_card):
        print("Such a card does not exist.")
        return False

    amount_to_transfer = int(input("Enter how much money you want to transfer:\n"))
    amount_in_account = int(get_balance(connection, cards[1])[0])
    if amount_to_transfer > amount_in_account:
        print("Not enough money!")
        return False

    transfer(connection, [cards[1], verify_card], amount_to_transfer)
    print("Success!")


def get_amount_balance() -> int:
    amount = int(input("\nEnter income:\n"))
    print("Income was added!")
    return amount


def exit_program() -> None:
    print("\nBye!")
    exit()


OPTIONS = dict(
    SHOWS_MENU="\n1. Create an account\n2. Log into account\n0. Exit\n",
    OPTIONS="""\n1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n""")

connection = do_connection()
create_table(connection)

while True:
    user_input = int(input(OPTIONS["SHOWS_MENU"]))

    if user_input == 0:
        exit_program()
    elif user_input == 1:
        show_card(create_card())
    elif user_input == 2:
        login()
