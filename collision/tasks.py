#задание 2

def isCorrectRect(list):
    if list[0][0] >= list[1][0] or list[0][1] >= list[1][1]:
        return False
    else:
        return True

    

#задание 3

def isCollisionRect(list1, list2):
    x1_left, y1_bottom = list1[0]
    x1_right, y1_top = list1[1]
    x2_left, y2_bottom = list2[0]
    x2_right, y2_top = list2[1]

    rect1_min_x, rect1_max_x = min(x1_left, x1_right), max(x1_left, x1_right)
    rect1_min_y, rect1_max_y = min(y1_bottom, y1_top), max(y1_bottom, y1_top)
    
    rect2_min_x, rect2_max_x = min(x2_left, x2_right), max(x2_left, x2_right)
    rect2_min_y, rect2_max_y = min(y2_bottom, y2_top), max(y2_bottom, y2_top)

    if rect1_min_x >= rect2_max_x or rect1_max_x <= rect2_min_x:
        return False

    if rect1_min_y >= rect2_max_y or rect1_max_y <= rect2_min_y:
        return False

    return True


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


def create_rectangle(list1, list2):
    for k in range(2):
        print(f"координаты для {k+1} прямооугольника")
        list_add = []
        for i  in range(2):
            print(f"\nВведите координаты для точки {i + 1}:")
            x_str = input(f"Введите X: ")
            y_str = input(f"Введите Y: ")
            try:
                x = int(x_str)
                y = int(y_str)
                list_add.append((x, y))
            except ValueError:
                print(f"Ошибка ввода! Координаты должны быть числами.")
                break

            if k == 0:
                list1 = list_add
            else:
                list2 = list_add

    if isCorrectRect(list1) == False or isCorrectRect(list2) == False:
        return print("прямоугольник некоректный")
    return list1,list2




def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0

    (first_x1, first_y1), (first_x2, first_y2) = rectangles[0]
    
    if first_x1 >= first_x2 or first_y1 >= first_y2:
        raise RectCorrectError(f"Некорректный прямоугольник: {rectangles[0]}")

    max_x1, max_y1 = first_x1, first_y1
    min_x2, min_y2 = first_x2, first_y2

    for rect in rectangles[1:]:
        (x1, y1), (x2, y2) = rect
        
        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError(f"Некорректный прямоугольник: {rect}")
        
        max_x1 = max(max_x1, x1)
        max_y1 = max(max_y1, y1)
        
        min_x2 = min(min_x2, x2)
        min_y2 = min(min_y2, y2)

    width = min_x2 - max_x1
    height = min_y2 - max_y1

    if width <= 0 or height <= 0:
        return 0

    return width * height

    