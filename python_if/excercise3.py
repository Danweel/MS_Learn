
'''
medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions)
'''


name = 'World'
message = f'Hello, {name}.'
print(message)

count = 10
value = 3.14
message = f'Count to {count}.  Multiply by {value}.'
print(message)