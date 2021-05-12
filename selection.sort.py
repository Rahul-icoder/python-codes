arr = [3,25,6,72,4]
counter = 0;
while counter < len(arr):
    small = counter
    for i in range(counter+1,len(arr)):
        if arr[small]>arr[i]:
            small = i
    temp = arr[counter]
    arr[counter]=arr[small]
    arr[small]=temp
    counter+=1
print(arr)
        
