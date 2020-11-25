import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns
df = pd.read_json(r'https://data.cdc.gov/resource/9mfq-cb36.json')
Stat = df[['state','tot_cases']].groupby(['state']).sum()
print(Stat)
Stat2 = df[['state','tot_death']].groupby(['state']).sum()
print(Stat2)
#test