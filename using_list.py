def insect(list1=[],list2=[]):
    result=[]
    for one in list1:
        if(one in list2):
            result.append(one)
    return result


list1=['a','b','h','c']
list2=['aaa','b','aafh','cccc']
for el in insect(list1,list2):
    print(el)

            
    
    