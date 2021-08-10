'''
Task1.
На основе заготовленного кода напишите функцию print_friends_count() для вывода количества друзей. Аргументом сделайте friends_count.
Вызовите эту функцию не менее трёх раз. Она должна корректно склонять фразу о количестве друзей при значении от 0 до 99.
'''
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
print_friends_count(0)
print_friends_count(1)
print_friends_count(2)
print_friends_count(5)
