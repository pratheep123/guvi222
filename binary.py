a=[10,20,30,40,50]
b=10
f=0
l=len(a)-1
while f<=l:
    mid=f+(l-f)//2
    if b==a[mid]:
        print(mid)
        break
    elif b<a[mid]:
        l=mid-1
    elif b>a[mid]:
        f=mid+1
else:
    print("Not found")
    
        