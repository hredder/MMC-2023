
alpha_income =       1
alpha_kpr =          1
alpha_health =       1
alpha_insurance =    1
alpha_vehicles =     1
alpha_pop_density =  1

def calc_distance(x, y):
    # TODO: Get distance for point
    # Get urban center
    urban = False
    # Get race
    white = False


    return Distance_Willing(urban, white)
    #return 5

def Distance_Willing(urban, white):
    if not urban and white:
        return white*23.15 + (1-white)*21.575
    elif urban and white:
        return 19.3
    elif not urban and not white:
        return 21.575
    elif urban and not white:
        return 17.725
