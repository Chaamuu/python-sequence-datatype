course=["java","python","jpython","jupyter"]
for name in course:
    print(name.center(20))
print()

course=["java","python","ruby","datasciencs"]
for name in course:
    print(name.rjust(20))
print()

course=["java","python","jupyter","jython"]
for name in course:
    print(name.ljust(20))

course=["python","java","data","c++"]
for name in course:
    print(name.rjust(20,"*"))
print()

course=["python","java","data","c++"]
for name in course:
    print(name.ljust(20,"*"))
print()

course=["java","python","jpython","jupyter"]
for name in course:
    print(name.center(20,"*"))
print()

student=[("java","python"),("data","c++"),("jython","jupyter")]
for stud in student:
    print(stud[0].center(20,"*"),stud[1].rjust(20,"$"))
