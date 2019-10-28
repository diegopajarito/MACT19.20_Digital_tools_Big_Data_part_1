# encoding: utf-8

##################################################
# This script shows uses the pandas and matplotlib libraries to produce different kind of plots
# It also combines data from two sources and create multiple plots
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
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

# We need to import pandas library as well as the plot library matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# We read the file for population data and gross domestic product
population = pd.read_csv('../data/world/pop_total_v2.csv', skiprows=4, header=0)
gdp = pd.read_csv('../data/world/gdp_percap_v2.csv', skiprows=4, header=0)


# First, we filter data for a single country, mind the way to select only columns having numeric data
pop_country = population[population['Country Name'] == 'Spain']
pop_country = pop_country.iloc[0, 4:63]

gdp_country = gdp[gdp['Country Name'] == 'Spain']
gdp_country = gdp_country.iloc[0, 4:63]


# Plots allow basic configuration of visual features. Here some of the most common
colors = np.random.rand(len(pop_country)).sort()
plt.scatter(x=pop_country, y=gdp_country, c=colors)
plt.show()
#Change elements


# We can also combine data from more than a contry in a scatter plot for population and gdp
countries = ['Iran, Islamic Rep.', 'Germany', 'Argentina']
for value in countries:
    a_pop = population[population['Country Name'] == value]
    a_pop = a_pop.iloc[0, 4:63]
    a_gdp = gdp[gdp['Country Name'] == value]
    a_gdp = a_gdp.iloc[0, 4:63]
    plt.scatter(x=a_pop/1000000, y=a_gdp/1000)
plt.show()


# Charts can also use lines to represent dataLine chart multiple
countries = ['China', 'India', 'United States']
for value in countries:
    a_pop = population[population['Country Name'] == value]
    a_pop = a_pop.iloc[0, 4:63]
    plt.plot(a_pop)
plt.show()


# There are different ways to represent data density, this 2d histogram shows population and gdp distribution
plt.hist2d(pop_country, gdp_country)
plt.show()

# For more than one country, and more than one variable, there are options to arrange subplots
pop_selection = population[['Country Code', '1960', '1980', '2000', '2018']]
gdp_selection = gdp[['Country Code', '1960', '1980', '2000', '2018']]
selection = pop_selection.merge(gdp_selection, on='Country Code', how='left').dropna()

fig, axs = plt.subplots(2, 2)
axs[0, 0].scatter(selection['1960_x'], selection['1960_y'])
axs[1, 0].hist2d(selection['1980_x'], selection['1980_y'], bins=50)
axs[0, 1].scatter(selection['2018_x'], selection['2018_y'])
axs[1, 1].hist2d(selection['2000_x'], selection['2000_y'], bins=50)
plt.show()


# Finally, can also serve to visualise multiple elements to identify general trends
for value in gdp['Country Name']:
    a_pop = population[population['Country Name'] == value]
    a_pop = a_pop.iloc[0, 4:63]
    plt.plot(a_pop)
plt.show()