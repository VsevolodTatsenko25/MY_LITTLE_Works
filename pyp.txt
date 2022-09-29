otchislen = 0
otlichnik = 0
begin = True
while begin:
    fam = input("Введите фамилию студента")
    name = input("Введите имя студента")
    mark1 = int(input("Введите оценку по базам данных "))
    mark2 = int(input("Введите оценку по программированию "))
    mark3 = int(input("Введите оценку по теиории информации"))
    if mark1 == 2 or mark2 == 2 or mark3 == 2:
        print(fam,"Отчислен")
        otchislen +=1
        command = input("Введите команду:")
    elif mark1 == 5 and mark2 == 5 and mark3 == 5:
        print(fam,"Круглый отличник")
        otlichnik += 1
        command = input("Введите команду:")
    elif (mark1 >2 and mark1 < 6) and (mark2 >2 and mark2 < 6) and (mark3 >2 and mark3 < 6):
        print("Оценки:", fam , mark1,mark2,mark3)
    if command == "otvet":
        run = False
        print("Отличники:",otlichnik)
        print("Отчислены:",otchislen)