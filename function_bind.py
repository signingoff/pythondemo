class MyClass:
	def printmessage():
		print('this is class method')
	def printmessage2(self,msg):
		print('this is class method',msg)
	
MyClass.printmessage();		
print(MyClass.__dict__)
mc=MyClass()
print(mc.__dict__)
mc.printmessage2('argument')
print(mc.__dict__)
