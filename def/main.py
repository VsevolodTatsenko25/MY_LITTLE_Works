def say_hello(username, age):   ## username - параметр!
    '''Функция приветствует пользователя'''

    print(f'hello  {username}!')
    print(f'Your age is {age}!')
    print('-'* 20)

#say_hello('Valera', 20)    ##Valera - позиционный Аругмент!
#say_hello('Vsevolod', 30)
#say_hello('Vladimir', 40)
#say_hello(username='Alex', age=25)
#say_hello(age=15, username='Arnold')

def numbers_sum(num1=10,num2=20):
    print(num1 + num2)
    print('*' * 20)


numbers_sum(num1=18,num2=232)
numbers_sum(num1=1012,num2=2032)
numbers_sum(num1=1054,num2=2032)
