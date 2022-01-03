import os
path = 'E:/python/modules/'
list = os.listdir(path)
i=1
for file in list:
    print(file)
    os.rename(path+file,path+"file"+str(i)+".jpg")
    i+=1

print('rename succesfull')
