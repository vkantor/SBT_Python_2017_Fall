#coding=utf-8

from my_algo import analyze_sales
import sys

# если мы утвердим порядок аргументов, то распарсить будет очень просто

if len(sys.argv) == 9:
	(
		filename, 
		date_field, 
		good_count_field, 
		total_money_field,
		start_date,
		finish_date, 
		date_format,
		arg_date_format
	) = sys.argv[1:]
elif len(sys.argv) == 8:
	(
		filename, 
		date_field, 
		good_count_field, 
		total_money_field,
		start_date,
		finish_date, 
		date_format
	) = sys.argv[1:]
	arg_date_format = None
else:
	raise ValueError('Invalid number of arguments')

analyze_sales(
	filename=filename, 
	date_field=date_field, 
	good_count_field=good_count_field, 
	total_money_field=total_money_field,
	start_date=start_date,
	finish_date=finish_date, 
	date_format=date_format,
	arg_date_format=arg_date_format
)