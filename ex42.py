## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#dog is an Animal
class Dog(Animal):

     def __init__ (self, name):
         ## dog has a name
         self.name = named

#cat is an Animal, animal class has-a cat in it
class Cat(Animal):

    def __init__ (self, name):
        ##cat has a name
        self.name = name

##introducing new class, person is an object
class Person(object):
#an object in a class has attributes
    def __init__ (self, name):
        ##person has-a name
        self.name = name

        #Person has a pet
        self.pet = None

## there is a class on employee inside the class person
class Emloyee(Person):

    def __init__ (self, name, salary):

        super(Employee, self). __init__(name)

        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


## rover is a dog
rover = Dog("Rover")

#sata in a cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

#mary has a pet
mary.pet = satan

##frank in an Employee and has a salary of
frank = Employee("Frank", 120000)

##frank has a peet
frank.pet = rover


flipper = Fish()

crouse = Salmon()

harry = Halibut()
