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

# We need to import pandas library
import pandas as pd

# We read the file for population data
a_df = pd.read_csv('../data/world/pop_total_v2.csv', skiprows=4, header=0)

# Range is the combination of min-max values
print('####################')
print('This is an example of the range values for the year 1960:')
pop_1960 = a_df['1960']
min_value = pop_1960.min()
max_value = pop_1960.max()
print('Population ranged between %i and %i' % (min_value, max_value))

# There are a set of statistics to descibe central tendency
mean_value = pop_1960.mean()
mode_value = pop_1960.mode()
median_value = pop_1960.median()
print('####################')
print('The three values for the central tendency of population in 1960 are:')
print('Mean population: %i' % mean_value)
print('Mode population: %s' % str(mode_value))
print('Median population: %i' % median_value)



# There are statistical values for dispersion
variance_value = pop_1960.var()
stdev_value = pop_1960.std()
print('####################')
print('The two values for the central tendency of population in 1960 are:')
print('Variance: %f' % variance_value)
print('Standard deviation: %f' % stdev_value)


# Work on differences across the years but especially across the countries
