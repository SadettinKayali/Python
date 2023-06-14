"""
for i in dir(tuple()):
    if "__" not in i:
        print(i)
        
count
index

"""
demet= ("deneme1","deneme2","deneme2","sadettin","sadettin","sadettin","sadettin","sadettin")
count=demet.count("sadettin")
index=demet.index("sadettin")
print(count)
print(index)