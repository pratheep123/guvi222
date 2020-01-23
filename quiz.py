p=0
def a(aa,bb):
  print(aa)
  print(bb)
a('1+2','a.1 b.2 c.3 d.4')
b=input("Enter the answer:")
if b=='c' or b=='3':
  print("Right answer")
  p+=1
else:
  print("wrong")
a('1+1','a.1 b.2 c.3 d.4')
b=input("Enter the answer:")
if b=='b' or b=='2':
  print("Right answer")
  p+=1
else:
  print("wrong")
a('1+3','a.1 b.2 c.3 d.4')
b=input("Enter the answer:")
if b=='d' or b=='4':
  print("Right answer") 
  p+=1
else:
  print("wrong")
print("points u got",p)   


