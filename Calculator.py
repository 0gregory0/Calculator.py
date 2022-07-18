#Welcome Message
print('Welcome to the Calculator App. Key in your expression parameters below.')

#Input prompt
while True:
    operation = input('''Which operation would you like to perform?
    For addition, press +
    For subtraction, press -
    For multiplication, press *
    For division, press /
    For exponentiation, press **
    For integer division, press //
    For modulo, press %
    Enter operation here:  ''')
    value_1 = float(input('Enter your first value: '))
    value_2 = float(input('Enter your second value: '))


    if type(value_1) is not (float or int):
        print('Invalid input. Please enter a real number.')
        retry_1 = input('Would you like to try again? Y or N: ')
        if retry_1 == 'N':
            break

    elif type(value_2) is not (float or int):
        print('Invalid input. Please enter a real number.')
        retry_2 = input('Would you like to try again? Y or N: ')
        if retry_2 == 'N':
            break

    if operation == '+':
        print(value_1, operation, value_2, '= ')
        computation = value_1 + value_2

    elif operation == '-':
        print(value_1, operation, value_2, '= ')
        computation = value_1 - value_2

    elif operation == '*':
        print(value_1, operation, value_2, '= ')
        computation = value_1 * value_2

    elif operation == '/':
        print(value_1, operation, value_2, '= ')
        computation = value_1 / value_2

    elif operation == '**':
        print(value_1, operation, value_2, '= ')
        computation = value_1 ** value_2

    elif operation == '//':
        print(value_1, operation, value_2, '= ')
        computation = value_1 // value_2

    elif operation == '%':
        print(value_1, operation, value_2, '= ')
        computation = value_1 % value_2

    print(computation)


    retry_4 = input('Do more calculation? Y or N: ')
    if retry_4 == 'N':
        break
