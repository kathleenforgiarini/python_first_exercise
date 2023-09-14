
"""
    Topic: Numbers - Operators
    Date: 12 Sep 2023
    Author: Kathleen
"""

a = 21
b = 10

print ("+++++++++++++++++++++++++ Math Operators")

print ("21 + 10 = ", a + b)

print ("21 * 10 = ", a * b)

print ("21 - 10 = ", a - b)

print ("21 / 10 = ", a / b)

print ("21 // 10 = ", a // b) ### floor division, round the result down to the nearest whole number or integer

print ("21 ** 10 = ", a ** b) ### 21^10

print ("21 % 10 = ", a % b)


print ("\n\n+++++++++++++++++++++++++ Comparison Operators")
print ("21 == 10", a == b)
print ("21 != 10", a != b)
print ("21 <= 10", a <= b)
print ("21 < 10", a < b)
print ("21 >= 10", a >= b)
print ("21 > 10", a > b)

"""
print (bool(True))
print (bool(a))
print (bool(-10.5))
print (bool(" "))
print (bool(""))
print (bool(0))
print (bool(None))
print (bool(False))
"""

print ("\n\n+++++++++++++++++++++++++ Assignment Operators")
a += b ### a = 21 + 10
print ("21 + 10 = ", a)
a *= b ### a = 31 * 10
print ("31 * 10 = ", a)
a /= b ### a = 310 / 10
print ("310 / 10 = ", a)
a //= b ### a = 31 // 10
print ("31 // 10 = ", a)
a **= b ### a = 3 ** 10
print ("3 ** 10 = ", a)
a %= b ### a = 59049.0 % 10
print ("59049.0 % 10 = ", a)
a -= b ### a = 9 - 10
print ("9 - 10 = ", a)


### ====================== Logical Operators

x = True
y = False

print("\n++++++++++++++++++++ Logical AND")

print ("False and False: ", y and y)
print ("False and True: ", y and x)
print ("True and False: ", x and y)
print ("True and True: ", x and x)

print("\n++++++++++++++++++++ Logical OR")

print ("False or False: ", y or y)
print ("False or True: ", y or x)
print ("True or False: ", x or y)
print ("True or True: ", x or x)

print("\n++++++++++++++++++++ Logical NOT")

print ("NOT True: ", not x)
print ("NOT False: ", not y)

print("\n++++++++++++++++++++ Logical OR")

print ("False or False: ", y or y)
print ("False or True: ", y or x)
print ("True or False: ", x or y)
print ("True or True: ", x or x)

print("\n\n++++++++++++++++++++ Bitwise Operator")

a = 60      ### 60 = 0011 1100
b = 13      ### 13 = 0000 1101
c = 0

c = a & b   ### 12 = 0000 1100
print ("60 & 13: ", c)

c = a | b   ### 61 = 0011 1101
print ("60 | 13: ", c)

c = ~a   ### -61 = 1100 0011
print ("~60: ", c)

c = a << 2 ### 60 = 0011 1100 --> 0111 1000 (120) --> 1111 0000 (240) ### multiply by 2 twice
print ("60 << 2: ", c)

c = a >> 2 ### 60 = 0011 1100 --> 0001 1110 (30) --> 0000 1111 (15) ### divide by 2 twice
print ("60 >> 2: ", c)


print("\n\n++++++++++++++++++++ Membership Operator")

l1 = [1,2,3,10,40]

print (10 in l1)
print ("Hi" in l1)
print (20 in l1)
print (20 not in l1)


print("\n\n++++++++++++++++++++ Identity Operator")

### immutable objects
x1 = 5
y1 = 5

print ("5 == 5:", x1 == y1)
print ("5 is 5:", x1 is y1)

x2 = "Hi"
y2 = "Hi"

print ("Hi == Hi:", x2 == y2)
print ("Hi is Hi:", x2 is y2)

### mutable objects, they have different memory addresses, because its value can change anytime
x3 = [1,2,3]
y3 = [1,2,3]

print ("[1,2,3] == [1,2,3]:", x3 == y3)
print ("[1,2,3] is [1,2,3]:", x3 is y3)


