#excercise
#Sort Tuple(A,a,b,c,C,B,D,z,Y,'44') & (1,22,43,98,37,12,53)

# a = ('A','a','b','c','C','B','D','z','Y','44')
# b = (1,22,43,98,37,12,53)
#
# l = list(a)
# m= list(b)
# l.sort()
# m.sort()
# a = tuple(l)
# b= tuple(m)
# print(a)
# print(b)
#
#
# #create worker class accept name and salary give raise to employees & print last name of employees
#
#
# class Worker:
#     def __init__(self, name, pay): # Initialize when created
#         self.name = name # self is the new object
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1] # Split string on blanks
#
#     def giveRaise(self, percent):
#         self.pay *= (1.0 + percent) # Update pay in-place
#
# Sam = Worker("Sam John",50000)
# Julie = Worker("Julie Andreas", 70000)
#
# print(Sam.lastName())
# print(Julie.lastName())
# print(Julie.pay)
# print(Sam.pay)
#
# print("Sam is going to get raise!!!!")
# Sam.giveRaise(.10)
# print(Sam.pay)
#

#pattern matching

# import re
#
# match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
# print(match.group(1))
#
# match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
# print(match.groups())
#
# #poping item from anywhere
#
# l =[1,2,'mi','lego',5,8,'yama']
# print(l)
# l.pop(2)
# print(l)
# l = ['x','y',2,10,'*',6,8,5]
# print(l)
# nl = []
# for i in l:
#     if i==10:
#         s = l.index(i)
#         l.pop(s)
#     elif i==5:
#         s = l.index(i)
#         l.pop(s)
#     else:
#         pass # nl.append(i)
# print(l)
#
# #Arbitory nesting

M = [[1, 2, 3],                 # A 3 × 3 matrix, as nested lists
[4, 5, 6],                      # Code can span lines if bracketed
[7, 8, 9]]

print(M)
#
# col2 =[row[0] for row in M]
# print(col2)
# #
# col2 =[row[1] for row in M]
# print(col2)
# #
# col2 =[row[1]+1 for row in M]
# print(col2)
#
# col2=[row[1] for row in M if row[1] % 2 == 0] # Filter out odd items
# print(col2)
# #
# diag = [M[i][i] for i in [0, 1, 2]]     # Collect a diagonal from matrix
# print(diag)
#
# doubles = [c * 2 for c in 'spam'] # Repeat characters in a string
# print(doubles)
# #
# doubles = [ord(c) for c in 'spam'] # find ord of every char
# print(doubles)
#
# G = (sum(row) for row in M) # Create a generator of row sums
# print(next(G))
# print(next(G))
# print(next(G))

# print(list(map(sum, M)))   # Map sum over items in M
#Home work
# print({sum(row) for row in M}) # Create a set of row sums
#
# print({i : sum(M[i]) for i in range(3)}) # Creates key/value table of row sums
#
# print([ord(x) for x in 'spaam'])    # List of character ordinals
#
# print({ord(x) for x in 'spaam'})     # Sets remove duplicates
#
# print({x: ord(x) for x in 'spaam'})  # Dictionary keys are unique
#
# #mapping opoerations
#
# D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# print(D['food'])                     # Fetch value of key 'food'
#
# D['quantity'] += 1 # Add 1 to 'quantity' value
# print(D)
#
#
#
# D = {}
# D['name'] = 'Bob' # Create keys by assignment
# D['job'] = 'dev'
# D['age'] = 40
# print(D)
# print(D['job'])
#
# # nesting
#
# rec = {'name': {'first': 'Bob', 'last': 'Smith'},
# 'job': ['dev', 'mgr'],
# 'age': 40.5}
# print(rec)
# print(rec['name'])                   # 'name' is a nested dictionary
# print(rec['name']['last'])           # Index the nested dictionary
# print(rec['job'])                    # 'job' is a nested list
#
# print(rec['job'][-1])                # Index the nested list
#
# rec['job'].append('janitor')         # Expand Bob's job description in-place
# print(rec)
#
# print('%s, eggs, and %s' % ('spam', 'SPAM!')) # Formatting expression (all ver)
#
# print('{0}, eggs, and {1}'.format('spam', 'SPAM!')) # Formatting expression (in 2.x & 3.x)
#


#File opoerations
# f = open('data.html', 'w')
# f.write('<html><Header><p>Hello this is a web page!! <p></Header></html>')
# f.write('Hello, its Not cool today\n')
# f.close()
# f = open('data.py')
# text= f.read()
# print(text)
# print(text.split())
# print(dir(f))
# print(f.__class__)
# print(help(f.seek))
# data = open('data.py', 'rb').read()
# print(data)


#creating Sets
# x = set('SPAM')
# print(x)
# y = {'H','A','M'}
# print(x,y)
#
# print({x ** 2 for x in [1, 2, 3, 4]}) # Set comprehensions in 3.0

# desimals
#
# print(1/3)
#
# print(2/3+1/2)

# import decimal                      # Decimals: fixed precision
#
# # d = decimal.Decimal('3.141')
# # print(d+1)
# decimal.getcontext().prec = 4
# print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# from fractions import Fraction # Fractions: numerator+denominator
#
# f = Fraction(2,3)
# print(f+1)
#
# print(f + Fraction(1, 2))
#
# print((2/3)+1)
# print(5/3)
#sort Tuple
# t = ('A','a','b','c','C','B','D','z','Y','48')
# t1 =(1,2,5,99,87,56,34,67)
# print(type(t))
# print("Tuple: ",t)
# print(t1)
#
# d = list(t)
# d1 = list(t1)
# print(d)
# print(d1)
# # print("Converted to list: ",d)
# d.sort()
# d1.sort()
# print("Sorted list: ",d)
# print("Sorted list: ",d1)
# t = d
# t1= d1
#
# print(t)
# print(t1)
#def classes excersise:

# class Worker:
#     def __init__(self, name, pay): # Initialize when created
#         self.name = name # self is the new object
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1] # Split string on blanks
#
#     def giveRaise(self, percent):
#         self.pay *= (1.0 + percent) # Update pay in-place
#
# Sam = Worker("Sam John",50000)
# Julie = Worker("Julie Andreas", 70000)
#
# print(Sam.lastName())
# print(Julie.pay)
#
# print(Sam.pay)
# print("Sam is going to get raise!!!!")
# Sam.giveRaise(.10)
# print(Sam.pay)

#importing math

# import math
#
# print(math.pi, math.e)
#
# print(math.sqrt(9))
#
# print(pow(2,2))

#getting random numbers

# import random
# print(random.random())
# print(random.randint(1,10))
#
# print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))

#more on fractions

# from fractions import Fraction
# # print(Fraction('0.25'))
# # print(Fraction('1.25'))
#
# print((2.5).as_integer_ratio())
# print(Fraction.from_float(1.75))


# for item in set('abc'): print(item * 3)

#
# S = set([1,2,3])
# print(S)

# print(S | [3, 4])
#
# print(S.union([3, 4]))
#
# print(S|set([3,4]))

# print(S.intersection((1, 3, 5)))
# print(S.issubset(range(-5, 5)))

#example of shared objects
#
# l1 = [1,2,3]
# l2 = l1
# print(l1)
# print(l2)
# l1[0]=25
#
# print(l1)
# print(l2)

#
# l3 = [2,4,6]
# l4 = l3[:]              #make a copy of l3
# print(l3)
# print(l4)
# l3[0]=55
# print(l3)
# print(l4)
# import sys
#
# print(sys.getrefcount(1))           # pointers to this shared piece of memory
#
#
# S = "xoneAutomation"
# print(S.isdigit())
# a= map(ord, S)
# print(a)
#
# def common_letters(string_one, string_two):
#   common_lst = []
#   for char1 in string_one:
#     for char2 in string_two:
#       if char1 == char2:
#         common_lst.append(char1)
#   return common_lst
#
# print(common_letters('Pune', 'Punjab'))

#string manipulation
#
# import sys
#
# print('My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
#
# print('My {config[spam]} runs {sys.platform}'.format(sys=sys,config={'spam': 'laptop'}))
#
# somelist = list('SPAM')
# print('first={0[0]}, third={0[2]}'.format(somelist))
# print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
#
#
# parts = somelist[0], somelist[-1], somelist[1:3]
# print('first={0}, last={1}, middle={2}'.format(*parts))
#
# print('{0:10} = {1:10}'.format('spam', 123.4567))


#dixtionary

# D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
# print(D)


#file opoerations





# total = 0
# items = str(total)
# report = "T"
#
#
# def adding_report(report):
#
#     while True:
#         var1 = input("Integer or 'Q'")
#         if var1.isdigit():
#             print("Yo")
#         else:
#             break
#
# print(adding_report(report))
