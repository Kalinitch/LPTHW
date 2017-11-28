from sys import exit

def start():
    print "Hello, what's your name?"

    yourname = raw_input("> ")
    print ("Hi " + yourname + "!")

def game():
    print "So, wanna see a trick? yes or no? "

    choice = raw_input("> ")
	
    if choice == "yes":
        game1()

    elif choice == "no":
        print ">Ay, doesn't matter, I will do it anyways"

def game1():
    print ">Would you believe me if I told you that I can guess your birthday?"
		
    choice = raw_input("> ")
    if choice == "yes":
        print ">Good, now you'll see the power of Homer 2000 in action."
    elif choice == "no":
         print ">I see, no fun allowed here :( "
         exit(0)
    else:
        print ">Ay, doesn't matter, I will do it anyways"
		
def preparation():
    print ">Would you believe me if I told you that I can guess your birthday?"

    choice2 = raw_input("> ")
	
    if choice2 == "yno":
        print ">I see, no fun allowed here :( "
        print ("Bye " + yourname + ",what a loser!")
        exit(0)
    elif choice2 == "yes":
        print ">Good, now you'll see the power of Homer 2000 in action."
    else:
        print ">Ay, doesn't matter, I will do it anyways"
def trick ():
    
    print ">Multiply the day of your birth by 2 (e.g. 12*2)"
    print ">Now, please add 5 to it"
    print ">For the next one you might want to grab a calculator"
    print ">Multiply the current result of your calculations by 50"
    print ">Add the number of the month of your birthday to the result of your calculations (e.g. January - 1; February - 2 etc.)"
    print ">Enter the result of your calculations"
	
    
    x = raw_input("> ")
    x = int(x)
    y = x - 250 
    y = int(y)	
    day = y / 100.
    month = y % 100
    monthsname = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
	
    print (">Alakazam! Your birthday is on %d %s" % (day,  monthsname[month-1]))

def end ():
    print ">Are you impressed by my terrific might?"

    choice3 = raw_input("> ")
	  
    while choice3 == "no":
        print ">Are you sure? Maybe you might want to reconsider? Take your time, I'll wait"
        print ">So, did you think about it? I'm going to ask you again"
    else:
        print "Thanks, I appreciate"
        print ("Bye!")

start()
game()
preparation()
trick()
end()
