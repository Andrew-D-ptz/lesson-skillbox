def addition(a, b):
    c = a + b
    print(f'{a} + {b} = {c}')

def difference(a, b):
    c = a - b
    print(f'{a} - {b} = {c}')

def multiplication(a, b):
    c = a * b
    print(f'{a} * {b} = {c}')

def division(a, b):
    c = a / b
    print(f'{a} / {b} = {c}')

while True:
    operation = input('Выберите операцию: ')

    while (operation != '+') and (operation != '-') and (operation != '*') and (operation != '/'):
        print('Ошибка ввода: такой опреции не существует. Введите +, -, *, /')
        operation = input('Выберите операцию: ')

    operands = int(input('Введите количество операндов: '))

    for i in range(1, operands + 1):
        number = float(input(f'Введите операнд {i}: '))
        if i == 1:
            result = number
            result_str = str(number)
            continue
        else:
            if operation == '+':
                result += number
                result_str += ' + ' + str(number)
            elif operation == '-':
                result -= number
                result_str += ' - ' + str(number)
            elif operation == '*':
                result *= number
                result_str += ' * ' + str(number)
            elif operation == '/':
                result /= number
                result_str += ' / ' + str(number)

    print(result_str, '=', result)