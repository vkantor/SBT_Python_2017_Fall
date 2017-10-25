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

# В таком случае, если нам не нужно получать ответ от запуска команды (например, если она сама всё выведет),
# мы можем просто воспользовать функцией call в модулей subprocess
subprocess.call('sh example3.sh')
