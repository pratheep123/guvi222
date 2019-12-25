a=3465878
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
b=3
c=8
def sum(d,e):
    if d==3:
        if e==8:
            sum=d+e
            print("the sum of first and last digit is:",sum)
sum(b,c)


    
