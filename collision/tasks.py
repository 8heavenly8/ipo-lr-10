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




'''list1 = []
list2 = []
list_result = []

print("координаты для первого прямооугольника")
for i in range(2):
    print(f"\nВведите координаты для точки {i + 1}:")
    x_str = input(f"Введите X: ")
    y_str = input(f"Введите Y: ")
    try:
        x = int(x_str)
        y = int(y_str)
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
        x2 = int(x_str2)
        y2 = int(y_str2)
        list2.append((x2, y2))
    except ValueError:
        print(f"Ошибка ввода! Координаты должны быть числами.")
        break
correct = True

for i in range(2):
    if isCorrectRect(list1) == False or isCorrectRect(list2) == False:
        print(f"{i+1} прямоугольник некоректный")
        correct = False
    else:
        correct = True


print(list1,list2)


if correct == True:
    print(isCollisionRect(list1,list2))
else:
    print("данные введены некоректно")'''


#задание 4
def intersectionAreaRect(list1,list2):
    if isCollisionRect(list1,list2) == False:
        return 0
    else:
        (x1_min, y1_min), (x1_max, y1_max) = list1
        (x2_min, y2_min), (x2_max, y2_max) = list2

        x_left = max(x1_min, x2_min)
        y_bottom = max(y1_min, y2_min)
        x_right = min(x1_max, x2_max)
        y_top = min(y1_max, y2_max)

        if x_right > x_left and y_top > y_bottom:
            width = x_right - x_left
            height = y_top - y_bottom
        return width * height



rectangle = []
list1 = []
list2 = []
list_result = []
def create_rectangle(list1, list2):
    for k in range(2):
        list = []
        print(f"координаты для {k} прямооугольника")
        for i in range(2):
            print(f"\nВведите координаты для точки {i + 1}:")
            x_str = input(f"Введите X: ")
            y_str = input(f"Введите Y: ")
            try:
                x = int(x_str)
                y = int(y_str)
                list.append((x, y))
            except ValueError:
                print(f"Ошибка ввода! Координаты должны быть числами.")
                break
            if i == 1:
                list1 = list
            else:
                list2 = list
    return list1,list2

list1, list2 = create_rectangle(list1, list2)
rectangle = [list1, list2]
print(rectangle)
correct = True



'''if isCorrectRect(list1) == True or isCorrectRect(list2) == True:
    print(list1,list2)
    print(intersectionAreaRect(list1,list2))
else:
    print("данные введены некоректно")'''



def intersectionAreaMultiRect():
    pass