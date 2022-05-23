# Напишите программу, которой на вход подается последовательность чисел через пробел,
# а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.
while  True:
    try:

        array = list(map(int,input('Введите числа через пробел:').split()))



        for i in range(len(array)):  # проходим по всему массиву
            idx_min = i  # сохраняем индекс предположительно минимального элемента
            for j in range(i, len(array)):
                if array[j] < array[idx_min]:
                    idx_min = j
            if i != idx_min:  # если индекс не совпадает с минимальным, меняем
                array[i], array[idx_min] = array[idx_min], array[i]
        print('отсортированный список чисел', array)
        if type(array) == list :
            break
        else:
            print('используйте числа')

    except ValueError as a:
        print(f'{a} - Ошибка "Необходимо ввести числа через пробел" ')



while True:
    try:

        element = int(input('Введите число для сравнения:'))


        if  array[0] <= element <= array[-1]:
            break
        else:
            print(f'введите число для сравнения в диапазоне от {array[0]} до {array[-1]} ')
    except ValueError as e:
        print(f'{e} - Ощибка " Необходимо ввести число"')


def binary_search(array, element, left, right):
    if left > right:
        return 'Отсутствует'
    middle = (right + left)//2
    if array[middle] == element and array[middle] >= element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle+1 , right)


print(binary_search(array,element,0,len(array)),f'- номер позиции элемента в списке {array} который меньше {element},\n' \
             'а следующий за ним больше или равен этому числу .')