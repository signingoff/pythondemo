def range_test():
	array=[1,2]
	print(len(array))
	print(range(len(array)))
	for index in range(len(array)):
		print(array[index])
		
	print(range(3))
	for index in range(3):
		print(index)	
		
	print(range(1,6,2))
	for index in range(1,6,2):
		print(index)
		
	print(range(1,6,-2))
	for index in range(1,6,-2):
		print(index)
	
range_test()