# encoding: utf-8

##################################################
# This script shows uses the pandas library to create statistically describe datasets
# It also shows basic plotting features
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2019, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library as well as the plot libraries matplotlib and seaborn
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np

# We read the file for population data
a_df = pd.read_csv('../data/world/pop_total_v2.csv', skiprows=4, header=0)

# Range is the combination of min-max values
print('####################')
print('This is an example of the range values for the year 1960:')
pop_2010 = a_df['2010']
pop_2010 = pop_2010[~np.isnan(pop_2010)]    # Note: working with series and seaborn usually demands dropping 'nan'
pop_comparison = a_df[['Country Code', '1960', '1990', '2010']]
pop_country = a_df[a_df['Country Name'] == 'Spain']
pop_country = pop_country.iloc[0, 4:53]

# Histogram and normal distribution
sns.distplot(pop_2010)


# Kernel density
sns.distplot(pop_2010, hist=False, rug=True)

sns.kdeplot(pop_2010, shade=True)


# Scatter plot two years all countries
pop_comparison.plot.scatter(x='1960', y='1990', c='DarkBlue')
max_range = range(0, 1000000000, 500000000)     # Sets values for an straight line
plt.pyplot.plot(max_range, max_range)
plt.show()


# Scatter plot one country all years
pop_country.plot()
plt.show()


# Try to compare multiple countries


# plot correlation
# ====================================
sns.set_style('ticks')
sns.regplot(pop_comparison['1960'], pop_comparison['1990'], ci=None)
sns.despine()


sns.set_style('ticks')
sns.regplot(pop_comparison['1990'], pop_comparison['2010'], ci=None)
sns.despine()


# rate of growth



