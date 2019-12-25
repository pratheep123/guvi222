a=int(input("Enter the number:"))
c=0
for i in range(2,a-1):
    if (a%i==0):
        print(i)
        i+=1
        c+=1
if c==0:
    print(a,"is a prime number")

