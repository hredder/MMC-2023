from matplotlib import pyplot as plt
import numpy as np
import csv
import json
import pandas as pd
from shapely.geometry import Polygon, Point, MultiPolygon

alpha_income =       1
alpha_kpr =          1
alpha_health =       1
alpha_insurance =    1
alpha_vehicles =     1
alpha_pop_density =  1

def Distance_Willing(income, kid_parant_ratio, health, insurance, vehicles, population_density):
    return alpha_income*income + alpha_kpr*kid_parant_ratio + alpha_health*health + alpha_insurance*insurance + alpha_vehicles*vehicles + alpha_pop_density*population_density

if __name__ == '__main__':
    count = 5000
    data_x = np.random.uniform(-84.41352382914673, -75.3388168853683, count)
    data_y = np.random.uniform(33.75578655156453, 36.733972442257816, count)

#Read the pharmacy x and y positions
phamacies_file = open("pharmacies.CSV", "r")
phamacies_reader = csv.reader(phamacies_file)
pharmacy_x = []
pharmacy_y = []
pharmacy_points = []
count = 0

for line in phamacies_reader:
    if (count > 0):
        pharmacy_x.append(float(line[8]))
        pharmacy_y.append(float(line[9]))
        pharmacy_points.append(Point(line[8], line[9]))
    count += 1

    #Import GPS data
    data = json.load(open('geojson.json'))
    df = pd.DataFrame(data["features"])

    #Extract fields
    df['Location'] = df['properties'].apply(lambda x: x['NAME'])
    df['Type'] = df['geometry'].apply(lambda x: x['type'])
    df['Coordinates'] = df['geometry'].apply(lambda x: x['coordinates'])

    #Generate polygon mapping
    df_new = pd.DataFrame()
    for idx, row in df.iterrows():

        if row['Type'] == 'MultiPolygon':
            list_of_polys = []
            df_row = row['Coordinates']
            for ll in df_row:
                list_of_polys.append(Polygon(ll[0]))
            poly = MultiPolygon(list_of_polys)

        elif row['Type'] == 'Polygon':
            df_row = row['Coordinates']
            poly = Polygon(df_row[0])

        else:
            poly = None

        row['Polygon'] = poly
        df_new = df_new.append(row)

    df_selection = df_new.drop(columns=['type', 'properties', 'geometry','Coordinates'] )
    nc_data_x = []
    nc_data_y = []
    nc_data_pharmacies = []

    #Prune random data for points only in N.C.
    for i in range(len(data_x)):
        point = Point(data_x[i], data_y[i])
        state = df_selection.apply(lambda row: row['Location'] if row['Polygon'].contains(point) else None, axis=1).dropna()
        if (state.size > 0 and state.iloc[0] == 'North Carolina'):
            nc_data_x.append(data_x[i])
            nc_data_y.append(data_y[i])


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



        

        # Iterate over every pharmacies checking its distance
        distance_willing = Distance_Willing(income, kpr, health, insurance, vehicles, pop_density)
        pharmacy_count = 0
        for pharmacy in pharmacy_points:
            if (distance(pharmacy, Point(data_x[i], data_y[i])) < distance_willing):
                pharmacy_count += 1
        nc_data_pharmacies.append(pharmacy_count)



#Plot random N.C. Data
    plt.scatter(nc_data_x,nc_data_y, c='b', s=3)
    plt.scatter(pharmacy_x, pharmacy_y, c='r', s=3)
    plt.show()
