Number = int(input(" Please Enter any Number: "))
i = 1
Sum = 0
while(i < Number):
    if(Number % i == 0):
        Sum = Sum + i
    i = i + 1
if (Sum == Number):
    print(Number,"  is a Perfect Number" )
else:
    print(Number," is not the Perfect Number")
