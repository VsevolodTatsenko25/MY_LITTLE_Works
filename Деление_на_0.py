a=int(input())
b=int(input())
if b != 0:
    print(a/b)
else:
    print('Деление невозможно !')
    b=int(input('Введите число не равное 0 ! '))
    if b == 0:
        print('Вы не справились с заданием! ')
    else:
        print(a/b)

