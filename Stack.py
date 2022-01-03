list = [];
count = 0;

def pop():
    return list[count-1];
    

def peek():
	if(list == None):
		 return 'not found'
    return list[count-1]

def size():
    return count-1;

def push(value):
    list[count] = value;
    count += 1;

# push("rahul");
print(peek());
print(size());
