# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt


# %%
file = "Google_Mobility_Report.csv"

df = pd.read_csv("Google_Mobility_Report.csv", low_memory=False) #low_memory=False is to adjust dtype, whatever that is.
#Much easier than Johns Hopkins in that there is one file, so all we need to do is read that csv file into a table.

df.fillna(0)
df


# %%
for country in countries:
    #trying to limit the data to us
    c = df[df['country_region'] == country]
    usa = df.astype(str).sum(axis=1).str.contains('United States')
    #df[country] makes new dataframe thingy
    #df.astype(str) converts all the things in the data table to string
    #.str.contains('United States') looks to see if column's value contains 'United States'
    #.sum(axis=1) concatenates horizontally
    #What's left: print only the values in the column in which the string parameters above are true
    #error: DataFrame is not callable

usa
usa[usa]
usa[usa].index
df[df('country_region').isin(usa[usa].index)]


# %%
countries = ['United States']
states = ['Virginia']
counties = ['Fairfax County']

for county in counties:
    s = df[df['sub_region_2'] == county]
    plt.plot(s['date'], s['retail_and_recreation_percent_change_from_baseline'], label = counties)
  
plt.legend
plt.show

#Google Mobility Data