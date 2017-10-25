#coding=utf-8

from my_algo import analyze_sales
import argparse

def calc_bank_values(my_pennies, percent_bank, percent_shares, percent_lending):
	revenue_bank = my_pennies * percent_bank
	revenue_shares = my_pennies * percent_shares
	revenue_lending = my_pennies * percent_lending

	additional_revenue_shares = revenue_shares - revenue_bank
	additional_revenue_lending = revenue_lending - revenue_bank

	relative_shares = additional_revenue_shares / revenue_bank
	relative_lending = additional_revenue_lending / revenue_bank
	
	print('relative shares is {:.2f}, relative lending is {:.2f}'.format(relative_shares, relative_lending)) 

parser = argparse.ArgumentParser()

# накидываем нужных нам аргументов
# но теперь не забываем про тип
parser.add_argument('--my-pennies', type=float)
parser.add_argument('--percent-bank', type=float)
parser.add_argument('--percent-shares', type=float)
parser.add_argument('--percent-lending', type=float)

args = parser.parse_args()

calc_bank_values(
	my_pennies=args.my_pennies,
	percent_bank=args.percent_bank, 
	percent_shares=args.percent_shares, 
	percent_lending=args.percent_lending
)