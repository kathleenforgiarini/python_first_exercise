
"""
    Topic: Numbers datatype
    Date: 12 Sep 2023
    Author: Kathleen
"""


print ("++++++++++++++++++++++ int data type")

age = 22
print (age)
print (type(age))
print (id(age))

print ("++++++++++++++++++++++ After modifying age")

age = 23
print (age)
print (type(age))
print (id(age))


print ("++++++++++++++++++++++ float data type")

price = 22.99
print (price)
print (type(price))
print (id(price))

print ("++++++++++++++++++++++ After modifying price")

price = 52.99
print (price)
print (type(price))
print (id(price))


print ("++++++++++++++++++++++ complex data type")

z = 10 + 20j
print (z)
print (type(z))
print (id(z))

print ("++++++++++++++++++++++ After modifying z")

z = 100.5 + 20j
print (z)
print (type(z))
print (id(z))


asking_price = input('Please enter your asking price: ')
print (asking_price)
print (type(asking_price))

#print (3 * asking_price) """Contatenate 3 times. Sum str with int is not allowed""" 

print ("++++++++++++++++++++++ Converting to int")
asking_price_int = int(asking_price)
print (asking_price)
print (type(asking_price))












