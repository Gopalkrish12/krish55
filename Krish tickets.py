print("Welcome to python online ticket booking system")
print("1.movie ticket booking system")
choice=int(input("enter 1 to continue: \n"))
if choice==1:
    print("you enterd movie booking system")
    
    def movie():
        print("1.movie1\t2.movie2\t3.movie3\t4.movie4")
        mn=int(input("choose the movie followed by 1,2,3,4\n"))
        if mn==1:
            print("you choosen the movie: movie 1\n")
            theater()
        elif mn==2:
             print("you choosen the movie: movie 2\n")
             theater()
        elif mn==3:
            print("you choosen the movie: movie 3\n")
            theater()
        elif mn==4:
             print("you choosen the movie: movie 4\n") 
             theater()
        else:
            print("wrong selection")
            movie()
    def theater():
        print("1.location1\t2.location2\t3.location3\t")
        tl=int(input("choose the location of theater:"))
        if tl<=4:
            timings()
        else:
            print("wrong selection")
            movie()
    def timings():
        print("you entered timing section")
        tw=int(input("enter number of ticket you wanted:\n"))
        print("your booking tickts count is:",tw)
        time={
            "1":"10.00-1.00",
            "2":"1.00-4.00",
            "3":"4.00-7.00",
            "4":"7.00-10.00"
            }
        print(time)
        t=int(input("choose the timing followed by 1 2 3 4:\t"))
        if t==1:
            print("your movie timing is:\t 10.00 AM-1.00 PM")
            greetings()
        elif t==2:
            print("your movie timing is:\t 01.00 PM-4.00 PM")
            greetings() 
        elif t==3:
            print("your movie timing is:\t 04.00 PM-07.00 PM")
            greetings() 
        elif t==4:
            print("your movie timing is:\t 07.00 PM-1.00 PM")
            greetings()
        else:
            print("wrong selection")
            timings()
    def greetings():
        print("succesfuly ticket booked!")   
        print("Enjoy")
movie()
