# Считываем три числа
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Проверяем условия
if first == second and first == third:
    print(3)  # Все числа равны
elif (first == second and first != third) or (first == third and first != second) or (second == third and second != first):
    print(2)  # Два числа равны
else:
    print(0)  # Ни одно число не равно другому