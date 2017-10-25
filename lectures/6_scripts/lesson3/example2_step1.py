#coding=utf-8
import shlex, subprocess

# читаем файл с командами
with open('example2.sh') as f:
	text = f.read()

# выведем его, чтобы проверить себя
print(text)

# будем использовать модуль shlex, чтобы разбить командную строчку на части (не всегда разбиение по пробелу это правильно)
for command_line in text.split('\n'):
	# посмотрим насколько разные ответы получатся
	print(command_line.split(' '))
	print(shlex.split(command_line))
	print()
