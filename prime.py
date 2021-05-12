import math
def main():
    flag = False
    value = int(input("Enter the value to check prime or not prime "))
    if value > 1:
        for i in range(2,value):
            if value%i==0:
                flag = True
                break
        if flag:
            print("Not Prime Number")
        else:
            print("Prime Number")
    
main()
        
