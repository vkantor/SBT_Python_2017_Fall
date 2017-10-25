#coding=utf-8

# импортируем специальную библиотеку
import pandas

# теперь мы можем считать файл одной строчкой
df = pandas.read_csv('sells2.csv')

# Вопрос на засыпку. Чем такой способ хуже предыдущего?
# Ответ: тем, что теперь мы весь файл считываем в память, а раньше по одной строчке читали

# Но распарсить каждое поле нам всё равно нужно
def parse_date(raw_date):
	parts = list(map(int, raw_date.split('.')))
	return (parts[2], parts[1], parts[0])


df.date = list(map(parse_date, df.date))
df.goods_count = list(map(int, df.goods_count))
df.total_money = list(map(int, df.total_money))

# Посмотрим, что в итоге получилось
print(df)