f=open("s",'w+')

b={}

for i in range(0,2):

    k=input("Enter the key:")

    v=int(input("Enter the value:"))

    b.update({k:v})

f.write("%s\r\n"%(b))

ch=input("Enter the ch:")

f.write("the ch is %s\r\n"%(ch))

if ch in b.keys():
 
    print(b[ch])

    f.write("the mark is %d"%(b[ch]))

f.close()