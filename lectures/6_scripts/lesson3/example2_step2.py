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
	# заспускаем подпроцесс с командой
	proc = subprocess.Popen(args, stdout=subprocess.PIPE)
	# ждём завершения 
	proc.wait()
	print(proc.stdout.read())


	# иногда удобнее писать так (как с файлами) 
	# with subprocess.Popen(args, stdout=subprocess.PIPE) as proc:
	#	print(proc.stdout.read())