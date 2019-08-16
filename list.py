# #lists are a mutable type
#
# squares = [1, 4, 9, 16, 25]
# print(squares)
#
# #indexing & slicing  can be used
#
# print(squares[0])
# print(squares[1])
# print(squares[-4])
# print(squares[0:3])
#
#
# #concatenation
#
# print(squares + [36, 49, 64, 81, 100])
#
# cubes = [1,8,27,65,125]
# print(cubes)
#
# #65 is wrong in the sequance
#
# cubes[3]=64
# print(cubes)
# cubes.append(216)
# print(cubes)
# cubes.append(7**3)
# print(cubes)
#
# #assignment to slices is also possible
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# # replace some values
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
#
#
# # now remove them
#
# letters[2:5] = []
# print(letters)
#
# print(len(letters))
#
#possible to nest lists (list inside of a list)

a = ['a', 'b', 'c']
print(a)
n = [1, 2, 3]
print(n)
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
