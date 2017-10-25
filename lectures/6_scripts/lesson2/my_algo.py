#coding=utf-8

# импортируем специальную библиотеку
import pandas
# в питоне есть специальная библиотека для работы с датами
import datetime

# Мы создаём функцию, в которой принимаем все нуные нам параметры и выполняем старые действия, используя их
def analyze_sales(filename, date_field, good_count_field, total_money_field, start_date, finish_date, date_format, arg_date_format=None):
	# Теперь есть дополнительный параметр - формат даты в аргументах
	# если он не передан, то считаем, что такой же, как в файле
	if arg_date_format is None:
		arg_date_format = date_format

	df = pandas.read_csv(filename)

	def parse_date(raw_date, format=date_format):
		return datetime.datetime.strptime(raw_date, format)

	df[date_field] = list(map(parse_date, df[date_field]))
	df[good_count_field] = list(map(int, df[good_count_field]))
	df[total_money_field] = list(map(int, df[total_money_field]))

	# находим нужные нам дни
	good_days = (df.date >= parse_date(start_date, arg_date_format)) & (df.date <= parse_date(finish_date, arg_date_format))

	result_goods = df[good_days][good_count_field].sum()
	result_money = df[good_days][total_money_field].sum()
	print('С {} по {} было куплено {} товаров на сумму {} рублей'.format(start_date, finish_date, result_goods, result_money))
