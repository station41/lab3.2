import random

R = 5.0
print(" X         Y        Результат")
print("------------------------------")

# цикл на 10 выстрелов
for i in range(10):
    # генерируем случайные координаты
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)

    # сначала предполагаем, что мы НЕ попали
    flag = 0

    # если точка попала в правую или левую фигуру:
    in_right = (x >= 0) and (x <= R) and (y <= 0) and (y >= -R) and ((x - R) ** 2 + (y + R) ** 2 >= R ** 2)
    in_left = (x >= -R) and (x <= 0) and (y >= 0) and (y <= R) and ((x + R) ** 2 + (y - R) ** 2 >= R ** 2)

    if in_right or in_left:
        flag = 1

        # проверяем, поднят ли флаг, и делаем вывод
    print(f"{x:8.2f} | {y:8.2f} | ", end="")
    if flag == 1:
        print("Попадает")
    else:
        print("Не попадает")