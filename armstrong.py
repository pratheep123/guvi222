number = int(input())
tot = 0
temp = number
while temp > 0:
    dig = temp % 10
    tot += dig ** 3
    temp=temp// 10
if number == tot:
    print(number,"is an Armstrong Number")
else:
    print(number,"is not an Armstrong number")
