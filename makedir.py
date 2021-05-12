import os
def main():
    current_path = os.getcwd()
    dir = "modules"
    try:
        path = os.path.join(current_path,dir)
        os.makedirs(path)
        print('New folder created')
    except:
        print('folder already exits')

main()
