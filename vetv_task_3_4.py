'''
#Функция range(24) перебирает все числа от 0 до 24 и по очереди передаёт их в тело цикла в переменной current_hour («текущее время»).
#Научите Анфису желать вам доброго утра, если в переменной current_hour записано значение меньше 12.

#Расширьте код из прошлой задачи. Если на часах полдень или больше — пусть Анфиса скажет: 'Добрый день!'
'''
for current_hour in range(24):
    if  current_hour < 12:
        print('Доброе утро!')
    else:
        current_hour >= 12
        print('Добрый день!')
