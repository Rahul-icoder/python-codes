def duplicate(list):
    # return duplicate item
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if(list[i]==list[j]):
            	print(list[j])


duplicate([4,3,4,8,2,3,4]);
