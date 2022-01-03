mood = input("Enter you ): for happy emoji and (: sad emoji ")
dic = {
	'(:' : '😞',
	'):' : '😊'
}

l = mood.split()
print(l)
for val in l:
	if val == 