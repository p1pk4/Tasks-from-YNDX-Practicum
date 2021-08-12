def my1():
    my_list_1 = [1, 3, 5, 7, 8]
    #print(my_list_1[2])
    return my_list_1
def my2():
    my_list_2 = ['f', 'd', 'ds', 'da']
    return my_list_2 #len(my_list_2)

def my3():
    my_list_3 = [12, 35, 65232, 3434, 24, 56, 768, 897, 21, -1, 0, -423, 645]
    #print(my_list_3)
    return my_list_3 #+ [2.2]

'''
Функция c параметром 'param' принимает аргумент (в данном случае это my3(нижний 'print(count_list(my3()))'))
и проходится циклом по ней, возвращая значение. И дальше принт уже выводит функцию на экран с аргументом.
Print будет == 13
'''
def count_list(param):
    count = 0
    for i in param:
        count +=1
    return count
print(count_list(my1()))
print(count_list(my2()))
print(count_list(my3()))
