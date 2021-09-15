#..........................................................#
### Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##........................................................##
df = pd.read_csv(r'dataset.csv')
df.head()

##........................................................##
#check null/nan values
df.isnull().sum()
df.isna().sum()

df.isnull().sum().any
df.isna().sum().any


##........................................................##
