try:
    sum = 0
    chisla = 0
    while chisla != 7:
        chisla = int(input("Введіть число: "))
        if chisla == 7:

            print("Сумма чисел -> ", sum)
            break
        else:
            sum += chisla




except Exception as ex:
    print("Erorr: ", ex)
finally:
    print(" Завдання виконано.")
