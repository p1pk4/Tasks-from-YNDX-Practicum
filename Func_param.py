# Добавьте вторым аргументом переменную name.
# Её значением по умолчанию должна быть пустая строка
def print_friends_count(friends_count, name=''):
    if friends_count == 1:
        text = '1 друг'
    elif 2 <= friends_count <= 4:
        text = str(friends_count) + ' друга'
    elif friends_count >= 5:
        text = str(friends_count) + ' друзей'
#Проверка, что содержит переменная name
    if name == '':
        #print('У тебя ' + str(friends_count) + text) в функции в переменную text УЖЕ передано сообщение о количестве друзей(friends_count).
         print('У тебя ' + text)
    else:
        #print(name + ', у тебя ' + str(friends_count) + text)
        print(name + ', у тебя ' + text)

    # и в зависимости от её значения напечатайте нужные варианты фразы

# дальше код не меняйте
print_friends_count(3, 'Артём')
print_friends_count(friends_count=7, name='Марина')
print_friends_count(6)
print_friends_count(4, name='Настя')
