#coding=utf-8

from my_algo import analyze_sales
import argparse
# используем json для config (помните, что это такое?)
import json

# глобальные комментарии по скрипту
parser = argparse.ArgumentParser(description='the script reads file and calcs total money and total goods in the given date diapason')

# Теперь нам нужно сделать все аргументы необязательными, но в конце добавить возможность передать config
parser.add_argument('-f', '--filename', required=False, help='Path to file with data')
parser.add_argument('--date-field', required=False, help='A name of the field containing date. Usually it is "date"')
parser.add_argument('--good-count-field', required=False, help='A name of the field containing goods  count. Usually it is "good_count"')
parser.add_argument('--total-money-field', required=False, help='A name of the field containing total money. Usually it is "total_money"')
parser.add_argument('--start-date', required=False, help='Start of date diapason inclusively')
parser.add_argument('--finish-date', required=False, help='Finish of date diapason inclusively')
parser.add_argument('--date-format', required=False, help='Datetime format of the date in the file')
parser.add_argument('--arg-date-format', required=False, help='Datetime format of the dates in command line')

parser.add_argument('--config', required=False, help='path to config json with all aparameters defined above')

args = parser.parse_args()

# Но теперь у нас вновь появилась проблема, что нас могут запустить с некорректным множеством аргументов, а мы об этом не скажем.
# Поэтому нужно вручную это проверить
cmd_arguments = {
	k: v
	for k, v in vars(args).items()
	if v is not None
}

if args.config is None:
	for arg_name in ['filename', 'date_field', 'good_count_field', 'total_money_field', 'start_date', 'finish_date', 'date_format']:
		if cmd_arguments.get(arg_name) is None:
			parser.error("config is not provided and {} is missing".format(arg_name))
else:
	# читаем json
	with open(args.config, 'r') as f:
		arguments = json.load(f)

	# У параметров командной строке будет приоритет по значения
	arguments.update(cmd_arguments)
	cmd_arguments = arguments

analyze_sales(
	filename=cmd_arguments.get('filename'), 
	date_field=cmd_arguments.get('date_field'), 
	good_count_field=cmd_arguments.get('good_count_field'), 
	total_money_field=cmd_arguments.get('total_money_field'),
	start_date=cmd_arguments.get('start_date'),
	finish_date=cmd_arguments.get('finish_date'), 
	date_format=cmd_arguments.get('date_format'),
	arg_date_format=cmd_arguments.get('arg_date_format')
)