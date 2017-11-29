from sys import exit
from time import sleep

def game():
    print "So, wanna see a trick? yes or no? "

    choice = raw_input("> ")

    if choice == "yes":
        preparation()

    elif choice == "no":
        print ">Ay, doesn't matter, I will do it anyways"
        sleep(2)
        preparation()

def preparation():
    print ">Would you believe me if I told you that I can guess your birthday?"

    choice = raw_input("> ")
    if choice == "yes":
        print ">Good, now you'll see the power of Homer 2000 in action."
        sleep(2)
        trick()
    elif choice == "no":
         print ">I see, no fun allowed here :( "
         exit(0)
    else:
        print ">Ay, doesn't matter, I will do it anyways"
        sleep(2)
        trick()

def trick ():
    print ">Multiply the day of your birth by 2 (e.g. 12*2)"
    sleep(3)
    print ">Now, please add 5 to it"
    sleep(3)
    print ">For the next one you might want to grab a calculator"
    sleep(3)
    print ">Multiply the current result of your calculations by 50"
    sleep(3)
    print ">Add the number of the month of your birthday to the result of your calculations (e.g. January - 1; February - 2 etc.)"
    sleep(3)
    print ">Enter the result of your calculations"
    sleep(2)


    x = raw_input("> ")
    x = int(x)
    y = x - 250
    y = int(y)
    day = y / 100.
    month = y % 100
    monthsname = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]

    print (">Alakazam! Your birthday is on %d %s" % (day,  monthsname[month-1]))
    sleep(2)
    end()

def end ():
    print ">Are you impressed by my terrific might?"

    choice = raw_input("> ")

    if choice == "no":
        print ">Are you sure? I'm gonna ask you again"

        choice = raw_input("> ")

        while choice == "no":
            end()

        else:
            print "Thanks, I appreciate"
            print ("Bye!")
            exit(0)

    else:
        print "Thanks, I appreciate"
        print ("Bye!")
        exit(0)

def start():
    print "Hello, what's your name?"

    yourname = raw_input("> ")
    print "Nice to meet you %s !" %yourname
    sleep(2)
    print "My name is Homer 2000"
    sleep(2)
    game()

start()
