ls # example1.sh  good_json.json  lesson_text.txt  my_algo.py  my_command.py 
echo "Hello wordl!" > tmpfile
ls # example1.sh     lesson_text.txt  my_command.py good_json.json  my_algo.py tmpfile
cd ..
ls # lesson1  lesson2  lesson3
cp ./lesson2/good_json.json ./lesson3/
ls lesson3 # example1.sh     lesson_text.txt  my_command.py good_json.json  my_algo.py tmpfile
rm lesson3/good_json.json
ls lesson3 # example1.sh     lesson_text.txt  my_command.py my_algo.py tmpfile
mv ./lesson3/tmpfile ./
ls # lesson1  lesson2  lesson3  tmpfile
rm tmpfile
ls # lesson1  lesson2  lesson3
mkdir tmpdir
ls # lesson1  lesson2  lesson3  tmpdir
cd tmpdir
echo "Hello wordl!" > tmpfile
ls # tmpfile
cd ..
ls # lesson1  lesson2  lesson3  tmpdir
rm -r tmpdir
ls # lesson1  lesson2  lesson3