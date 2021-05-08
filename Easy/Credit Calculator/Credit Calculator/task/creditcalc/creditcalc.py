import argparse
import math
import sys


def plural(string):
	year, month = 'year', 'month'

	if string[0] > 1:
		year += 's'
	if string[1] > 1:
		month += 's'

	return year, month


def convert_periods(periods):
	if periods == 1:
		return f"You need 12 months to repay this credit!"

	periods = divmod(periods, 12)
	year, month = plural(periods)
	if periods[0] < 1:
		return f"You need {periods[1]} {month} to repay this credit!"
	elif periods[0] >= 1 and periods[1] == 0:
		return f"You need {periods[0]} {year} to repay this credit!"

	return f"You need {periods[0]} {year} and {periods[1]} {month} to repay this credit!"


def count_none_type(args_list):
	count = 0
	for arg in args_list:
		if arg is None:
			count += 1

		if count > 1:
			print(incorrect)
			sys.exit()


def calculate_interest_rate(interest, periods=0):
	rate = interest / (12 * 100)
	if periods != 0:
		return rate * pow(1 + rate, periods) / (pow(1 + rate, periods) - 1)
	return rate


def calculate_monthly_payment(principal, monthly_payment, interest):
	rate = calculate_interest_rate(interest)
	periods = math.ceil(math.log((monthly_payment / (monthly_payment - rate * principal)), 1 + rate))
	over_payment = int(periods * args.payment - principal)
	print(convert_periods(periods))
	print(f"Overpayment = {over_payment}")


def calculate_annuity(principal, periods, interest):
	annuity = math.ceil(principal * calculate_interest_rate(interest, periods))
	over_payment = int(annuity * periods - principal)
	print(f"Your annuity payment = {math.ceil(annuity)}!")
	print(f"Overpayment = {over_payment}")


def calculate_months(monthly_payment, periods, interest):
	principal = monthly_payment / calculate_interest_rate(interest, periods)
	over_payment = int(args.payment * periods - principal)
	print(f"Your credit principal = {principal:.0f}!")
	print(f"Overpayment = {over_payment}")


def overpayment(principal, periods, interest):
	rate = calculate_interest_rate(interest)
	over_payment = principal

	for n in range(1, periods + 1):
		diff = math.ceil((principal / periods) + rate * (principal - (principal * (n - 1)) / periods))
		over_payment -= diff
		print(f"Month {n}: paid out {diff}")

	print(f"\nOverpayment = {over_payment}")


def check_args():
	args_list = [args.payment, args.periods, args.principal, args.interest]

	if args.type is None or (args.type not in ["annuity", "diff"]):
		print(incorrect)
		sys.exit()
	elif args.type == "diff":
		if args_list[2] is None or args_list[1] is None or args_list[3] is None:
			print(incorrect)
			sys.exit()
	elif args.type == "annuity":
		count_none_type(args_list)

	if args.type == "diff":
		overpayment(args_list[2], args_list[1], args_list[3])
	else:  # 0 payment #1 periods #2 principal #3 interest
		if args_list[0] is None:
			calculate_annuity(args_list[2], args_list[1], args_list[3])
		elif args_list[1] is None:
			calculate_monthly_payment(args_list[2], args_list[0], args_list[3])
		elif args_list[2] is None:
			calculate_months(args_list[0], args_list[1], args_list[3])


if __name__ == '__main__':
	incorrect = "Incorrect parameters"

	parser = argparse.ArgumentParser(description='Credit Calculator')
	parser.add_argument("--type", type=str, help="type of credit")
	parser.add_argument("--payment", type=float, help="the monthly payment")
	parser.add_argument("--principal", type=float, help="calculates both types of payment")
	parser.add_argument("--periods", type=int, help="number of months and/or years")
	parser.add_argument("--interest", type=float, help="credit interest")
	args = parser.parse_args()
	check_args()
