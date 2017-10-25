#coding=utf-8
import shlex, subprocess

# создаём код
my_script = """
ls
echo "Hello wordl!" > tmpfile
ls
cp ../lesson2/good_json.json ./
ls
rm good_json.json
ls
mv ./tmpfile ../
ls ../
rm ../tmpfile
ls ../
mkdir ../tmpdir
ls ../
rm -r ../tmpdir
ls
"""
with open('example3.sh', 'w') as f:
	f.write(my_script)

args = shlex.split('sh example3.sh') 
with subprocess.Popen(args, stdout=subprocess.PIPE) as proc:
	print(proc.stdout.read().decode('windows-1251'))
