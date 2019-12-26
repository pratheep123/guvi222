alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit=['0','1','2','3','4','5','6','7','9','8']
sp=['!',"@",'#','$','%','^','&','*','(',')','~']
inp=input("Enter any alphabet or digit or special character:")
if inp in alpha:
  print("It is an alphabet")
elif inp in digit:
  print("It is a digit")
elif inp in sp:
  print("It is a Special Character")
