#5. Data Structures

#5.1 more on list functions
# #
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# # f ="hello" # 
# print(type(f))
# print(fruits)
# # print(type(fruits))
# # print(fruits.count('apple'))
# # print(fruits.count('tangerine'))
# # print(fruits.index('banana'))
# # print(fruits.index('banana', 4))  # Find next banana starting a position 4
# # fruits.reverse()
# # print(fruits)
# # fruits.sort(reverse= True)
# # print(fruits)
# fruits.append('grape')
# print(fruits)
# # fruits.sort()
# # print(fruits)
# print(fruits.pop())
# print(fruits)


#5.1.1 use list as a stack
#
# stack = [3, 4, 5]
# stack.append(6)
# print(stack)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

#5.1.2 use list as an Queue

#we are importing functions from other classes
#from "classname" import "function/method/object"

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# # queue = ["Eric", "John", "Michael"])
# print(queue)
# queue.append("Terry")           # Terry arrives
# print(queue)
# queue.append("Graham")          # Graham arrives
# print(queue)
# queue.popleft()                 # The first to arrive now leaves
# print(queue)
# queue.pop()                 # The second to arrive now leaves
# print(queue)                    # Remaining queue in order of arrival



#5.1.3 List Comprehensions creating a list:
# # #method 1
# squares = []
# for x in range(10):
#     squares.append(x**2)
#
# print(squares)

# #method 2
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)
#
# # #method 3
# squares = [x**2 for x in range(10)]
# print(squares)

#best practice
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# #
# print(combs)
# #or we can use shorter version
#
# l= [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(l)

#few more for practice:

# vec = [-4, -2, 0, 2, 4]
# print(vec)
# create a new list with the values doubled
# print([x*2 for x in vec])

# filter the list to exclude negative numbers
# print([x for x in vec if x >= 0])

# apply a function to all the elements
#find out what abs() is used for
# print([abs(x) for x in vec])
#
# call a method on each element strip whitespaces

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print(freshfruit)
# print([weapon.strip() for weapon in freshfruit])

# # create a list of 2-tuples like (number, square)
# print([(x, x**2) for x in range(6)])
#
# the tuple must be parenthesized, otherwise an error is raised
# print([x, x**2 for x in range(6)])

# flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])

#bit complex list operation

# from math import pi
# # find more about 'round' function
# print([str(round(pi, i)) for i in range(1, 6)])




#5.1.4 Nested List Comprehensions

# we need to print 3x4 matrix but transpose it while printing
#
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# print(matrix)
#
# #how to print it in transposed state
#
# print([[row[i] for row in matrix] for i in range(4)])
#
# #regular way
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
#
# print(transposed)
#
# #same as
#
# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#
# print(transposed)
# #In the real world, you should prefer built-in functions
# #to complex flow statements. The zip() function
# #would do a great job for this use case:
#
# print(list(zip(*matrix)))
#
# # '*' used above is like we worked on unpacking the arguments


#5.2 Del Statement


# a = [-1, 1, 66.25, 333, 333, 1234.5]
# print(a)

# del a[0]
# print(a)
#
# #slice index 2 & 3
# del a[2:4]
# print(a)

# del a[:]                        #it will delete the entire variable
# print(a)




#5.3 Tuples and Sequences(Sequence Types — list, tuple, range)

# t = 12345, 54321, 'hello!'
# # print(t[0])
# #sequence unpacking
#
# x,y,z=t
# print(x)
# print(t)
#
# # Tuples may be nested:
# u = t, (1, 2, 3, 4, 5)
# print(u)
#
# # Tuples are immutable:
# t[0] = 88888
#
#
# but they can contain mutable objects:
# v = ([1, 2, 3], [3, 2, 1])
# print(v)



#5.4. Sets / dictionary


# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                      # show that duplicates have been removed
#
# print('orange' in basket)                 # fast membership testing
#
# print('crabgrass' in basket)
#
#
# # Demonstrate set operations on unique letters from two words
#
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)                                  # unique letters in a
#
# print(a - b)                             # letters in a but not in b
#
# print(a | b)                              # letters in a or b or both
#
# print(a & b)                              # letters in both a and b
#
# print(a ^ b)                              # letters in a or b but not both

#similary to list Comprehensions set Comprehensions also possible (refer 5.1.3)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

#5.5. Dictionaries (also know as as “associative memories” or “associative arrays”.)
#create dectionary

# tel = {'jack': 4098, 'sape': 4139}
# #add key and value to dictionary
# print(tel)
# tel['guido'] = 4127
# # # tel = {'guido': 4127}
# # print(tel)
# #
# # print(tel['jack'])
# #
# # del tel['sape']
# # print(tel)
# tel['irv'] = 4127
# print(tel)
# #
# print(list(tel))
#
# print(sorted(tel))
#
# print('guido' in tel)
# print('jack' not in tel)

#The dict() constructor builds dictionaries directly from
#sequences of key-value pairs:

# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
#
# #dictionary from Arbitrary keys and values
#
# print({x: x**2 for x in (2, 4, 6)})
#
# # specify pairs using keyword arguments check def dict()
#
# print(dict(sape=4139, guido=4127, jack=4098))
#
# 5.6. Looping Techniques
#When looping through dictionaries, the key and corresponding value
#can be retrieved at the same time using the items() method.

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

#When looping through a sequence, the position index and
#corresponding value can be retrieved at the same time using the enumerate() function.

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

#To loop over two or more sequences at the same time,
#the entries can be paired with the zip() function.
#
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence
# in a forward direction and then call the reversed() function.


# for i in reversed(range(1, 10, 2)):
#     print(i)



#To loop over a sequence in sorted order, use the sorted()
#function which returns a new sorted list while leaving the source unaltered.


# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

#
# It is sometimes tempting to change a list while you are looping over it;
# however, it is often simpler and safer to create a new list instead.
#
# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
#
# print(filtered_data)


#5.7. More on Conditions

# string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)

#5.8. Comparing Sequences and Other Types

# check with python shell

# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
