import os
import dbm
import shelve
import pickle

def print_file_content():
	file="C:\Program1.cs"
	fileobject=open(file)
	print(fileobject.read())
	fileobject.close()
	
def io_api():
	print (os.getcwd())
	print (os.curdir)
	print (os.path.abspath(os.curdir))
	print (os.path.abspath("."))
	for f in os.listdir(os.path.abspath(".")):
		print(f)
	print(os.path.exists("."))	
	print(os.path.exists("C:\\"))			
	
def testAnydbm():
	file=dbm.open("movie.txt","c");
	file["first"]="aaa"
	file.close()
	
def test_pickle():
	file=open("pickle.txt","wb")
	t=[1,2,3]
	pickle.dump(t,file)

def test_shelve():
	s=shelve.open("shelve.txt","cb");
	s["first"]="aaaaaaaaaaa"
	s.close()
	s=shelve.open("shelve.txt")
	print(len(s))
	print(s.keys())
	print(s['first'])
io_api()
testAnydbm()
test_pickle()
test_shelve()