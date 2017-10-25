#coding=utf-8

from my_algo import analyze_sales

# Надо на каждый запуск писать новый код, хоть и немного
# Приходится открывать редактор, что-то дописывать, иногда это это лень делать
# хочется просто одну строчку написать в консоли написать и наслажаться результатом

analyze_sales(
	filename='sells3.csv',
	date_field='date',
	good_count_field='goods_number',
	total_money_field='total_money',
	start_date='2017.01.05',
	finish_date='2017.01.10',
	date_format='%d.%m.%Y',
	arg_date_format='%Y.%m.%d'
)

analyze_sales(
	filename='sells2.csv',
	date_field='date',
	good_count_field='goods_count',
	total_money_field='total_money',
	start_date='05.01.2017',
	finish_date='10.01.2017',
	date_format='%d.%m.%Y'
)

analyze_sales(
	filename='sells3.csv',
	date_field='date',
	good_count_field='goods_number',
	total_money_field='total_money',
	start_date='30.12.2016',
	finish_date='07.01.2017',
	date_format='%d.%m.%Y'
)

analyze_sales(
	filename='sells4.csv',
	date_field='date',
	good_count_field='goods_number',
	total_money_field='total_money',
	start_date='2016.30.12',
	finish_date='2017.07.01',
	date_format='%Y.%d.%m',
	arg_date_format='%Y.%d.%m'
)
