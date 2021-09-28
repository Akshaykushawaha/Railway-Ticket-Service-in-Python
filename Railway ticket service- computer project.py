def info():
    print("\nTo get information about your ticket's waiting list:- \n 1.Just SMS your ticket no. to '95151' \n 2.You will get all the nesseccary details in 5-10 minutes via sms.\nTo print your ticket go to this site- WWW.printmyticket.com and enter your ticket number.")
    preflag()

def cncl():
    print("\nTo cancel your ticket go to this site- WWW.printmyticket.com and enter your ticket number and follow the procedure given.")
    preflag()

def tll():
    print("\nTo get a train's live location :- \n 1.SMS train PNR to 59152 \n 2.You will recieve the location of the train.")
    preflag()

def cc():
    print("\nTo connect to our customer care for further queries :- \n 1.Dial 59150 and your call will be connected to our customer care." )
    preflag()

def tr():
    import random
    a12=0
    while a12==0:
        a1=input("Do you want to save a copy of your Bill(s) as a record in Mysql Database?\n 1.If yes ,enter-1 \n 2.If no ,enter-2 \n Enter your choice here:- ")
        a2=input("Do you want to save a copy of your Bill(s) as a text document?\n 1.If yes ,enter-1 \n 2.If no ,enter-2 \n Enter your choice here:- ")
        if a1 not in ["1","2"] or a2 not in ["1","2"]:
            print("Enter a valid input")
        else:
            a12=1
    if a1=="1":
        print("Your bill(s) will be saved as a recrod in the database 'class12' and table 'tt_bill'")
        import mysql.connector
        abc = mysql.connector.connect(host='localhost', user='root', password='', port=3307)
        xyz=abc.cursor()
        xyz.execute("show databases")
        r = xyz.fetchall()
        if ('class12',) not in r:
            xyz.execute("create database class12")
        xyz.execute("use class12")
        xyz.execute("drop table if exists tt_bill ")
        xyz.execute("create table tt_bill(Departure varchar(20),Arrival varchar(20),Train varchar(20),Coach varchar(20),Seats integer(3),current_costing integer(8),Total_costing integer(8))")
    if a2=="1":
        print("Your bill(s) will be saved as a text document named as 'tts_bill'")
        f=open("tts_bill.txt","w")
        f.writelines("This is a copy of your Train Ticket Bill :D\n")
    cost=0
    flag13=1
    print("NOTE -------EMERGENCY BOOKING ONLY-------")        #same day train tickets only.
    flag3="yes"
    a=(".Delhi",".Bombay",".Goa",".Rajasthan",".Gujrat",".kolkata",".Bengaluru",".Chennai",".Kanyakumari",".Kerela",".Tamil Nadu",".Hyderabad",".Uttar Pradesh",".Assam",".Kashmir",".Sikkim",".Mizoram")
    cl=("Sleeper class","Sleeper class 2","A/C coach 1","A/C coach 2","A/C coach 3")
    t1=("Rajdhani","Duranto","Ajanta","Azad hind Express","Shatabdi express","Bombay Jayanti","Cold feild express","Forntier Express","Gangakaveri Express")
    while flag3!="no":
        sl1=random.randint(200,300)
        sl2=random.randint(200,300)
        ac1=random.randint(110,150)
        ac2=random.randint(10,99)
        ac3=random.randint(10,50)
        sl1cost=random.randint(100,200)
        sl2cost=random.randint(100,200)
        ac1cost=random.randint(200,350)
        ac2cost=random.randint(250,400)
        ac3cost=random.randint(300,500)
        csting=(sl1cost,sl2cost,ac1cost,ac2cost,ac3cost)
        flag4="yes"
        flag5="no"
        while flag5=="no":
            print("Enter the starting place for the journey from the given list")
            m=0
            for i in a:
                m+=1
                print(" ",m,i)
            p1=int(input("Enter your choice here:-" ))
            if 0<p1<18:
                flag5="yes"
                flag6="no"
                while flag6=="no":
                    print("Enter the ending place for the journey from the given list")
                    m=0
                    for i in a:
                        m+=1
                        if m!=p1:
                            print(" ",m,i)
                    p2=int(input("Enter your choice here:-" ))
                    if 0<p2<18:
                        if p1==p2:
                            print("Please enter a VALID input")
                        else:    
                            flag6="yes"
                    else:
                        flag6="no"
                        print("Please enter a VALID input")
                        
            else:
                flag5="no"
                print("Please enter a VALID input")
        flag7="no"
        while flag7=="no":
            print("Enter any one of the Trains from the following:-")
            m=0
            for i in t1:
                m+=1
                print(" ",m,i)
            t=int(input("Enter your choice here:-"))
            if 0<t<10:
                flag7="yes"
            else:
                print("Please enter a VALID input")
                flag7="no"
        while flag4=="yes":
            flag8="no"
            while flag8=="no":
                print("\nSelect the class from the following:-\n\nAvailable seats and cost per seat :-\n                  seats     costing\n 1.Sleeper class 1",sl1,"     Rs.",sl1cost,"\n 2.Sleeper class 2",sl2,"     Rs.",sl2cost,"\n 3.A/C coach 1    ",ac1,"     Rs.",ac1cost,"\n 4.A/C coach 2    ",ac2,"      Rs.",ac2cost,"\n 5.A/C coach 3    ",ac3,"      Rs.",ac3cost)
                c=int(input("Enter your choice here:- "))
                if 0<c<6:
                    flag8="yes"
                else:
                    flag8="no"
                    print("Please enter a VALID input")
            cst=0
            g=0
            sts=[sl1,sl2,ac1,ac2,ac3]
            print("\n\nAvailable seats in",t1[t-1],"'s"," ",cl[c-1],":-",sts[c-1])
            lp="no"
            while lp==("no"):   
                g=int(input("Enter the number of seats you need to book:- "))
                if g>sts[c-1]:
                    lp="no"
                    print("The number of seats selected exceed the availibility.\n\nselect the seats again")
                else:
                    lp="ok"
            if (c)==1:
                sl1-=g
                cost+=sl1cost*g
                cst=sl1cost*g
            elif (c)==2:
                sl2-=g
                cost+=sl2cost*g
                cst=sl2cost*g
            elif (c)==3:
                ac1-=g
                cost+=ac1cost*g
                cst=ac1cost*g
            elif (c)==4:
                ac2-=g
                cost+=ac2cost*g
                cst=ac2cost*g
            elif (c)==5:
                ac3-=g
                cost+=ac3cost*g
                cst=ac3cost*g
            print("\nBill for the current seat reservation: ")
            print("\nYour starting Destination--->",a[p1-1],"\nYour ending Destination----->",a[p2-1],"\nTrain name--->",t1[t-1],"\nClass of your Seat-->",cl[c-1],"\nNo. of seats billed:-",g,"\nYour current costing-->",cst,"(",csting[c-1],"*",g,")")
            print("\nAvailable seats :-\n 1.Sleeper class 1",sl1,"\n 2.Sleeper class 2",sl2,"\n 3.A/C coach 1    ",ac1,"\n 4.A/C coach 2    ",ac2,"\n 5.A/C coach 3    ",ac3)
            val=(a[p1-1],a[p2-1],t1[t-1],cl[c-1],g,cst,cost)
            if a1=="1":
                xyz.execute("insert into tt_bill values(%s,%s,%s,%s,%s,%s,%s)",val)
            if a2=="1":
                f.writelines("\nYour Bill no."+str(flag13))
                f.writelines("\n\nYour starting Destination---> "+a[p1-1]+"\nYour ending Destination-----> "+a[p2-1]+"\nTrain name---> "+t1[t-1]+"\nClass of your Seat--> "+str(cl[c-1])+"\nNo. of seats billed:- "+str(g)+"\nYour current costing--> "+str(cst)+"("+str(csting[c-1])+"*"+str(g)+")\n")
            flag9="no"
            while flag9=="no":
                flag11=int(input("Do you want to book any more seats ? \n 1.If yes ,enter-1 \n 2.If no ,enter-2 \n Enter your choice here:- "))
                if flag11==1:
                    flag9="yes"
                    flag10="no"
                    flag13+=1
                    while flag10=="no":
                        flag12=int(input("Do you want to book this ticket for the same train ? \n 1.If yes ,enter-1 \n 2.If no ,enter-2 \n Enter your choice here:- "))
                        if flag12==1:
                            flag4="yes" 
                            flag10="yes"
                        elif flag12==2:
                            flag10="yes"
                            flag4="no"
                        else:
                            print("Enter a valid input")
                elif flag11==2:
                    print("\nYour ticket request has been applied.\n\n***PLEASE CHECK THE WAITING LIST REGULARLY***")
                    print("\nYou will be redirected to Banking webpage for online payment (only online payment possible currently)")
                    flag3="no"
                    flag9="yes"
                    flag4="no"
                else:
                    print("Enter a valid input")
    print("Your total costing-----> Rs.",cost)
    print("\nThankyou for using Railway ticket service online portal!!!")
    preflag()
    print("\n-----Redirecting for Banking-----")
    if a2=="1":
        f.writelines("\n\nYour Total amount is: "+str(cost)+"\nYour ticket request has been applied.\n\n***PLEASE CHECK THE WAITING LIST REGULARLY***")
        f.writelines("\n\nThankyou for using Railway ticket service online portal!!!")
        f.close()
        do=input("A copy of your Bill has been saved as a text file.Do you want to read it?\n(y/n): ")
        if do=="y":
            f=open("tts_bill.txt","r")
            print("The file is:\n",f.read())
            f.close()
            
            
def ckflag(flag):
    if flag==1:
        funsel(0)
    if flag==2:
        print("\n ***Thankyou for using the Railway ticket service online portal***")
    if flag not in [1,2]:
        flag=int(input("-------->Please enter a VALID input \n Do you want any other help ? \n 1.If yes ,enter-1 \n 2.If no ,enter-2 \n Enter your choice here:- "))
        ckflag(flag)

def funsel(z):
    if z==1:
        tr()
    elif z==2:
        info()
    elif z==3:
        cncl()
    elif z==4:
        tll()
    elif z==5:
        cc()
    elif z==0:
        z=int(input("Please select a suitable option:- \n 1.Book Train Tickets \n 2.Enquire about your ticket \n 3.Get your ticket printed \n 4.Track a Train's live location \n 5.For Further queries you can also connect to our coustomer care \n\nEnter your option here:- "))
        funsel(z)
    if z not in [1,2,3,4,5]:
        print("Please enter a valid input")
        funsel(0)

def preflag():
    flag=int(input("\nDo you want any other help ? \n 1.If yes ,enter-1 \n 2.If no ,enter-2 \n Enter your choice here:- " ))
    ckflag(flag)
        
        
print("Welocme to Railway ticket service online portal\n  created by -Akshay Kushawaha \n                 class XII-Science ")
funsel(0)