# n = int(input("How many items to output = "))
# list1 = []
# for i in range(n):
#     x = int(input('x = '))
#     list1.append(x)

# print(list1)

# list1 = []
# for i in range(int(input("How many items to output = "))):
#     list1.append(int(input('x = ')))
# print(list1)

# list1 = [{"V": "S001"}, {"V": "S002"},
#          {"VI": "S001"}, {"VI": "S005"},
#          {"VII": " S005 "}, {" V ":" S009 "},
#          {" VIII":" S007 "}]
# set1 = set()
# for i in list1:
#     for v in i.values():
#         set1.add(v)
# print(set1)

# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11


# min_value = k - list_1[0]
# for i in list_1:
#     if k - i < 0:
#         if i - k < min_value:
#             min_value = i-k
#             min = i
#     else:
#         if k - i < min_value:
#             min_value = k-i
#             min = i
# print(min)

list_1 = [(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'] : 1),(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'] : 1),(['D', 'G'] : 2),(['B', 'C', 'M', 'P']: 3),(['F', 'H', 'V', 'W', 'Y'] : 4),(['K'] : 5), (['J', 'X'] : 8),(['Q', 'Z'] : 10),(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'] : 1),(['Д', 'К', 'Л', 'М', 'П', 'У'] : 2),(['Б', 'Г', 'Ё', 'Ь', 'Я'] : 3),(['Й', 'Ы'] : 4),(['Ж', 'З', 'Х', 'Ц', 'Ч'] : 5),(['Ш', 'Э', 'Ю'] : 5),(['Ф', 'Щ', 'Ъ'] : 10),]

k = 'ноутбук'

for i in list_1:
    for (k,v) in list_1.keys():
        print (k,v)

my_list = [
    1, 2, 3,
    4, 5, 6,
]