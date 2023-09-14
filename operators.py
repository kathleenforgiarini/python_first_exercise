
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


