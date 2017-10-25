#coding=utf-8

from my_algo import analyze_sales
import argparse

# глобальные комментарии по скрипту
parser = argparse.ArgumentParser(description='the script reads file and calcs total money and total goods in the given date diapason')

# накидываем нужных нам аргументов
# Все аргументы кроме последнего - обязательные
# Пишем краткое объяснение что означает параметр

# добавим для первого аргумента котороткую опцию -f, чтобы не нужно было писать полностью --filename
parser.add_argument('-f', '--filename', required=True, help='Path to file with data')
parser.add_argument('--date-field', required=True, help='A name of the field containing date. Usually it is "date"')
parser.add_argument('--good-count-field', required=True, help='A name of the field containing goods  count. Usually it is "good_count"')
parser.add_argument('--total-money-field', required=True, help='A name of the field containing total money. Usually it is "total_money"')
parser.add_argument('--start-date', required=True, help='Start of date diapason inclusively')
parser.add_argument('--finish-date', required=True, help='Finish of date diapason inclusively')
parser.add_argument('--date-format', required=True, help='Datetime format of the date in the file')
parser.add_argument('--arg-date-format', required=False, help='Datetime format of the dates in command line')

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