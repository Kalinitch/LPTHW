# Hello everyone, this is your final test.
#GOOD LUCK!!

# Please comply to the following convention during the test:
#
# - name your functions or classes like this:
#
#   def my_function_5(), class MyClass_7(object)
#
#   ---> the number should be identical to the number of the exercise.
#   If you need more than one function or class use additional alphabethical labeling.
#   example:  def my_function_1_a()
#
# TIP: Test your code by executing your script in the command line. (don't forget to call your functions)
#
# Notice: You can use all materials you have and research online. Make sure you keep an eye on the TIME when researching.
# I can recommend this cheat sheet:


#1. Functions
#________________________________________________________________________________
#Build a function which
# - takes terminal input from a user
# - converts it to an integer type
# - adds another number
# - prints out the result
#

#1.1
#_________________
#Implement error handling for input of non-numerical type.

#example 1 solution
def my_function_1_1_a():
    u_inp = raw_input("Please type a number\n>")
    if u_inp.isdigit():
        u_inp = int(u_inp)
        u_inp += 3
        print u_inp
    else:
        my_function_1_1_a()

#example 1 solution
def my_function_1_1_b():
    u_inp = raw_input("Please type a number\n>")
    try:
        u_inp = int(u_inp)
        u_inp += 3
        print u_inp
    except:
        user_input_1_1_b()

#1.2
#_________________
#Implement error handling for input shorter or longer than 5 digits.

def my_function_1_2():
    u_inp = raw_input("Please type a number\n>")
    if len(u_inp)==5:
        try:
            u_inp = int(u_inp)
            u_inp += 3
            print u_inp
        except:
            user_input_1_2()
    else:
        print "The number must have 5 digits."
        my_function_1_2()

#my_function_1_2()

#2. Functions, Strings
#_________________
# - Modify your function from #1. in a way to accept only STRING typed input.
# - Convert the string to lowercase during the prompt.
# - Don't forget to add a number to the input. Adapt your code to make this work.
# (Your output shoould look something like this: "String9")


def my_function_2():
    name = raw_input("What is your name?\n>").lower()
    if name.isalpha():
        name += "3"
        print name
    else:
        my_function_2()


#3. Functions, Parameters
#________________________________________________________________________________
#Take your function from #1. and change it so it uses a function parameter instead of user input.
def my_function_3(number):
    try:
        number = int(number)
        number += 3
        print number
    except ValueError:
        print "Wrong parameter type. Expected type: <int>"



#4. Loops and Lists
#________________________________________________________________________________
#Build a function taking 3 inputs from a user, implementing the requirements from #1. and #1.1 (integer conversion, error handling).
#
# - Store the result in a list
# - Print out the list in the end

#example 1 solution
def user_input_4_a():
    answers = []
    while len(answers) < 3:
        answer = raw_input("Please enter a number.\n")
        if answer.isdigit():
            answer = int(answer)
            answers.append(answer)
    print answers

#example 2 solution
def user_input_4_b():
    answers = []
    while len(answers) < 3:
        answer = raw_input("Please enter a number.\n")
        try:
            answer = int(answer)
            answers.append(answer)
        except:
            pass
    print answers




#5. Functions, Conditions
#________________________________________________________________________________
# Build a function which prompts the user for two inputs: name and zipcode.
# - Define two lists.
# - If the zipcode starts with a digit lower than 5, store both, zipcode and name, in the first list. Store those two values also as list.
#   Example: data1 =[["Jane", 12937]]
# - Do the equivalent for the remaining possibility/-ies.
# - Print out and return the lists in the end.
# - Implement error handling.


# You are free to decide in which order you prompt the user for the two values.



def my_function_5():
    data1 = []
    data2 = []
    name = None
    zipcode = None

    while not data1 or not data2:
        while not name:
            pre_name = raw_input("What is your name?\n")
            if pre_name.isalpha():
                name = pre_name.capitalize()
            else:
                print "Please type only letters."
        while not zipcode:
            tmp_zipcode = raw_input("What is your zipcode?\n")
            if tmp_zipcode.isdigit():
                zipcode = int(tmp_zipcode)
                first_number = int(tmp_zipcode[0])
                if first_number < 5:
                    data1.append(name)
                    data1.append(zipcode)
                else:
                    data2.append(name)
                    data2.append(zipcode)
            else:
                print "Please type only numbers!"

        print "data1: ", data1
        print "data2: ", data2
        return [data1,data2]


#5.1 Lists
#_________________
# - Assign the result from #5. to a variable.
#  (Don't forget to use the return statement inside your function to be able to access the value from the surrounding context.)
#
#  (You need two lists again, carrying the same properties. So make sure you unpack the result from your previous function properly.)
#
# - Add the following entries to the lists, using list build-in functions.
#  (Store the values into the proper list according to the same conditions as in #5.):
#
#       1. name = "Q", zipcode = 10000
#       2. name = "Seven of Nine", zipcode = 77777
#
#   (Make sure you are consistent with the position of name and zipcode in your lists, following the same pattern you used in #5.)
#
# - Print out the data.


data = my_function_5()
print "data: ", data

data1 = []
data2 = []
data1.append(data[0])
data1.append(["Q",10000])

data2.append( data[1])
data2.append(["Seven",77777])

print "data1: ", data1
print "data2: ", data2

#5.2 Lists (BONUS)
#_________________
# - Delete any empty entries if you have any.
# - Print out the clean list.


for i in data1:
    if i == []:
        data1.remove(i)

for i in data2:
    if i  == []:
        data2.remove(i)

#or
#del data1[i]

#or

data1 = list(x for x in data1 if x)
data2 = list(x for x in data2 if x)

#or

data1 = filter(None, data1)
data2 = filter(None, data2)


#checking
print "Deleting empty entries ..."
print "\ndata1: ", data1
print "\ndata2: ", data2


#6. Dictionaries
#________________________________________________________________________________
# Use your lists from #5.1. and convert them to dictionaries. Store the name as key and the zipcode as value.
#
# (If you have no result from #5.1 Create two lists containing the values from #5.1, and one additional value, replacing the user input from #5.
#  Convert these lists to dictionaries.)

#First solution step, if without result from #5.
# data1 = [10000,"Q"]
# data2 = [77777, "Seven of Nine"]

#Example if key value swap is necessary
data1 = dict((x, i) for i,x in data1.iteritems())
data1 = dict((x, i) for i,x in data1.iteritems())

# Example solution:
data1, data2 = dict(data1), dict(data2)
print data1
print data2



#6.1 Dictionaries
#_________________
# - Store the two dictionaries separately into another dictionary. The keys should be something like "users_1", "users_2", or "users_0_4", "users_5_9".
# - Add the following values using built-in dictionary methods:
#       1. name = "Homer", zipcode = 80890
#       2. name = "Ada", zipcode = 42424
# - Print out the new dictionary.

users = {}
users["users_1"] = data1
users["users_2"] = data2

users["users_2"]["Homer"] = 80890
users["users_1"]["Ada"] = 42424

print users


#6.2 Dictionaries
#_________________
# - Delete the entry with key "Q".
# - Implement error handling for the case the key doesn't exist.

#Example solution 1:
print "Deleting Q ....\n"
# for i in users.values():
#     print "i: ", i
#     try:
#         i.pop("Q")
#     except KeyError:
#         print "Key not found in this list."


#Example solution 2:

for i in users.values():
    if "Q" in i.keys():
        i.pop("Q")
    else:
        pass

#Example solution 3:
for i in users.values():
    if i.has_key("Q"):
        i.pop("Q")
    else:
        pass


print users

#6.3 Dictionaries
#_________________
# - Merge the two dictionaries in one, without subdividing it any longer.
# - Remove the entry with key "Homer"


print "Merging to one dict ..."
users_new = users["users_1"]
users_new.update(users["users_2"])
print users_new

print "Deleting 'Homer' ... "
users_new.pop("Homer")

print users_new


#7. Opening and Writing Files
#________________________________________________________________________________
# - Store the keys and the values from our dictionary into two separate lists.
# - Open a file named userlist.txt.
# - Store the two lists in this file. Write every item from the list on a new line. Write a comma after each list.
# - Open the file in a way which overwrites the previous content.


# (IF YOU DON'T HAVE A PREVIOUS RESULT: create a dictionary with the entries from #1.)


#Example solution 1:

keys = list( x + "\n" for x in users_new.keys() )
values = list( str(x) + "\n" for x in users_new.values() )

print "keys: ", keys, "\n", "values: ", values


document = open("userlist.txt", "w+")
document.writelines(keys)
document.writelines(",\n")
document.writelines(values)
document.close()

#Example solution 2, using "with" while opening file:

# with open("userlist.txt", "w+") as document:
#     document.writelines(keys)
    # document.writelines(",\n")
    # document.writelines(values)

#Example solution 3:

#check
print "Checking writing process: "
document = open("userlist.txt")
contents = document.read()
print contents
document.close()

#6. Classes
#________________________________________________________________________________
# - Create a class called User.
# - Add attributes to the class containing the following information: unique ID, name, password, borrowed media.
#
# The value for the unique ID attribute should be passed over during instantiation. Name and password should be left blank.

# The borrowed_media attribute should be a dictionary type.
# Every item should have an ID (being unique for every media item, like the ISBN) as key and another dictionary as value, containing the information about title, author etc.
# Add one item to the dictionary XYZ1000:{"title":"Clean Coder","author":"Martin, Robert. C","topic":"Softwaredevelopment"}

class User(object):
    def __init__(self, ID)
        self.ID = ID
        self.name = ""
        self.password = ""
        self.borrowed_media = {
                                XYZ1000:{"title":"Clean Coder","author":"Martin, Robert. C","topic":"Softwaredevelopment"}
                                }

# - Define a method of the User class, called borrow().
# - It should take one argument (f.i. called media) and store the value as item in its borrowed_media dictionary.
    def borrow(self, media):
        self.borrowed_media.update(media)

# Test your function by instantiating User and invoquing it's borrow() method. Add the following entry





# def test():
#     assert:
#
