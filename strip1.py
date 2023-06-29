s1="  nit"
s2="nit"
s1==s2
s3=s1.strip()
print(s3)
print(s1)
print(s2)
s4="*****nit****"
print(s4)
s6="www.puter.com"
s7=s6.strip("w.com")
print(s7)

#nameslist
namesList=["naresh",
            "nagehs",
            "ramesh",
            "radhika",
            "rigita"]
for name in namesList:
    if name.startswith("r"):
        print(name)
print()
for name in namesList:
    if name.startswith(("n","r")):
        print(name)
            
