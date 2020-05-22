import os
import pandas as pd
import matplotlib.pyplot as plt

file = "Google_Mobility_Report.csv"

df = pd.DataFrame() #establishes df as DataFrame (data table)

pd.read_csv("Google_Mobility_Report.csv", low_memory=False) #low_memory=False is to adjust dtype, whatever that is.
#Much easier than Johns Hopkins in that there is one file, so all we need to do is read that csv file into a table.