class Student(object):  # mentioning object is not compulsory
    # the below blocks defines attributes/variables (__init__(self) also called as constructor)
    def __init__(self):  # this internal method is used to initialize the variables
        self.name = "Sachin"
        self.age = 20
        self.marks = 900
        self.school ="SNP"

    # the block below defines a method
    def talk(self):  # instance method using self as first parameter
        print("Hi, I am ", self.name)
        print("My age is ", self.age)
        print("My marks are", self.marks)
        print("My School is", self.school)


# Creating an instance/object of a class  instancename = classname()

s1 = Student()
print(id(s1))  # used to print memory location in the heap in decimal number format.
# s1.name
# s1.age
# s1.marks

# call the method using instance
s1.talk()
print('['+'-'*25 +']'+'\n')
print()
print('['+'-'*25 +']'+'\n')

"""Additional Notes on class:

        The self variable: it contains the memory address of the instance of the current class
        Constructor: is a special method that is used to initialize the instance variables of a class
                     constructor is called at the time of creating an instance
        
"""

# let see an example where we pass arguments to the class instance


class Studen1:
    # this is a constructor
    def __init__(self, n = None, m = 0):
        self.name = n
        self.marks = m
    # this is an instance method

    def display(self):
        print('Hi', self.name)
        print("Your marks", self.marks)
print('['+'-'*25 +']'+'\n')

print('*'*10)
# passing the arguments to the instance created for Student1 class
s1 = Studen1('Sagar', 880)
s2 = Studen1(n = input("Enter student name: "), m = int(input("enter marks:")))
s1.display()
s2.display()
print('*'*10)


# Types of Variables
"""
    Instance variables and class variables or static variables
    
    instance variables: the variables whose separate copy is created in every instance.
                        if we modify copy of any variable in instance it will not affect other copies.
    
    """
print('['+'-'*25 +']'+'\n')

class Sample:
    def __init__(self):
        self.x = 10

    def modify(self):
        self.x += 1

print('['+'-'*25 +']'+'\n')
s1 = Sample()
s2 = Sample()
print("x in S1=", s1.x)
print("x in S2=", s2.x)


# Modify x in S1
print()
s1.modify()
print("x in S1=", s1.x)
print("x in S2=", s2.x)

print('['+'-'*25 +']'+'\n')


""" Class Variables: unlike instance variables class variable's single copy is available 
to all instances of the class."""


class Sampl1:
    # this is the class variable
    x = 10

    # this is the class method
    @classmethod  # we used this built in decorator statement to mark this method as a class method
    def modify(cls):  # a class method acting as a class variable, 'cls' is used to access the class variable
        cls.x += 1





s1 = Sampl1()
s2 = Sampl1()
print('x in s1=', s1.x)
print('x in s2=', s2.x)

s1.modify()

print('after modify x in s1=', s1.x)
print('after modify x in s2=', s2.x)

print('['+'-'*25 +']'+'\n')
