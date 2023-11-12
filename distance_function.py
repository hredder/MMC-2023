
alpha_income =       1
alpha_kpr =          1
alpha_health =       1
alpha_insurance =    1
alpha_vehicles =     1
alpha_pop_density =  1

def calc_distance(x, y):
    # TODO: Get distance for point
    # Get income
    income = 0
    # Get kid to parent ratio
    kpr = 0
    # Get general health
    health = 0
    # Get insurance
    insurance = 0
    # Get number of vehicles
    vehicles = 0
    # Get population density
    pop_density = 0
    #return Distance_Willing(income, kpr, health, insurance, vehicles, pop_density)
    return 5



def Distance_Willing(income, kid_parant_ratio, health, insurance, vehicles, population_density):
    #return alpha_income*income + alpha_kpr*kid_parant_ratio + alpha_health*health + alpha_insurance*insurance + alpha_vehicles*vehicles + alpha_pop_density*population_density
    return 2