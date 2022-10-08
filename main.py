try:
    while True:
        line = int(input("Введіть числа: "))
        if line > 0:
            print("Number is positive")
        if line < 0:
            print("Number is negative")
        if line == 0:
            print("Number is equal to zero")
        if line == 7:
            print("Good bye!")
            break


except Exception as ex:
    print("Erorr: ", ex)
finally:
    print(" Завдання виконано.")