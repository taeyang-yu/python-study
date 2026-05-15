#리스트 가져만 오기

#[:]
a = [1, 2, 3]
b = a[:]

a[1] = 130

print(a)
print(b)

#copy
from copy import copy
b = copy(a)
print(b)