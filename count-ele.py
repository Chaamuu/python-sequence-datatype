list1=[10,20,304,40,292,44,3033,23,210,10,20,20,30,40,23,40]
set1=set(list1)
list2=[]
for value in set1:
    c=list1.count(value)
    if c>1:
        list2.append(value)
print(list1)
print(set1)
print(list2)
        
    
