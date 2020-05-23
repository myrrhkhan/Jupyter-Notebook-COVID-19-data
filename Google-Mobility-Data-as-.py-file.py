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
usa = df['country_region'] == 'United States'
df[usa] = df[df['country_region'] == 'United States']
#Makes new data frame in which all of the data table values have united states as country_region. Source: https://towardsdatascience.com/apply-and-lambda-usage-in-pandas-b13a1ea037f7
#df[usa] is a new dataframe.
#df['country_region]=='United States' takes all of the data with US in it, and putting "df[]" around it makes a data table of it.
df[usa]


# %%
countries = ['United States']
states = ['Virginia']
counties = ['Fairfax County']

for county in counties:
    s = df[df['sub_region_2'] == county]
    plt.plot(s['date'], s['retail_and_recreation_percent_change_from_baseline'], label = counties)
  
plt.legend()
plt.show()


# %%
countries = ['United States']
states = ['Virginia']
counties = ['Fairfax County', 'Fairfax', 'Loudoun County', 'Stafford County']

for county in counties:
    s = df[df['sub_region_2'] == county]
    plt.plot(s['date'], s['retail_and_recreation_percent_change_from_baseline'], label = counties)

plt.legend()
plt.show()

#Google Mobility Data