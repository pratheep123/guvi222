a=36578
def first(b):
    while (b>10):
          b=b//10
    print("the firstdigit is:",b)
first(a)
def last(c):
    while (c>10):
          c=c%10
    print("The lastdigit is:",c)
last(a)
b=3
c=8
def swap(d,e):
    temp=d
    d=e
    e=temp
    print("after swapping:")
    print("first digit is:",d,"the lastdigit is:",e)
swap(b,c)
