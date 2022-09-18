print("\nWELCOME TO INDIAN BANK ATM\n")
print("************")
print("INSERT YOUR ATM CARD\n")
print("************")
print("please wait your card was processing\n")
print("************")
balance=30000
pin=int(input("enter your PIN number\n"))
print("************")
while pin==1111:
    print("1.Cash withdraw\n")
    print("2.Balance Enquiry\n")
    print("3.fast cash withdrawe\n")
    print("4.pin generate\n")
    choice=int(input("please choose your option followed by 1 2 3 4 \n"))
    if choice==1:
        print("you choosen cash withdrawe\n")
        w=int(input("please enter your amount in terms of 100\n"))
        if ((balance>w) and (w % 100==0)and (w!=0)):
            print("\ncollect your cash and your withdrawal amount is\t",w)
            rb=balance-w
            print("Available balance is:\t",rb)
            print("thank you visit again")
            break
        elif(w % 100!=0):
            print("\ninvalid selection of amount\n")
            print("\nenter cash again or choose fast cash withdraw method\n")
            print("***********\n")
            continue
        elif (balance-w==0):
            print("you need to maintain minimum balance of rs.500\n")
            print("\nAvailable balance is:",balance)
            print("***********\n")
            continue
        elif w==0:
            print("you entered rs.0 please enter more than rs.100\n")
            print("***********\n")
            continue
        else:
            print("invalid amount is entered\n")
    if choice==2:
        print("your balance amount is",balance)
    if choice==3:
        print("you selected fast cash withdraw \n")
        print("1.500\n")
        print("2.1000\n")
        print("3.2000\n")
        print("4.3000\n")
        print("5.4000\n")
        fcw=int(input("choose amount followed by\n"))
        if fcw==500:
            print('you entered amoount is "500" collect your cash')
            break
        elif fcw==1000:
            print('you entered amoount is "1000" collect your cash')
            break
        elif fcw==2000:
            print('you entered amoount is "2000" collect your cash')
            break
        elif fcw==3000:
            print('you entered amoount is "3000" collect your cash')
            break
        elif fcw==4000:
            print('you entered amoount is "4000" collect your cash')
            break
        elif fcw==5000:
            print('you entered amoount is "5000" collect your cash')
            break
        else:
            print("wrong amount choosen")
            continue

    if choice==4:
            print("Welcome to pin generation\n")
            mobno=int(input("Enter your 10 digit mobile number linked with bank account: "))
            DOB=int[9](input("enter your date of birth in term of dd-mm-yyyy: "))
            pin2=int[4](input("enter the OTP send your mobile number: "))
            print("your PIN is : 1888")
else:
       print("you entered wrong pin")
