# Python Notes 9/14/2019:
# A variable name must start with a letter or the underscore character
# Variable names are case-sensitive
# If you try to combine a string and a number, Python will give you an error:
# Global Variables
# Variables that are created outside of a function are known as global variables.
# # Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"


def myfunc():
    global x # global Keyword : use the global keyword if you want to change a global variable inside a function
    x = "fantastic" # new value gets assigned to 'x'
    print("python is "+x)

myfunc()

print("python is "+x)
print("\n\n\n")
# ------------------------------------------------------------------

""""
                Built-in Data Types
    
    Variables can store data of different types, 
    and different types can do different things.
    
            Text Type:	    str
            Numeric Types:	int, float, complex
            Sequence Types:	list, tuple, range
            Mapping Type:	dict
            Set Types:	    set, frozenset
            Boolean Type:	bool
            Binary Types:	bytes, bytearray, memoryview
"""

# using Type() Function

x = 5
print(type(x))

# output:
# <class 'int'>

# Setting the Specific Data Type

x = str("Hello World")
print(type(x))
x = int(20)
print(type(x))
x = float(20.5)
print(type(x))
x = complex(1j)
print(type(x))
x = list(("apple", "banana", "cherry"))
print(type(x))
x = tuple(("apple", "banana", "cherry"))
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = bytearray(5)
print(type(x))
x = bytes(5)
print(type(x))
x = frozenset(("apple", "banana", "cherry"))
print(type(x))
print("\n\n\n")
# Python Numbers
# int Float and Complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# int: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# Float: or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
print()

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print()

# Complex: Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print()

# Type Conversion: You can convert from one type to another with the int(), float(), and complex() methods:

x = 1 # int
y = 2.8 # float
z = 1j # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(type(a))
print(type(b))
print(type(c))

# --------------------------------------------------------------------

print("\n\n\n")

#               Python Casting
# Specify a Variable Type:
"""There may be times when you want to specify a type on to a variable.
This can be done with casting. 
Python is an object-orientated language, and as such it uses classes to define
data types, including its primitive types."""
x = int(1)          # x will be 1
y = int(2.8)        # y will be 2
z = int("3")        # z will be 3

x = float(1)        # x will be 1.0
y = float(2.8)      # y will be 2.8
z = float("3")      # z will be 3.0
w = float("4.2")    # w will be 4.2

x = str("s1")       # x will be 's1'
y = str(2)          # y will be '2'
z = str(3.0)        # z will be '3.0'

# -------------------------------------------------------------------------

#               Python Strings
"""
# Strings are Arrays:  strings in Python are arrays of bytes representing unicode characters.
# Python does not have a character data type, a single character is simply a string with a length of 1
# Python does not have a character data type, a single character is simply a string with a length of 1
"""
a = "Hello, World!"
print(a[1])

# Slicing :Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:5])

# Negative Indexing: Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])

# String Length: Len() Function.

a = "Hello, World!"
print(len(a))

#           String Methods

# strip(): Removes any whitespace

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

#   upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

# replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Check String

#   Ex: Check if the phrase "ain" is present in the following text:

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) # returns True

# Ex: Check if the phrase "ain" is NOT present in the following text:

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) # Returns False

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c) # no space in the output

# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format: we can combine strings and numbers by using the format() method!

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# can use index numbers {0} to be sure the arguments are placed in the correct placeholders

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

"""
Method	Description
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()        	Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()    	Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning
"""

# Python Booleans :Booleans represent one of two values: True or False.

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))
# Almost any value is evaluated to True if it has some sort of content
"""Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

ne more value, or object in this case, evaluates to False, and 
that is if you have an objects that are made from a class with a
 __len__ function that returns 0 or False:
"""


class myclass():
  def __len__(self):
    return 0

  def bools(self):
    return 1


myobj = myclass()
print(bool(myobj.bools()))


# Functions can Return a Boolean: like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

# -------------------------------------------------------------------

# Python Operators
"""
Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators: is / is not
Membership operators : in / not in
Bitwise operators : are used to compare (binary) numbers
"""
# -------------------------------------------------------------------

#   Python Lists
#   Python Collections (Arrays)
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

"""

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  #Changing second item

# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Add Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To add an item at the specified index, use the insert() method:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove Item

# remove() method

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop() method
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del() keyword

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

del thislist # Deletes complete list

# clear() method empties list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""
Copy a List
You cannot copy a list simply by typing list2 = list1,
because: list2 will only be a reference to list1, and changes made 
in list1 will automatically also be made in list2.
There are ways to make a copy, one way is to use the built-in List 
method copy().

"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# Join Two Lists +

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# append

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# The list() Constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# List Methods

"""
Method	        Description
append()	    Adds an element at the end of the list
clear()     	Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
"""

# -----------------------Python Tuples-------------------------------

# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Change Tuple Values
"""Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple."""

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""                 Create Tuple With One Item
To create a tuple with only one item, you have add a comma after the item, 
unless Python will not recognize the variable as a tuple."""

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Remove Items
# Note: You cannot remove items in a tuple.

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Tuple Methods

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# -----------------------------------------------------------------------------

#                       Python Sets

# sets: A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Access Items
"""You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
But you can loop through the set items using a for loop, 
or ask if a specified value is present in a set, by using the in keyword"""

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Example

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) # Retuns True

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

"""Add Items
To add one item to a set use the add() method.
To add more than one item to a set use the update() method."""

# add() Method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# update method
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)


# Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

"""Remove Item
To remove an item in a set, use the remove(), or the discard() method."""

# remove() method
# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# discard() method
# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# pop()
# Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clear() method:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# del keyword

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset) this will raise an error

"""Join Two Sets
There are several ways to join two or more sets in Python.
You can use the union() method that returns a new set containing all items from both sets, or the update() 
method that inserts all the items from one set into another:"""

# union() method : returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

# The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# Set Methods
#
# Method	            Description
# add()	                Adds an element to the set
# clear()	            Removes all the elements from the set
# copy()	            Returns a copy of the set
# difference()	        Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	            Remove the specified item
# intersection()	    Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	        Returns whether two sets have a intersection or not
# issubset()	        Returns whether another set contains this set or not
# issuperset()	        Returns whether this set contains another set or not
# pop()	                Removes an element from the set
# remove()          	Removes the specified element
# symmetric_difference()            Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# union()	            Return a set containing the union of sets
# update()	            Update the set with the union of this set and others


# --------------------------Python Dictionaries--------------------------------------------

"""Dictionary
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries 
are written with curly brackets, and they have keys and values"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing Items
x = thisdict["model"]

#There is also a method called get() that will give you the same result:
x = thisdict.get("model")


# Change Values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Loop Through a Dictionary

"""You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys 
of the dictionary, but there are methods to return the values 
as well."""

for x in thisdict:
  print(x) # returns all keys

for x in thisdict:
  print(thisdict[x]) # returns all values one by one.

# use values() function to return values of a dictionary

for x in thisdict.values():
  print(x)

# Loop through both keys and values, by using the items() function

for x, y in thisdict.items():
  print(x, y)

# Check if Key Exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Dictionary Length

print(len(thisdict))

# Adding Items : Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Removing Items:

# pop() method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() method removes the last inserted item

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# del keyword

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# del key word can delete entire dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.


# clear() keyword empties the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

"""Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, and changes made 
in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in 
Dictionary method copy()."""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in method dict().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# If you want to Create three dictionaries, than create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# The dict() Constructor makes new dictionary

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# Dictionary Methods
"""
Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and values
get()	        Returns the value of the specified key
items()	        Returns a list containing the a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""

 # ------------------------------------------------------------------------------

# Python If ... Else

# "if statement" is written by using the if keyword
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Elif keyword

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else keyword

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else

a = 2
b = 330
print("A") if a > b else print("B")

# with 3 conditions

a = 331
b = 331
print("A") if a > b else print("=") if a == b else print("B")

# And Keyword

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or keywords

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Nested If

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# ---------------------------------------------------------------
# Python While Loops
# Python has two primitive loop commands:
#
# while loops
# for loops

# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

# Note: remember to increment i, or else the loop will continue forever.

# The break Statement

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# The continue Statement

# Continue to the next iteration if i is 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# ------------------------------------------------------------------

# Python For Loops

"""A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in 
other object-orientated programming languages.With the for loop we can execute a set of statements, 
once for each item in a list, tuple, set etc."""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String

for x in "banana":
  print(x)


# The break Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Ex where break comes before the print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() Function
"""To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments 
by 1 (by default), and ends at a specified number."""

for x in range(6):
  print(x)

"""The range() function defaults to 0 as a starting value, however it is possible to specify
 the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
"""

for x in range(2, 6):
  print(x)

"""The range() function defaults to increment the sequence by 1, however it is possible to specify 
the increment value by adding a third parameter: range(2, 30, 3)"""

for x in range(2, 30, 3):
  print(x)

# Else in For Loop

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Nested Loops
"""A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":"""

# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# ---------------------------------------------------------------------------

# Python Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function

def my_function():
  print("Hello from a function")

# Calling a Function
def my_function():
  print("Hello from a function")

my_function()

# Parameters

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as a Parameter

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values
# To let a function return a value, use the return statement:


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# Arbitrary Arguments
"""If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:"""

# If the number of arguments are unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

"""Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it."""

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# ----------------------------------------------------------------

# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# A lambda function that adds 10 to the number passed in as an argument, and print the result:
print("-"*70)
x = lambda a : a + 10
print(x(5))

# A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b : a * b
print(x(5, 6))

# A lambda function that sums argument a, b, and c and print the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:


def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(2) # change it to 3 and it will calculate the triple instead of double
# mytripler = myfunc(3)
print(mydoubler(11))
# print(mytripler(11))

#Use lambda functions when an anonymous function is required for a short period of time.

# --------------------------------------------------------------------

# Python Arrays
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Arrays : Arrays are used to store multiple values in one single variable:

cars = ["Ford", "Volvo", "BMW"]

"""What is an Array?
An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), 
storing the cars in single variables could look like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
The solution is an array!
An array can hold many values under a single name, and you can access the values by referring to an index number.

"""

# Access the Elements of an Array

x = cars[0]

# Modify the value of the first array item:

cars[0] = "Toyota"

# The Length of an Array

x = len(cars)

# Note: The length of an array is always one more than the highest array index.

# Looping Array Elements

for x in cars:
  print(x)

# Adding Array Elements

# append() method to add an element to an array.

cars.append("Honda")

# Removing Array Elements

# pop() method to remove an element from the array.

cars.pop(1)

# remove() method to remove an element from the array.
# Delete the element that has the value "Volvo":
cars.append("Volvo")
cars.remove("Volvo")

# Note: The list's remove() method only removes the first occurrence of the specified value.

# Array Methods
"""
Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()       	Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list"""

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.


# ---------------------------------------------------------------------

# Python Classes and Objects


"""Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects."""

# Create a Class

# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

# Create Object :use the class named myClass to create objects:

p1 = MyClass()
print(p1.x)

# The __init__() Function
"""The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:"""

# Example
# Create a class named Person, use the __init__() function to assign values for name and age:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Sachin", 35)
print(p1.name)
print(p1.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Object Methods
"""Objects can also contain methods. Methods in objects are functions that belong to the object.
Let us create a method in the Person class:"""

# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

"""The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:"""

# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)

p1.myfunc()

"""
Breakup of above code:
person is a class
p1 is an object
myfunc is a method

"""
# Modify Object Properties
p1.age = 40

# Delete Object Properties

del p1.age

# Delete Objects

del p1

# -------------------------------------------------------------------


# Python Inheritance
"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class."""

# Create a Parent Class


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John","Doe")
x.printname()

# Create a Child Class
"""To create a class that inherits the functionality from another class, send the parent class 
as a parameter when creating the child class:"""


class Student(Person):
  pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


x = Student("Mike", "Olsen")
x.printname()


# Add the __init__() Function

"""So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
Note: The __init__() function is called automatically every time the class is being used to create a new object."""


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Mike", "Olsen")
x.printname()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

# Use the super() Function
# Python also have a super() function that will make the child class inherit all the methods
# and properties from its parent


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


x = Student("Mike", "Olsen")
x.printname()

# Add Properties

# Add a property called graduationyear to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname,lname)
        self.graduationyear = 2019


x = Student("Sachin","Jadhav")
print(x.graduationyear)

# Add Methods
# Add a method called welcome to the Student class:

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = 2019
    def welcome(self):
        print("Welcome",self.firstname,self.lastname, "to be the class of", self.graduationyear)
x = Student("Sachin","Jadhav",2019)
x.welcome()

#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

# ---------------------------------------------------------------------------------

# Python Iterators

"""An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()."""

# Iterator vs Iterable
"""Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:"""

# Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:

mystr ="Sachin"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Looping Through an Iterator
# use a for loop to iterate through an iterable object:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# Create an Iterator
"""To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
 all classes have a function called __init__(), which allows you do some initializing when the object is being created.
 The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""
# Create an iterator that returns numbers, starting with 1, and
# each sequence will increase by one (returning 1,2,3,4,5 etc.):


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x=self.a
        self.a +=1
        return x


myclass = MyNumbers()
myitr = iter(myclass)

print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))

# StopIteration
"""The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
To prevent the iteration to go on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:"""

# Stop after 20 iterations:


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# -------------------------------------------------------------------------------

# Python Scope

# A variable is only available from inside the region it is created. This is called scope.

# Local Scope

# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()

# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#Global Scope

"""A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local."""

# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Naming Variables
"""If you operate with the same variable name inside and outside of a function, Python will 
treat them as two separate variables, one available in the global scope (outside the function) 
and one available in the local scope (inside the function):"""

# The function will print the local x, and then the code will print the global x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Global Keyword

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# ---------------------------------------------------------------------------------

# Python Modules
"""What is a Module?
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application."""

# Create a Module

# Save this code in a file named mymodule.py
#
# def greeting(name):
#   print("Hello, " + name)

# Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")

# Note: When using a function from a module, use the syntax: module_name.function_name.


# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
"""Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}"""


import mymodule

a = mymodule.person1["age"]
print(a)

"""Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:"""

import mymodule as mx

a = mx.person1["name"]
print(a)


# Built-in Modules

import platform

x = platform.system()
x = platform.uname()
print(x)


# Using the dir() Function

import platform

x = dir(platform)
print(x)

# Import From Module
# You can choose to import only parts from a module, by using the from keyword
"""The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}"""

from mymodule import person1

print (person1["age"])
print (person1["country"])

# -------------------------------------------------------------------------------------------------------

# Python Datetime

# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime

x = datetime.datetime.now()
print(x)

# Return the year and name of weekday

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects

# Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
# Display the name of the month:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

"""Directive	 Description	            Example
%a	            Weekday, short version	    Wed	
%A	            Weekday, full version           	    Wednesday	
%w	            Weekday as a number 0-6, 0 is Sunday	3	
%d	            Day of month 01-31	                    31	
%b          	Month name, short version	            Dec	
%B          	Month name, full version	            December	
%m	            Month as a number 01-12	                12	
%y          	Year, short version, without century	18	
%Y	            Year, full version	                    2018	
%H	            Hour 00-23	                            17	
%I	            Hour 00-12	                            05	
%p	            AM/PM	                                PM	
%M	            Minute 00-59	                        41	
%S	            Second 00-59	                        08	
%f	            Microsecond 000000-999999	            548513	
%z	            UTC offset	                            +0100	
%Z	            Timezone	                            CST	
%j	            Day number of year 001-366	            365	
%U	            Week number of year, Sunday as 
                the first day of week, 00-53        	52	
%W	            Week number of year, Monday as the 
                first day of week, 00-53            	52	
%c	            Local version of date and time	
                Mon Dec 31 17:41:00                     2018	
%x	            Local version of date	                12/31/18	
%X	            Local version of time	                17:41:00	
%%	            A % character	                        %
"""

# Python JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Parse JSON - Convert from JSON to Python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))

"""You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

 """
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Order the Result

print(json.dumps(x, indent=4, sort_keys=True))

# --------------------------------------------------------------------

# Python RegEx

"""A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern."""

# RegEx Module


import re

txt = "The rain in Spain"
x = re.search("The.*Spain$",txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


"""RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string"""

# Metacharacters

"""Character	Description	                        Example
[]	            A set of characters	                "[a-m]"	
\	            Signals a special sequence          "\d"	
.	Any character (except newline character)	    "he..o"	
^	Starts with	                                    "^hello"	
$	Ends with	                                    "world$"	
*	Zero or more occurrences                    	"aix*"	
+	One or more occurrences	                        "aix+"	
{}	Exactly the specified number of occurrences	    "al{2}"	
|	Either or	                                    "falls|stays"	
()	Capture and group	                                            """


# Special Sequences

"""
Character	                                                Description	                                            Example
\A	Returns a match if the specified characters are at the beginning of the string	                                "\AThe"	
\b	Returns a match where the specified characters are
    at the beginning or at the end of a word	r"\bain"                                                            r"ain\b"	
\B	Returns a match where the specified characters are present,
    but NOT at the beginning (or at the end) of a word	r"\Bain"                                                    r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	                                            "\d"	
\D	Returns a match where the string DOES NOT contain digits	                                                    "\D"	
\s	Returns a match where the string contains a white space character	                                            "\s"	
\S	Returns a match where the string DOES NOT contain a white space character	                                    "\S"	
\w	Returns a match where the string contains any word characters 
    (characters from a to Z, digits from 0-9, and the underscore _ character)                                   	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	                                        "\W"	
\Z	Returns a match if the specified characters are at the end of the string	                                    "Spain\Z"	

"""

"""Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:"""

"""Set	    Description
[arn]	    Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string"""


# The findall() Function

# Print a list of all matches:

import re

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

# Return an empty list if no match was found:

import re

str = "The rain in Spain"
x = re.findall("Portugal", str)
print(x)

# The search() Function

# Search for the first white-space character in the string:

import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())


# Make a search that returns no match:

import re

str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)

# The split() Function

# Split at each white-space character:/string has been split at each match:

import re

str = "The rain in Spain"
x = re.split("\s", str)
print(x)

# The sub() Function

# Replace every white-space character with the number 9:sub() function replaces the matches with the text of your choice:


import re

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

# Replace the first 2 occurrences:

import re

str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)

# Match Object

"""A Match Object is an object containing information about the search and the result.
Note: If there is no match, the value None will be returned, instead of the Match Object."""

# Do a search that will return a Match Object:

import re

str = "The rain in Spain"
x = re.search("ai", str)
print(x) #this will print an object

"""The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match"""

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":

import re

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())
print(x.string)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object.

# -------------------------------------------------------------------------------

# Python PIP
"""PIP is a package manager for Python packages, or modules if you like."""

# Using a Package

# Import and use "camelcase":

import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.


# Python Try Except

"""The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, 
regardless of the result of the try- and except blocks."""

# The try block will generate an exception, because x is not defined:

try:
  print(x1)
except:
  print("An exception occurred")

#The try block will generate a NameError, because x is not defined:

try:
  print(x1)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Else

# In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# try to open and write to a file that is not writable:

# try:
#   f = open("demofile.txt")
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
# finally:
#   f.close()


# -----------------------------------------------------------------------
# Python Strings
# Command Line Input
print("Enter your name:")
x = input()
print("Hello ", x)
# -----------------------------------------------------------------------

# Python String Formatting

# String format(): The format() method allows you to format selected parts of a string.
# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



































