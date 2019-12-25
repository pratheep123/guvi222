a=int(input("Enter the number:"))
b=a
rev=0
while a>0:
    rev=(rev*10)+(a%10)
    a=a//10
if (b==rev):
    print("the number is palindrome")
       
else:
    print("not palindrome")
        
        
       
       
    
