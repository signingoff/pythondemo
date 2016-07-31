import os

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
	
io_api()