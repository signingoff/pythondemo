def testtuple():
    tuple = ('a','b','4','aa',56,'hg','p','000')
    print('the first element is ' + str(tuple[0]))
    print('the length of tuple is ' + str(len(tuple[0])))
    tupletwo=('c','d',tuple)
    print('the tupletwo[2][1] element is ' + str(tupletwo[2][1]))
    print(tuple[2:4])
    print(tuple[2:4:2])
    print(tuple[2:4:-2])
    print(tuple[2:-1])
testtuple()
    