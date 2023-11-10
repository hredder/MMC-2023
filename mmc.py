from matplotlib import pyplot as plt
import numpy as np

alpha_income =       1
alpha_kpr =          1
alpha_health =       1
alpha_insurance =    1
alpha_vehicles =     1
alpha_pop_density =  1

def Distance_Willing(income, kid_parant_ratio, health, insurance, vehicles, population_density):
    return alpha_income*income + alpha_kpr*kid_parant_ratio + alpha_health*health + alpha_insurance*insurance + alpha_vehicles*vehicles + alpha_pop_density*population_density

count = 1000
data_x = np.random.uniform(33.75578655156453, 36.733972442257816, count)
data_y = np.random.uniform(-84.41352382914673, -75.3388168853683, count)

plt.scatter(data_x, data_y)
plt.show()

print(data_x)
print(data_y)