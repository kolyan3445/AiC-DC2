#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.
#Натуральные числа, состоящие из цифр в порядке возрастания. Для каждого числа минимальную и максимальную цифру вывести прописью.
import re

dict = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}


def num_to_text(number):
    return dict[number]  # словарь


work_buffer = ''
numbers = []

with open("test1.txt") as file:  # открытие файла
    text = file.readline().split()
    if not text:
        print('Файл пуст, пожалуйста выберите другой файл')
    else:
        for i in text:
            r = re.fullmatch(r'0?1?2?3?4?5?6?7?8?9?', i)
            if r:
                numbers.append(i)

for i in numbers:
    ans = ' min = ' + num_to_text(i[0]) + ', max = ' + num_to_text(i[len(i) - 1])
    print(i + ' - ' + ans)