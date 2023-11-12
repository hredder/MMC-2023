import pandas as pd

def calc_distance(x, y, county):
    # TODO: Get distance for point
    # Get urban center
    urbanDf = pd.read_csv("Rural_and_Urban_Data.csv")
    urbanType = urbanDf.loc[urbanDf['County'] == county].iloc[3]
    if urbanType == Urban:
        urban = True
    else:
        urban = False
    # Get race
    whiteDf = pd.read_csv("nc-count-by-ethnicity SORTED.csv")
    white = whiteDf.loc[(whiteDf['County'] == county) & (whiteDf['Race'] == 'White alone')].iloc[3]


    return Distance_Willing(urban, white)
    #return 5

def Distance_Willing(urban, white):
    if not urban:
        return white*23.15 + (1-white)*21.575
    else:
        return white*17.725 + (1-white)*19.3
