#coding=utf-8

# импортируем специальную библиотеку
import pandas

# Глобальные константы обычно в верхнем регистре называют
FILENAME = 'sells3.csv'
DATE_FIELD = 'date'
GOODS_COUNT_FIELD = 'goods_number'
TOTAL_MONEY_FIELD = 'total_money'
START_DATE = '05.01.2017'
FINISH_DATE = '10.01.2017'

# теперь мы читаем файл с названием переменной FILENAME
df = pandas.read_csv(FILENAME)

def parse_date(raw_date):
	parts = list(map(int, raw_date.split('.')))
	return (parts[2], parts[1], parts[0])


df[DATE_FIELD] = list(map(parse_date, df[DATE_FIELD]))
df[GOODS_COUNT_FIELD] = list(map(int, df[GOODS_COUNT_FIELD]))
df[TOTAL_MONEY_FIELD] = list(map(int, df[TOTAL_MONEY_FIELD]))

# находим нужные нам дни
good_days = (df.date >= parse_date(START_DATE)) & (df.date <= parse_date(FINISH_DATE))

result_goods = df[good_days][GOODS_COUNT_FIELD].sum()
result_money = df[good_days][TOTAL_MONEY_FIELD].sum()
print('С {} по {} было куплено {} товаров на сумму {} рублей'.format(START_DATE, FINISH_DATE, result_goods, result_money))