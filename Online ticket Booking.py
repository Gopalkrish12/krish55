import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="ticketbooking"

)
mycursor=mydb.cursor()
print(">>>>>>>>>>>>>>>>Online Movie Tickect Booking<<<<<<<<<<<<<<<<<<<<<<<<<")
print("1.Book Your Tickets")
print("2.View Details")
print("3.Update the Ticket")
print("4.Cancel the Ticket")
def insert_data(Name,Mobile_No,Movie_Name,Timing,No_of_Person,Class,Total_amount):
    sql="insert into booking (Name,Mobile_No,Movie_Name,Timing,No_of_Person,Class,Total_amount)values(%s,%s,%s,%s,%s,%s,%s)"
    val=(Name,Mobile_No,Movie_Name,Timing,No_of_Person,Class,Total_amount)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f"{Movie_Name},is Booked \nShow Time is {Timing}")
def view_data():
    mycursor.execute("select * from booking")
    result=mycursor.fetchall()
    for i in result:
        print(i)
def update(Name,Mobile_No):
    if choose==1:
        mycursor=mydb.cursor()
        sql="update booking set Name=%s where Mobile_No=%s"
        val=(Name,Mobile_No)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==2:
        mycursor=mydb.cursor()
        sql="update booking set Movie_Name=%s where Mobile_No=%s "
        val=(Movie_Name,Mobile_No)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully") 
    elif choose==3:
        mycursor=mydb.cursor()
        sql="update booking set Timing=%s where Mobile_No=%s"
        val=(Timing,Mobile_No)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==4:
        mycursor=mydb.cursor()
        sql="update booking set No_of_Person=%s where Mobile_No=%s"
        val=(No_of_Person,Mobile_No)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==5:
        mycursor=mydb.cursor()
        sql="update booking set Class=%s where Mobile_No=%s"
        val=(Class,Mobile_No)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==6:
        mycursor=mydb.cursor()
        sql="update booking set Total_amount=%s where Mobile_No=%s"
        val=(Total_amount,Mobile_No)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    else:
        print(">>>>>>>>>>>>Invalid Selection<<<<<<<<<<<<<<")
def delete(Mobile_No):
    mycursor=mydb.cursor()
    sql="delete from booking where Mobile_No=%s"
    mycursor.execute(Mobile_No)
    mydb.commit()
    print(mycursor.rowcount,"records(s) deleted")
    print("Data Deleted Sucessfully")

user=int(input("Select Your Option : "))

if user==1:  
    Name=input("Enter the Name : ")
    Mobile_No=int(input("Enter the Mobile No : "))
    Movie_Name=input("Enter the Movie Name : ")
    Timing=input("Enter the Show Timing : ")
    No_of_Person=int(input("Enter the No of Tickets : "))
    Class=input("Select the Class : ")
    Premium=220
    First_Class=175
    Budget=100
    
    if Premium>=0:
        Total_amount=Premium*No_of_Person
        print(f"Total amount:{Total_amount}")
    elif First_Class>=0:
        Total_amount=First_Class*No_of_Person
        print(f"Total amount:{Total_amount}")
    elif Budget>=0:
        Total_amount=Budget*No_of_Person
        print(f"Total amount:{Total_amount}")
    else:
        print(">>>>>>>Invalid Class<<<<<<<<<<<<")
    insert_data(Name,Mobile_No,Movie_Name,Timing,No_of_Person,Class,Total_amount)
elif user==2:
    view_data()
    
elif user==3:
   print("\t1.Name Updated")
   print("\t2.Mobile No Updated")
   print("\t3.Movie Name Updated")
   print("\t4.Timing Updated")
   print("\t5.No of Person Updated")
   print("\t6.Total amount Updated\n")
   
   
   choose=int(input("\tSelect the choice From 1-6 you need to update : "))
   Mobile_No=int(input("\tEnter the Mobile No : "))
   
   
   if choose==1:
       Name=input("\tEnter the Name :\n")
       update(Name,Mobile_No)
       print(f"{Name},Updated Sucessfully")
   elif choose==2:
       Movie_Name=input("\tEnter the Movie Name : ")
       update(Movie_Name,Mobile_No)
       print(f"{Movie_Name},Updated Sucessfully")
   elif choose==3:
       Timing=input("\tEnter the Timing : ")
       update(Timing,Mobile_No)
       print(f"{Timing},Updated Sucessfully")
   elif choose==4:
       No_of_Person=input("\tEnter the No of Person : ")
       update(No_of_Person,Mobile_No)
       print(f"{No_of_Person},Updated Sucessfully")
   elif choose==5:
       Class=input("\tEnter the Class : ")
       update(Class,Mobile_No)
       print(f"{Class},Updated Sucessfully")
   elif choose==6:
       Total_amount=input("\tEnter the Total Amount : ")
       update(Total_amount,Mobile_No )
       print(f"{Total_amount},Updated Sucessfully")
       
   else:
       print("------------Invalid Selction-----------")
       
elif user==4:
    Mobile_No=input("Enter the Mobile No to Delete : ")
    delete(Mobile_No)
        
        
        
        
        
    