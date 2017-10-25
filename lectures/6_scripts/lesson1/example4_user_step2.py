#coding=utf-8

# теперь нам нужно просто импортировать наш скрипт
from example4_algo_step2 import analyze_sales

#  можем использовать на своё усмотрение и не один раз
analyze_sales(
	filename='sells3.csv',
	date_field='date',
	good_count_field='goods_number',
	total_money_field='total_money',
	start_date='05.01.2017',
	finish_date='10.01.2017',
	date_format='%d.%m.%Y'
)

# другой файл
analyze_sales(
	filename='sells2.csv',
	date_field='date',
	good_count_field='goods_count', # там другое название надо это укзаать
	total_money_field='total_money',
	start_date='05.01.2017',
	finish_date='10.01.2017',
	date_format='%d.%m.%Y'
)

# другие даты
analyze_sales(
	filename='sells3.csv',
	date_field='date',
	good_count_field='goods_number',
	total_money_field='total_money',
	start_date='30.12.2016',
	finish_date='07.01.2017',
	date_format='%d.%m.%Y'
)

# другой формат даты
analyze_sales(
	filename='sells4.csv',
	date_field='date',
	good_count_field='goods_number',
	total_money_field='total_money',
	start_date='2016.30.12',
	finish_date='2017.07.01',
	date_format='%Y.%d.%m'
)
