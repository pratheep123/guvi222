a=input("Enter a string:")
b=len(a)
q=b*2
print("the length is ",b)
i=0
j=0
k=0
z=0
while j<b*2:
  if z==b:
    print("congratulation")
    break
  c=input("try a character:")
  while i<b:
    if c==a[i]:
      print("character present in",i+1)
      i+=1
      z+=1
    else:
      if i==b-1:
        if i==k:
          print("the character is not present")
          q=q-1
          print("chances remaining:",q)
      i+=1
      k+=1
  i=0
  k=0
  j+=1
if z!=b:
  print("you are hanged")



