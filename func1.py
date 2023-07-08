def func1(a,b):
    print(a,b)
def func2(a=0,b=0):
    print(a,b)
    
func1(10,20)
func1(100,200)
func2()
func2(100,200)
func2(b=900)

#function with return argument
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
def div(a,b):
    return a/b

r1=add(10,20)
r2=sub(10,5)
r3=multiply(90,8)
r4=div(5,2)
print(r1,r2,r3,r4)
