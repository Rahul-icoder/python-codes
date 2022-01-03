arr = [3,25,6,72,4]
counter = 0;
while counter < len(arr):
    small = arr[counter]
    for i in range(counter,len(arr)):
        if small>arr[i]:
            small = arr[i]
    print(small)
    arr[counter]=small
    counter+=1
print(arr)
        
