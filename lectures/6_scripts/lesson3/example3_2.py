#coding=utf-8
import shlex, subprocess

# создаём код
my_script = """
python my_command.py --config config1.json
python my_command.py --config config2.json
python my_command.py --config config3.json
python my_command.py --config config4.json
"""
with open('example3.sh', 'w') as f:
	f.write(my_script)

args = shlex.split('sh example3.sh') 
with subprocess.Popen(args, stdout=subprocess.PIPE) as proc:
	print(proc.stdout.read().decode('windows-1251'))
