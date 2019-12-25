a=int(input("Enter the digits:"))
sum=0
while (a>0):
    remainder=a%10
    a=a//10
    sum=sum+remainder
print("The sum of a:",sum)
