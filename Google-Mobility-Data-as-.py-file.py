# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt


# %%
file = "Google_Mobility_Report.csv"

df = pd.read_csv("Google_Mobility_Report.csv", low_memory=False) #low_memory=False is to adjust dtype, whatever that is.
#Much easier than Johns Hopkins in that there is one file, so all we need to do is read that csv file into a table.

df.head()


# %%
countries = ['United Arab Emirates', 'United States']

for country in countries:
    c = df[df['country_region'] == country]
    plt.plot(c['date'], c['retail_and_recreation_percent_change_from_baseline'], label = country)
    
plt.legend
plt.show

#Google Mobility Data