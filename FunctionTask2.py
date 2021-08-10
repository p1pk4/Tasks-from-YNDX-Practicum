'''
#Напишите цикл, в котором функция print_friends_count() вызывается c аргументами от 1 до 10.
def print_friends_count(friends_count):
    remainder = friends_count % 10
    if friends_count == 0:
        print('У тебя нет друзей')
    elif remainder == 0 or remainder >= 5 or (10 <= friends_count <= 19):
        print('У тебя', friends_count, 'друзей')
    elif remainder == 1:
        print('У тебя', friends_count, 'друг')
    else:
        print('У тебя', friends_count, 'друга')

for friends_count in range(1,11):
    print_friends_count(friends_count)
'''

def keys (key_from_home):
    any_key = key_from_home + 20
    if key_from_home >= 1:
        print('на связке', key_from_home, 'ключей')
    else:
        print('нет ключей')
for key_from_home in range(1, 20, 3):
    keys(key_from_home)
