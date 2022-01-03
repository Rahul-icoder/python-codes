import random
n = 1
def main():
    print("welcome to the world of python quesing ")
    storeValue = random.randrange(1, 1000, 2);
    

    def isResultFun(value,storeValue):
        if value==storeValue:
            return True
        elif value < storeValue:
            print("your value is low")
        elif value > storeValue:
            print("your value is high")
    
    while(n<=10):
        value = int(input("hint: Enter the value in range 0 and 1000 "))
        isresult = isResultFun(value,storeValue)
        if isresult:
            print(f"you won game in {n} chance")
            break
        n+=1
main()
if(n>10):
    print("you lose")
