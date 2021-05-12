import requests
from pprint import pprint
def main():
    res = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = res.json()
    pprint(data)

main()
