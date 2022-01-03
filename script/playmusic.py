import random
import os
path = 'D:\Emotional Miser\\'
os.chdir(path)
music_list = os.listdir(os.getcwd())
file_name = random.choice(music_list)
print(file_name)
os.startfile(path + file_name)
print('enjoy!')
