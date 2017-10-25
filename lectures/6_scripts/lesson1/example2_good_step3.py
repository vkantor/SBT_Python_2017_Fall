#coding=utf-8

# импортируем специальную библиотеку
import pandas

df = pandas.read_csv('sells1.csv')

def parse_date(raw_date):
	parts = list(map(int, raw_date.split('.')))
	return (parts[2], parts[1], parts[0])


df.date = list(map(parse_date, df.date))
df.goods_count = list(map(int, df.goods_count))
df.total_money = list(map(int, df.total_money))

# находим нужные нам дни
good_days = (df.date >= (2017, 1, 5)) & (df.date <= (2017, 1, 10))

result_goods = df[good_days].goods_count.sum()
result_money = df[good_days].total_money.sum()
print('С 2017.01.05 по 2017.01.10 было куплено {} товаров на сумму {} рублей'.format(result_goods, result_money))