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

	for cmd in commands:
		# мы создаём на каждую команду отдельный процесс
		p = multiprocessing.Process(target=process_function, args=(cmd,))
		# и запускаем его
		p.start()
