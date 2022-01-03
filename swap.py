def swap(list,pos1,pos2):
    list[pos1-1] = list[pos2-1]
    list[pos2-1] = list[pos1-1]
    return list
newList = swap([3,4,2,5,9,8],2,4)
print(newList)
