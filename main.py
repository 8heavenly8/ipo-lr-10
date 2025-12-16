from collision import tasks


list1 = []
list2 = []
list_result = []
check = True
try:
    list1, list2 = tasks.create_rectangle(list1, list2)
    rectangles = [list1,list2]
    area = tasks.intersectionAreaRect(list1,list2)
    all_area = tasks.intersectionAreaMultiRect(rectangles)
except:
    print(f"Ошибка ввода!")
    check = False


if check != False:
    print(f"пересечение прямоугольников: {tasks.isCollisionRect(list1,list2)}")
    print(f"площадь пересечения: {area}")
    print(f"уникальная площадь пересеченя:{all_area}")

