from es_import import *
lambda_ = 10
mu = 30
needed_error = 0.0001
import matplotlib.pyplot as plt
#needed_error = e_himmelblau_styblinskyTang_fitness_f
#       styblinsky_tang_fitness_f
#  min_styblinskiy_tang

# ЛЯМБДА+МЮ #########################################################################################################################
# population_lplusmu=[]
def create_pochatkovu_pop_LambdaPlusMu_StyblinskiyTang(lambda_, mu): # лямбда+мю
    population_lplusmu = []
    for _ in range(lambda_):
        parent_x = random.uniform(-5, 5)  # початкове значення батька x (1 батько із 4)
        parent_and_children = []
        # добавляем родителей в популяцию:
        parent = parent_x
        parent_and_children.append(parent)
        children = [parent_x + random.gauss(0,0.2) for _ in range(mu)]
        parent_and_children.extend(children)
        population_lplusmu.append(parent_and_children)
    return population_lplusmu # return population, parent_and_children

#################################################################################################################

def create_next_pop_lambdaPlusMu_StyblinskiyTang(old_pop, lambda_):
    next_pop, znach_styblinskiyTang = [],[]; best_individ =[]
    p_and_ch_disclosed_sqBrackets = []
    for j in old_pop:
        p_and_ch_disclosed_sqBrackets.extend(j)
    for each_p_and_ch in old_pop:  # old_parent_and_children
        for each_ind in each_p_and_ch:
            x = each_ind
            znach_styblinskiyTang.append(styblinsky_tang_fitness_f(x))

    new_znach_styblinskiyTang = []
    for each_z in znach_styblinskiyTang:
        new_znach_styblinskiyTang.extend(each_z) # те ж саме, що й znach_levi13, але: [[],[],[]] -> [, , ,] (не сортовані)
    error_for_each_znach = \
        [abs(min_styblinskiy_tang - each_znach_styblinskiyTang) for each_znach_styblinskiyTang in new_znach_styblinskiyTang]
    sorted_error_for_each_znach_best_lambda = sorted(error_for_each_znach)[:lambda_] # обрали (лямбда) елементів найменших(найкращих згідно з формулою |min_real_levi13-each_znach[i]|)помилок)
    best_inds_indexes = [i for i, el in enumerate(new_znach_styblinskiyTang) if error_for_each_znach[i] in sorted_error_for_each_znach_best_lambda] # індекси найкращих індивідів (можуть бути і батьки, і діти)
    # вибираємо кращих індивідів у популяції за отриманими індексами:
    next_pop = [p_and_ch_disclosed_sqBrackets[best_ind_index] for best_ind_index in best_inds_indexes]
    next_pop = sorted(next_pop)
    best_individ = min(next_pop, key=lambda each_coord: abs(styblinsky_tang_fitness_f(each_coord) - min_styblinskiy_tang))
    return next_pop, best_individ # лучшие индивиды(лямбда(4) штуки) и лучший индивид: [x,y]

pop_update = create_pochatkovu_pop_LambdaPlusMu_StyblinskiyTang(lambda_,mu) # перша популяція, для входження в цикл
error_real, epoch = 19000, 0
errors_history=[]
epoch_history=[]
print(f"Стратегія \"ЛЯМБДА + МЮ:\" ",'\n')
while error_real > needed_error:  #error_real > e_himmelblau_styblinskyTang_fitness_f
    next_popul = []
    next_popul_best_lambda_inds, best_in = create_next_pop_lambdaPlusMu_StyblinskiyTang(pop_update, lambda_)

    # створюємо нову популяцію,для (lambda_) кращих батьків
    for each_best_ind_lambda in next_popul_best_lambda_inds:
        p_x = each_best_ind_lambda  #  значення батька x
        p_and_c_ = []
        # добавляем родителей в популяцию:
        p = p_x
        p_and_c_.append(p)
        children_ = [p_x + random.gauss(0,0.2) for _ in range(mu)]
        p_and_c_.extend(children_)
        next_popul.append(p_and_c_)

    epoch+=1 #збільшуємо номер ітерації(популяції)
    error_real = abs(styblinsky_tang_fitness_f(best_in)-min_styblinskiy_tang)
    print(f"Ітерація: {epoch}, знайдена точка мінімуму: {best_in}, знач.функції Стиблінського-Танга: "
          f"{styblinsky_tang_fitness_f(best_in)}, помилка:\\"
          f"{error_real} ",'\n')
    errors_history.append(error_real)
    epoch_history.append(epoch)
    if error_real < needed_error:
        print(f"...Знайдена точка(аргументи) глобального мінімуму: {best_in}, епоха(популяція):{epoch}, помилка: {error_real}, \\"
              f"глобальний мінімум: {styblinsky_tang_fitness_f(best_in)}",'\n')
        break # закінчуємо проводити ітерації(створення нових популяцій) і виходимо з циклу
    pop_update = next_popul  # оновлюємо список(аби значення були новими)
    best_in = 0

print("==================================================================================================================================\\"
      "=================================================================")
plt.plot(epoch_history, errors_history, marker='.', linestyle='-')
plt.title('Графік помилки для функції Ст.-Танга, Лямбда+МЮ')
plt.xlabel('Епоха')
plt.ylabel('Помилка')
plt.grid(True)
plt.show()



# ЛЯМБДА+МЮ #########################################################################################################################
#population_onlymu=[]
def create_pochatkovu_pop_OnlyMu_StyblinskiyTang(lambda_, mu): # лямбда+мю
    population_onlymu = []
    for _ in range(lambda_):
        parent_x = random.uniform(-5, 5)  # початкове значення батька x (1 батько із lambda_)
        # додаємо тільки нащадків
        children = [parent_x + random.gauss(0,0.2) for _ in range(mu)]
        population_onlymu.append(children)
    return population_onlymu # return population, parent_and_children


def create_next_pop_onlyMu_StyblinskiyTang(old_pop, lambda_):
    next_pop, znach_styblisnkiyTang = [],[]; best_individ =[]
    p_and_ch_disclosed_sqBrackets = []
    for j in old_pop:
        p_and_ch_disclosed_sqBrackets.extend(j)
    #styblinsky_tang_fitness_f(x,y):
    for each_p_and_ch in old_pop:  # old_parent_and_children
        for each_ind in each_p_and_ch:
            x = each_ind
            znach_styblisnkiyTang.append(styblinsky_tang_fitness_f(x))

    new_znach_styblisnkiyTang = []
    for each_z in znach_styblisnkiyTang:
        new_znach_styblisnkiyTang.extend(each_z) # те ж саме, що й znach_levi13, але: [[],[],[]] -> [, , ,] (не сортовані)
    error_for_each_znach = [abs(min_styblinskiy_tang - each_znach_styblisnkiyTang) for each_znach_styblisnkiyTang in new_znach_styblisnkiyTang]
    sorted_error_for_each_znach_best_lambda = sorted(error_for_each_znach)[:lambda_] # обрали (лямбда) елементів найменших(найкращих згідно з формулою |min_real_levi13-each_znach[i]|)помилок)
    best_inds_indexes = [i for i, el in enumerate(new_znach_styblisnkiyTang) if error_for_each_znach[i] in sorted_error_for_each_znach_best_lambda] # індекси найкращих індивідів (можуть бути і батьки, і діти)
    # вибираємо кращих індивідів у популяції за отриманими індексами:
    next_pop = [p_and_ch_disclosed_sqBrackets[best_ind_index] for best_ind_index in best_inds_indexes]
    next_pop = sorted(next_pop)
    best_individ = min(next_pop, key=lambda each_coord: abs(styblinsky_tang_fitness_f(each_coord) - min_styblinskiy_tang))
    return next_pop, best_individ # лучшие индивиды(лямбда(4) штуки) и лучший индивид: [x,y]

pop_update = create_pochatkovu_pop_OnlyMu_StyblinskiyTang(lambda_,mu) # перша популяція, для входження в цикл
error_real, epoch = 100, 0
errors_history=[]
epoch_history=[]
print(f"Стратегія \"ЛЯМБДА,МЮ (тільки нащадки):\" ",'\n')
while error_real > needed_error:  #error_real > e_himmelblau_styblinskyTang_fitness_f
    next_popul = []
    next_popul_best_lambda_inds, best_in = create_next_pop_onlyMu_StyblinskiyTang(pop_update, lambda_)

    # створюємо нову популяцію,для (lambda_) кращих батьків
    for each_best_ind_lambda in next_popul_best_lambda_inds:
        p_x = each_best_ind_lambda  #  значення батька x

        children_ = [p_x + random.gauss(0,0.2) for _ in range(mu)]
        next_popul.append(children_)

    epoch+=1 #збільшуємо номер ітерації(популяції)
    error_real = abs(styblinsky_tang_fitness_f(best_in)-min_styblinskiy_tang)
    print(f"Ітерація: {epoch}, знайдена точка мінімуму: {best_in}, знач.функції Стиблінського-Танга: {styblinsky_tang_fitness_f(best_in)}, помилка:\\"
          f"{error_real} ",'\n')
    errors_history.append(error_real)
    epoch_history.append(epoch)
    if error_real < needed_error:
        print(f"...Знайдена точка(аргументи) глобального мінімуму: {best_in}, епоха(популяція):{epoch}, помилка: {error_real}, \\"
              f"глобальний мінімум: {styblinsky_tang_fitness_f(best_in)}",'\n')
        break # закінчуємо проводити ітерації(створення нових популяцій) і виходимо з циклу
    pop_update = next_popul  # оновлюємо список(аби значення були новими)
    best_in = 0

print("==================================================================================================================================\\"
      "=================================================================")
plt.plot(epoch_history, errors_history, marker='.', linestyle='-')
plt.title('Графік помилки для функції Ст.-Танга, Лямбда,МЮ')
plt.xlabel('Епоха')
plt.ylabel('Помилка')
plt.grid(True)
plt.show()
