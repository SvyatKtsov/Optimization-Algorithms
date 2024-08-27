import random
import math as m
import numpy as np
import matplotlib.pyplot as plt
e_levi_13_f = 20 / 2047  # точність для ф-ції Леві 13
e_himmelblau_styblinskyTang_fitness_f = 10 / 1023

def levi_13_fitness_f(x_input_levi13, y_input_levi13):
    levi_13_fitness_f = []
    if not isinstance(x_input_levi13, list):
        x_input_levi13 = [x_input_levi13]
    if not isinstance(y_input_levi13, list):
        y_input_levi13 = [y_input_levi13]
    for each_x, each_y in zip(x_input_levi13, y_input_levi13):
        res = (m.sin(3 * m.pi * each_x)) ** 2 + (each_x - 1) ** 2 * (1 + (m.sin(3 * m.pi * each_y)) ** 2) + \
              (each_y - 1) ** 2 * (1 + (m.sin(2 * m.pi * each_y)) ** 2)
        levi_13_fitness_f.append(res)
    return levi_13_fitness_f

levi_13_fitness_f_x_input = np.arange(-10, 10 + e_levi_13_f, e_levi_13_f)
levi_13_fitness_f_y_input = np.arange(-10, 10 + e_levi_13_f, e_levi_13_f)
min_levi13 = min(levi_13_fitness_f(list(levi_13_fitness_f_x_input), list(levi_13_fitness_f_y_input)))

#########################################################################################################################
def styblinsky_tang_fitness_f(styblinskiy_tang_f_x_input):
    styblinsky_tang_fitness_f = []
    if isinstance(styblinskiy_tang_f_x_input, (int, float)):
        # якщо передано в аргументи лише одне число, то йде конвертація його у список для обробки
        styblinskiy_tang_f_x_input = [styblinskiy_tang_f_x_input]
    elif not isinstance(styblinskiy_tang_f_x_input, list):  # якщо аргумент - не список
        raise ValueError("...введене значення повинне бути або числом(int,float), або списком чисел")
    for each_x_stt in range(len(styblinskiy_tang_f_x_input)):
        res = 0
        for k in range(each_x_stt, len(styblinskiy_tang_f_x_input)):
            res += (styblinskiy_tang_f_x_input[k]) ** 4 - 16 * (styblinskiy_tang_f_x_input[k] ** 2) + 5 * \
                   styblinskiy_tang_f_x_input[k]
        res /= 2
        styblinsky_tang_fitness_f.append(res)
    return styblinsky_tang_fitness_f
#########################################################################################################################
def himmelblau_fitness_f(himmelblau_fitness_f_x_input,himmelblau_fitness_f_y_input):
    himmelblau_fitness_f = []
    if isinstance(himmelblau_fitness_f_x_input, (int, float)):
        himmelblau_fitness_f_x_input = [himmelblau_fitness_f_x_input]
    elif not isinstance(himmelblau_fitness_f_x_input, list):
        raise ValueError("...введене значення повинне бути або числом(int,float), або списком чисел")
    if isinstance(himmelblau_fitness_f_y_input, (int, float)):
        himmelblau_fitness_f_y_input = [himmelblau_fitness_f_y_input]
    elif not isinstance(himmelblau_fitness_f_y_input, list):
        raise ValueError("...введене значення повинне бути або числом(int,float), або списком чисел")
    for each_x, each_y in zip(himmelblau_fitness_f_x_input, himmelblau_fitness_f_y_input):
        res = (each_x ** 2 + each_y - 11) ** 2 + (each_x + each_y ** 2 - 7) ** 2
        himmelblau_fitness_f.append(res)
    return himmelblau_fitness_f
# Хіммельбау: -5 <= x,y <= 5
# Стіблинський-Танг: -5 <= Xi <= 5, 1 <= i <= n...

himmelblau_fitness_f_x_input = np.arange(-5, 5 + e_himmelblau_styblinskyTang_fitness_f,
                                         e_himmelblau_styblinskyTang_fitness_f)
himmelblau_fitness_f_y_input = np.arange(-5, 5 + e_himmelblau_styblinskyTang_fitness_f,
                                         e_himmelblau_styblinskyTang_fitness_f)
#min_himmelblau = min(himmelblau_fitness_f(list(himmelblau_fitness_f_x_input), list(himmelblau_fitness_f_y_input)))
min_himmelblau=np.float64(0.000)

styblinskiy_tang_f_x_input = np.arange(-5, 5 + e_himmelblau_styblinskyTang_fitness_f,
                                       e_himmelblau_styblinskyTang_fitness_f)
min_styblinskiy_tang = min(styblinsky_tang_fitness_f(list(styblinskiy_tang_f_x_input)))
min_styblinskiy_tang=np.float64(-39.166165)

print(type(min_himmelblau))
print(min_himmelblau, '\n',e_himmelblau_styblinskyTang_fitness_f)
print(f" Глобальный мін. Стибл-Танга:{min_styblinskiy_tang}")
