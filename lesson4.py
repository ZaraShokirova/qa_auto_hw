import math
import random
from decimal import Decimal
#
#
# a = 0.5
#
# print(a)
#
# import math
#
# a = 0.1 + 0.2
# print(a)
# print(math.pi)
#
# random.seed('some word')
#
# print('-----------------')
#
# print(random.randint(0, 100))
# print(random.randint(0, 100))
# print(random.randint(0, 100))
#
# print('-----------------')
#
# print(round(1.222222, 2))

# строки
# a = 'hello'
# b = 'World'
# print(a + ',' + b + '!')
# print('{a}, {b}'.format(a=a, b=b))
# print(f'{a}, {b}!')
#
# url_temple = 'http://www.python.org {}'
#
# users_url = url_temple.format('users')
# groups_url = url_temple.format('groups')

# Делаем списки
#
# l = [1, 2, 3, 'a', 'b', 'c', [4, 5, 6]]
#
# print(l[0])
# print(l[-1])
#
# print(l[-1][0])
# print(l[::-1])
#
# # функции списков
#
# l.append('zara')
# l.extend(['zara' 'zarina shoki'])
# len(l)
#
# l[0] = 200
#
# print(l)


# множества
#
# s1 = {1,2,3,4,5,5,5,5,5}
# s2 = {1, 2, 5, 5}
# print(s1)
# print(s2)
#
# s1.intersection(s2)
# print(list(set([1,2,3,4,5,5,5,5,5])))


# словари

# d = {'key': 'value',
#      'anouther': 'anouther value'
# }
#
# user1 = {
#     'name': 'Zara',
#     'age': 30,
# }
#
#
# user2 = {
#     'name': 'Milla',
#     'age': 35,
# }
#
# users = {
#     25: user1,
#     42: user2
# }
#
# print(users[42])
# print(user1['name'])
# print(user2['name'])
#
# users[55] = {'name': 'Bubu', 'age': 13}
#
# # Функции словари
#
# users.items()
# users.values()
# users.keys()
#
# # print(users[50])
# print(users.get(50, {'name': 'default user'}))
# print(users.get(25, {'name': 'default user'}))

# b = bool
#
# t = True
# f = False
# n = None
#
# if True:
#     print('Я выполняюсь')
#
# if False:
#     print('Я никогда не выполняюсь')
#
# code = 200
#
# if 200 <= code < 400:
#     print('проверка прошла успешно')
# elif 400 <= code < 600:
#     print('проверка не прошла ')
# else:
#     print('непонятный код ответа')

# user_list = []
# if user_list == []
#     pass
#
# items_count = 0
# if items_count:
#
# if 'abc' == ''
#
# if 'abc':

# print(bool(100))
# print(bool(-100))
# print(bool(0))
#
#
# print(bool('abc'))
# print(bool(''))
#
# print(bool([]))
# print(bool([1, 2, 3]))
# print(bool([False]))


required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number:
    user_number = random.randint(0, 10)
    print(f'Пользователь ввел число {user_number}')

