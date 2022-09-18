import time as t
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid19db"

)
mycursor=mydb.cursor()

print(">>>>>>>>>>>>>>>>>>>COVID CASESE IN TAMILNADU<<<<<<<<<<<<<<<<<<<<<")
print("\t\t1.Insert_data")
print("\t\t2.View_data")
print("\t\t3.Update_data")
print("\t\t4.Delete_data\n")
print("\t\tSelect the choice 1to 4\n")

def insert_data(Slno,District,Active_cases,Retrive_cases,Death_rate,Total_cases,Vaccinated_people):
    sql="insert into covid_19(Slno,District,Active_cases,Retrive_cases,Death_rate,Total_cases,Vaccinated_people)values(%s,%s,%s,%s,%s,%s,%s)"
    val=(Slno,District,Active_cases,Retrive_cases,Death_rate,Total_cases,Vaccinated_people)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f"{District},inserted sucessfully\n")
    
def View_data():
    mycursor.execute("select * from covid_19")
    result=mycursor.fetchall()
    for i in result:
        print(i)
        
def update(District,Slno):
    if choose==1:
        mycursor=mydb.cursor()
        sql="update covid_19 set District=%s where Slno=%s"
        val=(District,Slno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==2:
        mycursor=mydb.cursor()
        sql="update covid_19 set Active_cases=%s where Slno=%s"
        val=(Active_cases,Slno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==3:
        mycursor=mydb.cursor()
        sql="update covid_19 set Retrive_cases=%s where Slno=%s"
        val=(Retrive_cases,Slno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==4:
        mycursor=mydb.cursor()
        sql="update covid_19 set Death_rate=%s where Slno=%s"
        val=(Death_rate,Slno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==5:
        mycursor=mydb.cursor()
        sql="update covid_19 set Total_cases=%s where Slno=%s"
        val=(Total_cases,Slno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==6:
        mycursor=mydb.cursor()
        sql="update covid_19 set Vaccinated_people=%s where Slno=%s"
        val=(Vaccinated_people,Slno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")
    elif choose==7:
        mycursor=mydb.cursor()
        sql="update covid_19 set Slno=%s where Slno=%s"
        val=(Slno,Slno)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated Sucessfully")       
    else:
        print("invalid data")
        
def delete(Slno):
    mycursor=mydb.cursor()
    sql="delete from covid_19  where Slno=%s"
    mycursor.delete(Slno)
    mydb.commit()
    print(mycursor.rowcount,"records(s) deleted")
    print("Data Deleted Sucessfully")
user=int(input("Enter your choice : "))
t.sleep(2)

if user==1:  
    Slno=(input("tEnter the Slno : "))
    District=input("Enter the District Name : ").strip()
    Active_cases=input("Total no.of Active cases : ")
    Retrive_cases=(input("Total no of Retrive cases : "))
    Death_rate=(input("Total no of Death cases : "))
    Total_cases=(input("Total no of Cases : "))
    Vaccinated_people=(input("Total no of Vaccinated People : "))
    insert_data(Slno,District,Active_cases,Retrive_cases,Death_rate,Total_cases,Vaccinated_people)
elif user==2:
    View_data()
    
elif user==3:
   print("\t1.District Updated")
   print("\t2.Active_Cases Updated")
   print("\t3.Retive_Cases Updated")
   print("\t4.Death_rate Updated")
   print("\t5.Total_cases Updated")
   print("\t6.Vaccinated_people Updated\n")
   
   
   choose=int(input("\tSelect the choice From 1-6 you need to update : "))
   Slno=int(input("\tEnter the Slno : "))
   
   
   if choose==1:
       District=input("\tEnter the District :\n")
       update(District,Slno )
       print(f"{District},Updated Sucessfully")
   elif choose==2:
       Active_cases=input("\tEnter the Active_cases : ")
       update(Active_cases,Slno )
       print(f"{Active_cases},Updated Sucessfully")
   elif choose==3:
       Retrive_cases=input("\tEnter the Retrive_cases : ")
       update(Retrive_cases,Slno )
       print(f"{Retrive_cases},Updated Sucessfully")
   elif choose==4:
       Death_rate=input("\tEnter the Death_rate : ")
       update(Death_rate,Slno )
       print(f"{Death_rate},Updated Sucessfully")
   elif choose==5:
       Total_cases=input("\tEnter the Total_cases : ")
       update(Total_cases,Slno )
       print(f"{Total_cases},Updated Sucessfully")
   elif choose==6:
       Vaccinated_people=input("\tEnter the Vaccinated_people : ")
       update(Vaccinated_people,Slno )
       print(f"{Vaccinated_people},Updated Sucessfully")
       
   else:
       print("------------Invalid Selction-----------")
       
elif user==4:
    Slno=input("Enter the Slno to Delete : ")
    delete(Slno)
