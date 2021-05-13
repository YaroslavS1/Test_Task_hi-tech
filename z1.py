# 1. Создайте список (list) и массив (ndarray), содержащие числа от 0 до 100 000 000.
# 2. Напишите функцию, которая вычисляет сумму всех элементов массива, используя цикл for.
# 3. Замерьте: время выполнения этой функции на списке и на массиве, время выполнения функции sum() на списке и на массиве, время выполнения функции numpy.sum() на списке и на массиве.
# ----------------------------------------------------
# время выполнения этой функции на списке и на массиве
# время выполнения функции sum() на списке и на массиве
# время выполнения функции numpy.sum() на списке и на массиве.
#-----------------------------------------------------


import numpy as np
import time



def f_list():
    """Cписок (list), содержащий числа от 0 до 100 000 000."""
    a = list(range(100000000+1))
    return a

def f_array():
    """Массив (ndarray), содержащий числа от 0 до 100 000 000."""
    a = np.arange(0, 100000000+1, 1)
    return a

def mySum(a):
    """Сумма всех элементов списка/массива"""
    s = 0
    for i in a:
        s += i
    # print(s)
    return s
    
def mete_time_f(f, f_s):
    a = f()
    start = time.process_time()
    f_s(a)
    elapsed = (time.process_time() - start)
    return elapsed

print('{:15}|{:20}'.format('mySum(list)', mete_time_f(f_list, mySum)))
print('{:15}|{:20}'.format('mySum(ndarray)', mete_time_f(f_array, mySum)))
print('{:15}|{:20}'.format('-'*15, '-'*20))
print('{:15}|{:20}'.format('sum(list)', mete_time_f(f_list, sum)))
print('{:15}|{:20}'.format('sum(ndarray)', mete_time_f(f_array, sum)))
print('{:15}|{:20}'.format('-'*15, '-'*20))
print('{:15}|{:20}'.format('np.sum(list)', mete_time_f(f_list, np.sum)))
print('{:15}|{:20}'.format('np.sum(ndarray)', mete_time_f(f_array, np.sum)))

