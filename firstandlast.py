a=int(input("Enter the digit:"))
def first(b):
    while b>10:
        b=b//10
    print("the firstdigit is:",b)
first(a)
def last(c):
    while c>10:
        c=c%10
    print("the lastdigit is:",c)
last(a)

