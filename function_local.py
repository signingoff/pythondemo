def func(x):
    print(' value of x in func 1 is '+str(x))    
    x=x+1000
    print(' value of x in func 2 is '+str(x))    

x=10
print('value of x is '+str(x))
func(x)
print('value of x is '+str(x))