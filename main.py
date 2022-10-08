try:
    chisla = int(input("Введіть число: "))



except Exception as ex:
    print("Erorr: ", ex)
finally:
    print(" Завдання виконано.")