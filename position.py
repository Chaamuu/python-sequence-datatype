str1=input("enter any string")
i=int(input("enter position"))
str2=''
for j in range(len(str1)):
    if i!=j:
        str2=str2+str1[j]

print(str1)
print(str2)
print()


#check substring is present in given string
str1=input("enter any string")
sub=input("enter substring")
if sub in str1:
    print(f'{sub} is found')
else:
    print(f'{sub} is not found')



