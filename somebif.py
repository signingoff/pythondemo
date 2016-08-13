class A:
    pass

class B(A):
    pass

print('------issubclass-----')
print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,(A,B)))

a=A()
b=B()
print('------isinstance-----')
print(isinstance(a,A))#True
print(isinstance(a,B))#False
print(isinstance(b,A))#True
print(isinstance(b,B))#True

