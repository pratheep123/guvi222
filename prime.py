a=int(input("enter the number:"))
if a>1:
    for i in range(2,a):
        if (a%2)==0:
            print(a,"it is not prime number")
            break
        else:
            print(a,"is prime number")
            break
            
else:
    print("it is not prime number")
