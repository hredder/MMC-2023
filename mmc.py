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

count = 10
data_x = np.random.uniform(33.75578655156453, 36.733972442257816, count)
data_y = np.random.uniform(-84.41352382914673, -75.3388168853683, count)

#Read the pharmacy x and y positions
file=open("pharmacies.CSV", "r")
reader = csv.reader(file)
pharmacy_x = []
pharmacy_y = []
count = 0

for line in reader:

    if (count > 0):
        pharmacy_x.append(float(line[8]))
        pharmacy_y.append(float(line[9]))
    count += 1

#plt.scatter(data_x, data_y)
#plt.scatter(pharmacy_x, pharmacy_y, c='r')
#plt.show()


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
nc_pharmacies_x = []
nc_pharmacies_y = []

for i in range(len(pharmacy_x)):
    point = Point(pharmacy_x[i], pharmacy_y[i])
    state = df_selection.apply(lambda row: row['Location'] if row['Polygon'].contains(point) else None, axis=1).dropna()
    print(state)