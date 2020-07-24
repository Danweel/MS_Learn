#user prompt
fahrenheit = input("What is the temperature in fahrenheit? ")


try:
    int(fahrenheit)

except:
    float(fahrenheit)

    

if int(fahrenheit) is False:
    print(int(round(fahrenheit)) - 32) * 5/9
    
else: c = (fahrenheit - 32) * 5/9
print(c)


'''
To check if o is an instance of str or any subclass of str, use isinstance (this would be the "canonical" way):

if isinstance(o, str):
To check if the type of o is exactly str (exclude subclasses):

if type(o) is str:
The following also works, and can be useful in some cases:

if issubclass(type(o), str):
See Built-in Functions in the Python Library Reference for relevant information.

'''


'''
fahrenheit = input('What is the temperature in Fahrenheit?  ')

if fahrenheit.isnumeric() == False:
    print('Input is not a number.')
    exit()

fahrenheit = int(fahrenheit)

celsius = int((fahrenheit - 32) * 5/9)
print('Temperature in celsius is ' + str(celsius))
'''