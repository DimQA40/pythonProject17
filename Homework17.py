numbers = input("Введите последовательность целых чисел через пробел: ")
user_number = int(input("Введите любое целое число: "))

# 1. Преобразование введённой последовательности в список
numbers_list = list(map(int, numbers.split()))
# Формирование полного списка
numbers_all = numbers_list + [user_number]

# 2. Сортировка списка по возрастанию элементов в нем
def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

qsort(numbers_all, 0, len(numbers_list))
print(numbers_all)

#3. Установка номеров позиций до и после числа пользователя
def binary_search(array, min_user_num, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == min_user_num:
        if array[0] == min_user_num:
            return f'Нет меньшего числа:  {user_number} , индекс : {middle}'
        if array[-1] == min_user_num:
            return  f'Нет числа больше: {user_number} , индекс : {middle}'
        return f'Номер позиция до и после: {middle - 1} , {middle + 1}'
    elif min_user_num < array[middle]:
        return binary_search(array, min_user_num, left, middle - 1)
    else:
        return binary_search(array, min_user_num, middle + 1, right)

indexs = binary_search(numbers_all, user_number, 0, len(numbers_list))
print(indexs)