#!/bin/bash
echo "+================================================+";
echo "|---------------------ABOUT----------------------|";
echo "+================================================+";
echo "|---THIS TOOL HAS BEEN MADE BY PRANAV BHASKAR.---|"; 
echo "|--IF YOU ARE NOT HIM BETTER STAY AWAY FROM IT.--|";
echo "+================================================+";
echo "|---THIS TOOL WAS MADE FOR EDUCATIONAL PURPOSE---|";
echo "|ONLY AND IF MISSUSED IT IS NOT HIS RESPONSIBIITY|";
echo "+================================================+";
echo "";
echo "+================================================+";
echo "|--------------------CREDITS---------------------|";
echo "+================================================+";
echo "|------E-MAIL = [pranavbhaskar23@gmail.com]------|";
echo "+================================================+";
echo "|FB = [www.fb.com/profile.php?id=100006318544877]|";
echo "+================================================+";
echo "|--GITHUB = [https://github.com/Pranav-Bhaskar]--|";
echo "+================================================+";
echo "";
echo "+================================================+";
echo "|----------------IMPORTANT NOTE------------------|";
echo "+================================================+";
echo "|CHANGING THE CREDITS WILL NOT MAKE YOU THE CODER|";
echo "+================================================+";
echo "";
echo "Is this the FIRST TIME (Y/N) : ";
read varN
if [ $varN == 'Y' ] || [ $varN == 'y' ]
then
	echo "";
	echo "+================================================+";
	echo "|-------------Installing Python 2.X--------------|";
	echo "+================================================+";
	echo "";
	sudo apt install python2.7
	echo "";
	echo "+================================================+";
	echo "|-------------Installing Python 3.X--------------|";
	echo "+================================================+";
	echo "";
	sudo apt install python3
	echo "";
	echo "+================================================+";
	echo "|---------Installing required libraries----------|";
	echo "+================================================+";
	echo "";
	apt install python-mechanize
fi
echo "";
echo "+================================================+";
echo "|--------YOU CAN NOW BEGIN WITH THE HACK---------|";
echo "+================================================+";
echo "";
python3 make.py;
echo "+================================================+";
echo "|--------YOUR WORDLIST HAS BEEN CREATED----------|";
echo "+================================================+";
python2.7 fbcrack.py;
echo "+================================================+";
echo "|----------------HAPPY HACKING-------------------|";
echo "+================================================+";
