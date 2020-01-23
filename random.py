import random
a=random.randint(0,11)
i=5
while (i>0):
    b=int(input())
    if a==b:
        break
    else:
        i=i-1
if(i>0):
    print("You won")
else:
    print("You lost")
