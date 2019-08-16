# #string examples
# print('spam emails')  # single quotes
#
# #example of escape characters
# #\n \t '\' called as a escape character
#
# #print('doesn't') #will not work
# print('doesn\'t') #this will run
# print("doesn't") #or use double quotes instead
#
# print('"Yes," they said.')
# print("\"Yes,\" they said.")
#
# print('"Isn\'t," they said.')
#
# s ='First line.\nSecond line.'
#
# print(s)
#
# #raw string format  using r
#
# print('c:\some_user\nilesh_kumar') # here \n means newline!
#
# #print('C:\user\nilesh_kumar') # this will give error
#
# print(r'C:\user\nilesh_kumar') # r placed before quotes
#
#
#
# #here \ prevents eol (initial new lines get removed)
#
# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
#
# #Strings can be concatenated (glued together) with the + operator, and repeated with *
#
# # 3 times 'un', followed by 'ium'
#
# print(3 * 'un' + 'ium')
#
# #Two or more string literals (i.e. the ones enclosed between quotes)
# #next to each other are automatically concatenated.
#
# print("py" "thon")
#
# prefix = 'Py'
# #print(prefix 'thon') # can't concatenate a variable and a string literal use + sign instead
#
# print(prefix+'thon')
#
# #string can be stored as indexes
#
s = "Sachin"
#
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# #print(s[6])
#
# #Indices may also be negative numbers, to start counting from the right
#
# print('--'*5)
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# print(s[-6])
#
# #In addition to indexing, slicing is also supported
#
# print(s[0:4])
#
# print(s[0:])
# print(s[:4])
#
# #out of index error
#
# #print(s[55])
#
# #understanding index
#
#
# print("""\
#         +---+---+---+---+---+---+
#         | P | y | t | h | o | n |
#         +---+---+---+---+---+---+
#         0   1   2   3   4   5   6
#         -6  -5  -4  -3  -2  -1
# """)

# #Python strings cannot be changed — they are immutable.
# s[0]='A'
# print(s)


# #but we can create new string using existing string
#
# a = 'J_'+s
#
# print(a)
# #or
# print('J_'+s)


# #len function
#
# l = 'supercalifragilisticexpialidocious'
#
# print(len(l))
#
# #str.capitalize() first letter capital
# print(str.capitalize(l))
# print(l.capitalize())
#
# #str.casefold() lowercase aggrassion
# j = 'PYTHONß'
#
# print(str.casefold(j))
# print(j.casefold())
#
# #we can use lower() as well but it is less agressive
#
# j = 'PYTHONß'
#
# print(str.lower(j))
# print(j.lower())
#
# #str.center(width[, fillchar])
# print(l.center(40, 'a'))
