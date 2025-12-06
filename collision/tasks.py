#задание 2

def isCorrectRect(list):
    if list[0][0] >= list[1][0] or list[0][1] >= list[1][1]:
        return False
    else:
        return True


'''list = []
for i in range(2):
    print(f"\nВведите координаты для точки {i + 1}:")
    x_str = input(f"Введите X: ")
    y_str = input(f"Введите Y: ")
    try:
        x = float(x_str)
        y = float(y_str)
        list.append((x, y))
    except ValueError:
        print(f"Ошибка ввода! Координаты должны быть числами.")
        break

if len(list) != 0:
    print(isCorrectRect(list))'''
    

#задание 3

def isCollisionRect(list1, list2):
    x1_left, y1_bottom = list1[0]
    x1_right, y1_top = list1[1]

    x2_left, y2_bottom = list2[0]
    x2_right, y2_top = list2[1]

    if x1_left >= x2_right or x1_right <= x2_left:
        return False

    if y1_bottom >= y2_top or y1_top <= y2_bottom:
        return False

    return True




list1 = []
list2 = []
list_result = []

print("координаты для первого прямооугольника")
for i in range(2):
    print(f"\nВведите координаты для точки {i + 1}:")
    x_str = input(f"Введите X: ")
    y_str = input(f"Введите Y: ")
    try:
        x = float(x_str)
        y = float(y_str)
        list1.append((x, y))
    except ValueError:
        print(f"Ошибка ввода! Координаты должны быть числами.")
        break


print(' ')
print("координаты для второго прямооугольника")
for i in range(2):
    print(f"\nВведите координаты для точки {i + 1}:")
    x_str2 = input(f"Введите X: ")
    y_str2 = input(f"Введите Y: ")
    try:
        x2 = float(x_str2)
        y2 = float(y_str2)
        list2.append((x2, y2))
    except ValueError:
        print(f"Ошибка ввода! Координаты должны быть числами.")
        break
correct = True

for i in range(2):
    break
    if isCorrectRect(list[i]) == False:
        print(f"{i+1} прямоугольник некоректный")
        correct = False
    else:
        correct = True
print(list1,list2)
if correct == True:
    print(isCollisionRect(list1,list2))
