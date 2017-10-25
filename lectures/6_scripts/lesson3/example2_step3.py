#coding=utf-8
import shlex, subprocess

# читаем файл с командами
# на windows не работает с example2.sh, так как ">" не поддерживается 
with open('example2_simple.sh') as f:
	text = f.read()

# будем использовать модуль shlex, чтобы разбить командную строчку на части (не всегда разбиение по пробелу это правильно)
for command_line in text.split('\n'):
	args = shlex.split(command_line) 
	print(args)
	with subprocess.Popen(args, stdout=subprocess.PIPE) as proc:
		response = proc.stdout.read()
		if args[0] == 'ls':
			# к сожалению просто так сразу получить нужную строчку не получится нужно сделать преобразования
			print(str(response))
			print()
			# удалим b и кавычки
			print(str(response)[2:-1])
			print()
			# а остаток разделим по \\n, два слеша так как \n - это перевод строки а нам нужно именно \n как два символа
			print(str(response)[2:-1].split('\\n'))
			print()
			print()
