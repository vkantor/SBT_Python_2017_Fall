#coding=utf-8

from my_algo import analyze_sales
import argparse

parser = argparse.ArgumentParser()

# накидываем нужных нам аргументов
# Все аргументы кроме последнего - обязательные
parser.add_argument('--filename', required=True)
parser.add_argument('--date-field', required=True)
parser.add_argument('--good-count-field', required=True)
parser.add_argument('--total-money-field', required=True)
parser.add_argument('--start-date', required=True)
parser.add_argument('--finish-date', required=True)
parser.add_argument('--date-format', required=True)
parser.add_argument('--arg-date-format', required=False)

args = parser.parse_args()

analyze_sales(
	filename=args.filename, 
	date_field=args.date_field, 
	good_count_field=args.good_count_field, 
	total_money_field=args.total_money_field,
	start_date=args.start_date,
	finish_date=args.finish_date, 
	date_format=args.date_format,
	arg_date_format=args.arg_date_format
)