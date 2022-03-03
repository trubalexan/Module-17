# Этот файл создан для задания 17.9.1 по следующим требованиям:
#
# Напишите программу, которой на вход подается последовательность чисел через пробел,
# а также запрашивается у пользователя любое число.
#
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному
# в условии ввода данных.
#
# Далее программа работает по следующему алгоритму:
#
#     Преобразование введённой последовательности в список
#
#     Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#
#     Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
#     а следующий за ним больше или равен этому числу.
#
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
# Реализуйте его также отдельной функцией.
#
# Подсказка
#
# Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
# В этом случае необходимо вывести соответствующее сообщение


# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
import random


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return(array)

# Устанавливается номер позиции элемента алгоритмом двоичного поиска
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# Элемента нет в списке
# Устанавливается номер позиции после которой можно вставить элемент
def binary_search_no_element(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return left  # значит элемент отсутствует и берём левую границу

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search_no_element(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search_no_element(array, element, middle + 1, right)


if __name__ == '__main__':
    # Ввод данных
    raw_array = '2 3 1 4 6 5 9 8 7 23 44 56 79 97 12 31 65 88'
    # Альтернативный ввод списка
    # range_array = [i for i in range(1, 101)]  # 1,2,3,4,...
    # random.shuffle(range_array)
    # raw_array = ' '.join(map(str, range_array))


    num = input("\nInput any integer number and press 'Enter': ")
    # check the correct input
    while num.isdigit() is False:
        num = input("\nError, should be an integer number"
                    "\nInput a new integer number and press 'Enter': ")
    num = int(num)

    # Преобразование введённой последовательности в список
    array_num = list(map(int, raw_array.split()))
    # print(array_num)

    # Сортировка списка
    sort_array = bubble_sort(array_num)
    # print(sort_array, len(sort_array))

    # Проверка нахождения места числа в пределах последовательности
    left_border = sort_array[0]
    right_border = sort_array[-1]
    if num < left_border or num > right_border:
        print('\nEntered number is out of range of the array. Ending algorithm.')
    elif num == left_border:
        print('\nThe number is equal to the first element in the array')
    elif num == right_border:
        print(f'\nThe number is equal to the last, {len(sort_array)} element in the array')
    else:
        index_of_num = binary_search(sort_array, num, 0, len(sort_array)-1)
        if index_of_num:
            # print(sort_array, index_of_num)
            print(f'\nThe number goes after {index_of_num} element in the array')
        else:
            no_num_index = binary_search_no_element(sort_array, num, 0, len(sort_array) - 1)
            print('\nThere is no such a number in the array, '
                  'but it fits between %d and %d element' % (no_num_index, no_num_index+1))

