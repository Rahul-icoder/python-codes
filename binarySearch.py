def find(list,target):
    for index in range(0,len(list)):
        if(list[index]==target):
            return index;
    else:    
        return "None";


list = [3,4,1,3,5,6];

get = find(list,3);
if(get is not "none"):
    print("Item Found on index ",get);
else:
    print("Item Not Found ");
