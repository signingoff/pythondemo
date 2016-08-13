class mystr_repr:
    def __str__(self):
        return 'this method is like ToString()?'
    
    def __repr__(self):
        return 'this method is __repr__'


e=mystr_repr();
print(e)
print(str(e))
print(repr(e))