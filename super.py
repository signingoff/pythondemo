class Parent(object):
	def showMessage(self,message):
		print(message+" in Parent")
		
class Child(Parent):
	def showMessage(self,message):
		super(Child,self).showMessage(message)
		print(message+" in Child")
		
	def showSelfType(message):
		print(type(message))
		
Child().showMessage("hello world")		
Child().showSelfType()		