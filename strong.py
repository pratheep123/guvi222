Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    Reminder = Temp % 10

    for i in range(1, Reminder + 1):
        Factorial = Factorial * i

    print("Factorial of " ,(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("Sum of Factorials of a Given Number" ,(Number, Sum))
    
if (Sum == Number):
    print(Number,"is a Strong Number")
else:
    print(Number,"is not a Strong Number")
