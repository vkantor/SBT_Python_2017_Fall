#coding=utf-8
import subprocess
import multiprocessing

# каждый процесс будет выполнять
def process_function(command):
	subprocess.call(command)


# раз уж теперь у нас будет много процессов, нужно пометить главный процесс
# это делается вот так:
if __name__ == '__main__':
	commands = [
		'python my_command.py --config config1.json',
		'python my_command.py --config config2.json',
		'python my_command.py --config config3.json',
		'python my_command.py --config config4.json'
	]


	# Сделаем максимум 10 процессов
	pool = multiprocessing.Pool(processes=10)
	# нам нужно параллельно применить нашу функцию к различным аргументам
	# в нашем случае это список строчек commands * 100
	pool.map(process_function, commands * 100)
