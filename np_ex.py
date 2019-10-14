import numpy as np

a = np.array([1,2,3,4])

print(a.dtype.name)
print(a.ndim)
print(a.shape)

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b.ndim)
print(b.shape)
z = np.add(a,b)
x = np.dot()
print(z.dtype)

# c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(c.ndim)
# print(c.shape)
#
# d = np.arange(15).reshape(3, 5)
# print(d)
# # print()
# print(d.ndim)
# print(d.shape)