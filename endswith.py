namesList=["naresh",
            "nagehs",
            "ramesh",
            "radhika",
            "rigita"]
            
for name in namesList:
    if name.endswith("a"):
        print(name)
print()

for name in namesList:
    if name.endswith(("a","s")):
        print(name)
