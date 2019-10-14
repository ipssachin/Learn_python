#using assert statement
#
# x = int(input("Enter a number grater than 0: "))
# #
# assert x>0, "Wrong input entered."
# print("You have entered: ",x)
# #
#using exception handler
#
# x = int(input("Enter a number grater than 0: "))
# try:
#     # x = int(input("Enter a number grater than 0: "))
#     assert x>0, "Wrong input entered."
#     print("You have entered: ",x)
# except AssertionError:
#     print("Wrong input provided")
# except ValueError:
#     print("Enter integer value.")

#What is an array?

#creating an array

from array import *
# import array
#
# # a = array.array('i',[5,6,7,2,44,15])
# a = array('i',[5,6,7,2,44,15])
# # #
# print("The elements in array are: ")
# for elements in a:
#     print(elements)

#v2

# arr = array.array('u',['s','a','c','h','i','n'])
# #
# print("The elements in array are: ")
# for chr in arr:
#      print(chr)

# indexing and slicing on arrays
#
# x = array('i',[10,20,30,40,50,60])

# print(x)
#find number of elements in array
# l = len(x)
#
# #With for loop
# for i in range(l):
#     print(x[i], end=' ')
# # #with while loop
# i = 0
# print('\n')
# while i<l:
#     print(x[i],end=' ')
#     i+=1


#create array y with elements from the 1st and 3rd from x
#???
# y = array('i',[])
# for i in x[1:3]:
#     y.append(i)
# print(y)

#create array y from last 4 elements of # X


#create y with last 4th element and with 3[-4-(-1)=-3] elements towards right

#create y with 0th to 7th element from x.
#Stride every 2

#check array methods

#write all elements to the file
#a.tofile(f)

#
from array import *

arr = array('i',[10,20,50,70,6,90,45,78,64,35,20,30,80,44])

print("orignal array: ",arr)

# #append
#
arr.append(30)
arr.append(60)
# #
print("array after appending 30 & 60: ", arr)
#
# #insert 99 at 1st position

arr.insert(5,99)
print("array after insert operation : ", arr)
#
# #remove an element from the array
#
arr.remove(20)
print("array after remove(20) operation : ", arr)
#
# #finding position of element using index method
#
# n = arr.index(30)
# print("index of first instance of 30 is: ",n)
#
# #convert an array into a list
# lst=arr.tolist()
# print("converted array to a list: ",lst)

# #convert an array into a byte string
# str=arr.tostring()
# print("converted array to a string: ",str)
# #--------------------------------------------------------------------------------
# #lets create a program accepting inputs from the user
#
# from array import *
#
# str = input("Enter marks for a studen: ").split(',')
# print(str)
#
# #create marks array using values fromk str
#
# marks = [int(num) for num in str]
#
# #display the marks and total
# sum = 0
# for x in marks:
#     print(x)
#     sum+=x
# print("total marks = ",sum)
#
#
# #display pecentage
# n=len(marks)
# percent = sum/n
# print("percentage: ", percent)

#interesting unicode

# name = u'\u0915\u094b\u0930  \u092a\u0948\u0925\u0964\u0928'
# print(name)
