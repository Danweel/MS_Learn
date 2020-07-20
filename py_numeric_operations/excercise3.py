#demonstration of operations
first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value 

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))



#controlling order of operations with parentheses
print(3 + 4 * 5)
print((3 + 4) * 5)



#demonstration that dividing two int makes a float
first_value = 5
second_value = 4

quotient = first_value / second_value

print(type(quotient))
print(quotient)



#ways to round or truncate float to int
pi = 3.14
print(type(pi))
print(int(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))


#controlling the decimal place python rounds to
first_value = round(7.654321, 2)
print(first_value)

second_value = round(9.87654, 3)
print(second_value)


