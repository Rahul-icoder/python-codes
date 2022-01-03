# interchange first and last of element in list

def interchange(interlist):
    if len(interlist) == 0:
        print("Empty list")
        return
    lastelem = interlist[len(interlist)-1]
    firstelem = interlist[0]
    interlist[0] = lastelem
    interlist[len(interlist)-1] = firstelem
    return interlist

newList = interchange(["a","b","c","d","e"])
print(newList)
