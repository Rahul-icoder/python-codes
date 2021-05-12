def elemExits(list,elem):
    for item in list:
        if elem in item:
            return "match "+elem
out = elemExits(["rahul","pea","1",3],"pea")
print(out)
    
