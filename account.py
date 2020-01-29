f=open("account.txt","w+")

import random

accid={}

d=0

while d<4:

    print(("Enter the r to register or s to signup or q to quit"))

    inp=input("Enter the string:")

    if inp=="r":

        def register():

            if inp=="r":

                name=input("Enter the name:")

                f.write("the name is %s\r\n"%(name))

                emailid=input("Enter the mailid:")

                f.write("The mailid is %s\r\n"%(emailid))

                l1=len(emailid)

                while l1>10:

                    if "@gmail.com" in emailid:

                        f.write("valid mailid\r\n")

                        l=list(range(1000,9999))

                        random.choice(l)

                        l.pop()

                        a=[]

                        pwd=input("Enter the pwd:")

                        f.write("the pwd is %s\r\n"%(pwd))

                        accid.update({emailid:pwd})

                        f.write("Registration is successful\r\n")

                        break

                    else:

                        f.write("invalid mailid\r\n")

                        f.write("Registration is unsuccessful\r\n")

                        break
        register()

    d+=1

    if inp=="s":

        def signup():

            c=0

            while c<3:

                emailid=input("Enter the mailid:")

                f.write("the mailid is %s"%(emailid))

                if emailid in accid.keys():

                    pwd=input("Enter the pwd")

                    f.write("the pwd is %s"%(pwd))

                    if pwd in accid.values():

                        f.write("Login successful")

                        break

                    else:

                        f.write("Invalid pwd")

                        c+=1

                else:

                    f.write("Enter valid mailid")

                    c+=1

            bal=15000

            cwd=input("1.checkbalance 2.deposit 3.withdrawl")

            f.write("The option is %s\r\n"%(cwd))

            if cwd=="1" or cwd=="checkbalance":

                f.write("the balance is %d\r\n"%(bal))

            elif cwd=="2" or cwd=="depposit":

                deposit=int(input("Enter the money:"))

                bal+=depposit

                f.write("The balance is %d\r\n"%(bal))

            elif cwd=="3" or cwd=="withdrawl":

                withdrawl=int(input("Enter the money:"))

                bal-=withdrawl

                f.write("the balance is %d\r\n"%(bal))

                if bal<10000:

                    f.write("your accont has minimum balance\r\n")

        signup()

    d+=1

    if inp=="q":

        f.write("quit")
                
            
        
    
    

    
    
    
    
    


