from es_import import *

import matplotlib.pyplot as plt
lambda_ = 10
mu = 30
needed_error = 0.0001
#needed_error=e_levi_13_f

########################################### Леви13
# ЛЯМБДА+МЮ #########################################################################################################################
# population_lplusmu=[]
def create_pochatkovu_pop_LambdaPlusMu_Levi13(lambda_, mu): # лямбда+мю
    population_lplusmu = []
    for _ in range(lambda_):
        parent_x = random.uniform(-10, 10)  # початкове значення батька x (1 батько із 4)
        parent_y = random.uniform(-10, 10)  # початкове значення батька y
        parent_and_children = []
        # додаємо батьків у популяцію:
        parent = [parent_x, parent_y]
        parent_and_children.append(parent)
        children = [[parent_x + random.gauss(0,0.2), parent_y + random.gauss(0,0.2)] for _ in range(mu)]
        parent_and_children.extend(children)
        population_lplusmu.append(parent_and_children)
    return population_lplusmu # return population, parent_and_children

#################################################################################################################

def create_next_pop_lambdaPlusMu_Levi13(old_pop, lambda_):
    next_pop, znach_levi13 = [],[]; best_individ =[]
    p_and_ch_disclosed_sqBrackets = []
    for j in old_pop:
        p_and_ch_disclosed_sqBrackets.extend(j)
    #levi_13_fitness_f(x,y):
    for each_p_and_ch in old_pop:
        for each_ind in each_p_and_ch:
            x = each_ind[0]
            y = each_ind[1]
            znach_levi13.append(levi_13_fitness_f(x, y))

    new_znach_levi13 = []
    for each_z in znach_levi13:
        new_znach_levi13.extend(each_z) # те ж саме, що й znach_levi13, але: [[],[],[]] -> [, , ,] (не сортовані)
    #error_for_each_znach = [abs(min_levi13-each_znach_levi13[0]) for each_znach_levi13 in znach_levi13] #помилка для кожного parent і child
    error_for_each_znach = [abs(min_levi13 - each_znach_levi13) for each_znach_levi13 in new_znach_levi13]
    sorted_error_for_each_znach_best_lambda = sorted(error_for_each_znach)[:lambda_] # обрали (лямбда) елементів найменших(найкращих згідно з формулою |min_real_levi13-each_znach[i]|)помилок)
    best_inds_indexes = [i for i, el in enumerate(new_znach_levi13) if error_for_each_znach[i] in sorted_error_for_each_znach_best_lambda] # індекси найкращих індивідів (можуть бути і батьки, і діти)
    # вибираємо кращих індивідів у популяції за отриманими індексами:
    #next_pop.append(p_and_ch_disclosed_sqBrackets[best_ind_index] for best_ind_index in best_inds_indexes)
    next_pop = [p_and_ch_disclosed_sqBrackets[best_ind_index] for best_ind_index in best_inds_indexes]
    next_pop = sorted(next_pop)
    best_individ = min(next_pop, key=lambda each_coord: abs(levi_13_fitness_f(each_coord[0], each_coord[1]) - min_levi13))
    return next_pop, best_individ # найкращі індивіди(лямбда(4) штуки) і найкращий індивид: [x,y]

pop_update = create_pochatkovu_pop_LambdaPlusMu_Levi13(lambda_,mu) # перша популяція, для входження в цикл
error_real, epoch = 100, 0
errors_history = []
epoch_history = []
print(f"Стратегія \"ЛЯМБДА + МЮ:\" ",'\n')
while error_real > needed_error:  #error_real > e_levi_13_f
    next_popul = []
    next_popul_best_lambda_inds, best_in = create_next_pop_lambdaPlusMu_Levi13(pop_update, lambda_)

    # створюємо нову популяцію,для (lambda_) кращих батьків
    for each_best_ind_lambda in next_popul_best_lambda_inds:
        p_x = each_best_ind_lambda[0]  #  значення батька x
        p_y = each_best_ind_lambda[1]  #  значення батька y
        p_and_c_ = []
        # добавляем родителей в популяцию:
        p = [p_x, p_y]
        p_and_c_.append(p)
        children_ = [[p_x + random.gauss(0,0.2), p_y + random.gauss(0,0.2)] for _ in range(mu)]
        p_and_c_.extend(children_)
        next_popul.append(p_and_c_)

    epoch+=1 #збільшуємо номер ітерації(популяції)
    #error_real = abs(best_in-min_levi13)
    error_real = abs(levi_13_fitness_f(best_in[0],best_in[1])-min_levi13)
    print(f"Ітерація: {epoch}, знайдена точка мінімуму: {best_in}, знач.функції Леві13: {levi_13_fitness_f(best_in[0],best_in[1])}, помилка:\\"
          f"{error_real} ",'\n')

    epoch_history.append(epoch)
    errors_history.append(error_real)
    if error_real < needed_error:
        print(f"...Знайдена точка(аргументи) глобального мінімуму: {best_in}, епоха(популяція):{epoch}, помилка: {error_real}, \\"
              f"глобальний мінімум: {levi_13_fitness_f(best_in[0],best_in[1])}",'\n')
        break # закінчуємо проводити ітерації(створення нових популяцій) і виходимо з циклу
    pop_update = next_popul  # оновлюємо список(аби значення були новими)
    best_in = 0

print("==================================================================================================================================\\"
      "=================================================================")
plt.plot(epoch_history, errors_history, marker='.', linestyle='-')
plt.title('Графік помилки для функції Леві13,Лямбда+МЮ')
plt.xlabel('Епоха')
plt.ylabel('Помилка')
plt.grid(True)
plt.show()



# ЛЯМБДА+МЮ #########################################################################################################################
#population_onlymu=[]
def create_pochatkovu_pop_OnlyMu_Levi13(lambda_, mu): # лямбда+мю
    population_onlymu = []
    for _ in range(lambda_):
        parent_x = random.uniform(-10, 10)  # початкове значення батька x (1 батько із lambda_)
        parent_y = random.uniform(-10, 10)  # початкове значення батька y
        # додаємо тільки нащадків
        #np.random.normal()
        children = [[parent_x + random.gauss(0,0.2), parent_y + random.gauss(0,0.2)] for _ in range(mu)]
        population_onlymu.append(children)
    return population_onlymu # return population, parent_and_children


def create_next_pop_onlyMu_Levi13(old_pop, lambda_):
    next_pop, znach_levi13 = [],[]; best_individ =[]
    p_and_ch_disclosed_sqBrackets = []
    for j in old_pop:
        p_and_ch_disclosed_sqBrackets.extend(j)
    #levi_13_fitness_f(x,y):
    for each_p_and_ch in old_pop:  # old_parent_and_children
        for each_ind in each_p_and_ch:
            x = each_ind[0]
            y = each_ind[1]
            znach_levi13.append(levi_13_fitness_f(x, y))

    new_znach_levi13 = []
    for each_z in znach_levi13:
        new_znach_levi13.extend(each_z) # то же самое, что и znach_levi13, но: [[],[],[]] -> [, , ,] (не сортированные)
    #error_for_each_znach = [abs(min_levi13-each_znach_levi13[0]) for each_znach_levi13 in znach_levi13] #помилка для кожного parent і child
    error_for_each_znach = [abs(min_levi13 - each_znach_levi13) for each_znach_levi13 in new_znach_levi13]
    sorted_error_for_each_znach_best_lambda = sorted(error_for_each_znach)[:lambda_] # обрали (лямбда) елементів найменших(найкращих згідно з формулою |min_real_levi13-each_znach[i]|)помилок)
    best_inds_indexes = [i for i, el in enumerate(new_znach_levi13) if error_for_each_znach[i] in sorted_error_for_each_znach_best_lambda] # індекси найкращих індивідів (можуть бути і батьки, і діти)
    # вибираємо кращих індивідів у популяції за отриманими індексами:
    #next_pop.append(p_and_ch_disclosed_sqBrackets[best_ind_index] for best_ind_index in best_inds_indexes)
    next_pop = [p_and_ch_disclosed_sqBrackets[best_ind_index] for best_ind_index in best_inds_indexes]
    next_pop = sorted(next_pop)
    best_individ = min(next_pop, key=lambda each_coord: abs(levi_13_fitness_f(each_coord[0], each_coord[1]) - min_levi13))
    return next_pop, best_individ # лучшие индивиды(лямбда(4) штуки) и лучший индивид: [x,y]

pop_update = create_pochatkovu_pop_OnlyMu_Levi13(lambda_,mu) # перша популяція, для входження в цикл
error_real, epoch = 100, 0
errors_history = []
epoch_history = []
print(f"Стратегія \"ЛЯМБДА,МЮ (тільки нащадки):\" ",'\n')
while error_real > needed_error:  #error_real > e_levi_13_f
    next_popul = []
    next_popul_best_lambda_inds, best_in = create_next_pop_onlyMu_Levi13(pop_update, lambda_)

    # створюємо нову популяцію,для (lambda_) кращих батьків
    for each_best_ind_lambda in next_popul_best_lambda_inds:
        p_x = each_best_ind_lambda[0]  #  значення батька x
        p_y = each_best_ind_lambda[1]  #  значення батька y

        children_ = [[p_x + random.gauss(0,0.2), p_y + random.gauss(0,0.2)] for _ in range(mu)]
        next_popul.append(children_)

    epoch+=1 #збільшуємо номер ітерації(популяції)
    #error_real = abs(best_in-min_levi13)
    error_real = abs(levi_13_fitness_f(best_in[0],best_in[1])-min_levi13)
    print(f"Ітерація: {epoch}, знайдена точка мінімуму: {best_in}, знач.функції Леві13: {levi_13_fitness_f(best_in[0],best_in[1])}, помилка:\\"
          f"{error_real} ",'\n')
    errors_history.append(error_real)
    epoch_history.append(epoch)
    if error_real < needed_error:
        print(f"...Знайдена точка(аргументи) глобального мінімуму: {best_in}, епоха(популяція):{epoch}, помилка: {error_real}, \\"
              f"глобальний мінімум: {levi_13_fitness_f(best_in[0],best_in[1])}",'\n')
        break # закінчуємо проводити ітерації(створення нових популяцій) і виходимо з циклу
    pop_update = next_popul  # оновлюємо список(аби значення були новими)
    best_in = 0

print("==================================================================================================================================\\"
      "=================================================================")

plt.plot(epoch_history, errors_history, marker='.', linestyle='-')
plt.title('Графік помилки для функції Леві13, Лямбда,МЮ')
plt.xlabel('Епоха')
plt.ylabel('Помилка')
plt.grid(True)
plt.show()
