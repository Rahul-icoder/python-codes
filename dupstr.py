str = "anacnna"
	
i=0
dupstr = ""
for s in str:
	if str.index(s)==i:
		dupstr+=s
	i+=1
print(dupstr)