def makeexpression(n):
    return lambda s,t,z:  str(n * 2) + s + t + z

print('make expression %d',makeexpression(100)('a','b','c'))