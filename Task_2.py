'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить
на своем месте.
Для заполнения списка элементов необходимо использовать
функцию input().
'''

element_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)