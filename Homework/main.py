a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
command = input('Введите действие: ')
if command == '+':
    print('Результат сложения двух  чисел равен: ', a + b)
elif command == '-':
    sl = input('Произвести вычитание первого числа из второго ? no/yes')
    if sl == 'yes':
        print('Результат вычитания двух чисел равен: ', a - b)
    elif sl == 'no':
        print('Результат вычитания двух чисел равен: ', b - a)
elif command == '*':
    print('Результат умножения двух чисел равен: ', a * b)
elif command == '/':
    delenie = input('Произвести деление первго числа на второе? no/yes')
    if delenie == 'yes':
        print('Результат деления первого числа на второе: ', a / b)
    elif delenie == 'no':
        print('Результат деления второго числа на первое : ', b / a)