import requests
import math
import sys
try:
    url = sys.argv[1]
    file_arr = url.split('/')
    file_name = file_arr[len(file_arr)-1]
    chunk_size = 1024*64
    res = requests.get(url,stream=True)
    total_size = int(res.headers['Content-Length'])
    n = math.ceil(total_size/chunk_size)
    with open(file_name,'wb') as file:
        for chunk in res.iter_content(chunk_size=chunk_size):
            file.write(chunk)
    print('download finished')
except:
    print('donwload failed please provide working link')
