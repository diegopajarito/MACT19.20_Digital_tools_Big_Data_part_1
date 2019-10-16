# encoding: utf-8

##################################################
# This script shows three different data structures commonly used in python scripts
# This is a review of that basic structures prior to introduce the data structures used in pandas
# There are multiple examples of how to use these structures. Here three of them:
# Lists: https://www.w3schools.com/python/python_lists.asp
# Dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
# Tuples: https://www.w3schools.com/python/python_tuples.asp
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

# There is no need for extra libraries

cities = {
    'cities': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City', 'Cairo', 'Dhaka', 'Mumbai', 'Beijing', 'Osaka'],
    'population': [37435191, 29399141, 26317104, 21846507, 21671908, 20484965, 20283552, 20185064, 20035455, 19222665],
}

print('####################')
print('We can use a loop to print out the values in variables:')
for text in cities['cities']:
    print(text)

print('####################')
print('We can also uses indexes as part of the loop')
for i in range(0, len((cities['cities']))):
    text = '%s - %i people'
    print(text % (cities['cities'][i], cities['population'][i]))

print('####################')
print('With conditionals we can decide to change the course of events based on conditions')
print('For instance, we only print cities with population bigger than 25 million')
for i in range(0, len((cities['cities']))):
    if cities['population'][i] > 25000000:
        text = '%s has more than 25 million people (%i)'
        print(text % (cities['cities'][i], cities['population'][i]))
    else:
        text = '%s has less than 25 million people'
        print(text % cities['cities'][i])
