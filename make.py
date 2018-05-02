#!/usr/bin/python

import os
import itertools
import math
from random import randint

tmp_dir = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file_name = 'temp.PASSWD'

def permu(n,r):
	fac = math.factorial
	com = fac(n)/(fac(n-r))
	return com
	
def make(l,minlen):
	f = []
	for x in range(1,len(l)+1):
		f = f + list(itertools.permutations(l,r=x))
	t = []
	for x in range(len(f)):
		if len(''.join(f[x])) >= minlen :
			t.append(''.join(f[x]))
	print('Writing on File')
	if not os.path.exists(tmp_dir):
		os.makedirs(tmp_dir)
	file_path = "{}/{}".format(tmp_dir, file_name)
	f = open(file_path, 'w')
	for x in t:
		f.write(x)
		f.write('\n')
	f.close()
	
def makecase(l,minlen):
	f = []
	for x in range(1,len(l)+1):
		f = f + list(itertools.permutations(l,r=x))
	t = []
	for x in range(len(f)):
		if len(''.join(f[x])) >= minlen :
			t.append(''.join(f[x]))
	print('Writing on File')
	if not os.path.exists(tmp_dir):
		os.makedirs(tmp_dir)
	file_path = "{}/{}".format(tmp_dir, file_name)
	f = open(file_path, 'w')
	z = set()
	for x in t:
		z.update(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in x))))
	t = list(z)
	t.sort()
	t.sort(key=len)
	for x in t:
			f.write(x)
			f.write('\n')
	f.close()
	
def calc(l):
	t = 0 
	num = 0
	temp = 1
	comb = 0
	fac = math.factorial
	for x in range(len(l)):
		comb += permu(len(l),x+1)
	for x in range(len(l)-1):
		num += permu(len(l)-1,x+1)
	for x in l:
		t += len(x)*(comb-num)
	t += comb1
	print('Total Number of Combinations : '+str(comb))
	print('Size in bytes     : '+str(t//temp))
	temp = 1024*temp
	print('Size in megabites : '+str(t//temp))
	temp = 1024*temp
	print('Size in gigabites : '+str(t//temp))
	temp = 1024*temp
	print('Size in terabites : '+str(t//temp))
	temp = 1024*temp
	print('Size in petabites : '+str(t//temp))
	
def calcase(l):
	t = 0 
	num = 0
	temp = 1
	comb = 0
	alph = 0;
	fac = math.factorial
	for x in range(len(l)):
		comb += permu(len(l),x+1)
	for x in l:
		for y in x:
			alph += 1
	comb *= (2**alph)
	#for x in range(len(l)-1):
	#	num += combi(len(l)-1,x+1) * fac(x+1)
	#for x in l:
	#	t += len(x)*(comb-num)
	#t += comb1
	print('Total Number of Combinations : '+str(comb))
	print('Size in bytes     : '+str(t//temp))
	temp = 1024*temp
	print('Size in megabites : '+str(t//temp))
	temp = 1024*temp
	print('Size in gigabites : '+str(t//temp))
	temp = 1024*temp
	print('Size in terabites : '+str(t//temp))
	temp = 1024*temp
	print('Size in petabites : '+str(t//temp))
	
def opt(l):
	code = randint(10000,100000)
	minlen = int(input('Enter the minimum length of a password : '))
	ch = input('Is the password cAsEsEnSeTiVe (qwerty!=QWERTY) (Y/N) : ')
	if (ch=='y'or ch=='Y'):
		#calcase(l)
				
	else:
		calc(l)
		
	num = int(input('Are you sure you want to Proceed. If YES enter the number '+str(code)+' : '))
	if(num == code)and(ch=='y'or ch=='Y'):
		print('Please Wait Preparing Data')
		makecase(l,minlen)
		print('Done')
	elif(num == code):
		print('Please Wait Preparing Data')
		make(l,minlen)
		print('Done')
l=list(input("Enter the words with ';' in between : ").strip().split(';'))
print('You Gave '+str(len(l))+' number of words.')
opt(l)
