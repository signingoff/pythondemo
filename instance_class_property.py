class Person:
	count=0
	
a1=Person()	
b1=Person()
c1=Person()

print('a1.count ',a1.count)
print('b1.count ',b1.count)
print('c1.count ',c1.count)

a1.count=a1.count+1

print('a1.count ',a1.count)
print('b1.count ',b1.count)
print('c1.count ',c1.count)

Person.count=99

print('a1.count ',a1.count)
print('b1.count ',b1.count)
print('c1.count ',c1.count)
print('Person.count ',Person.count)

