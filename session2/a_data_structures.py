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

a_list = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City', 'Cairo', 'Dhaka', 'Mumbai', 'Beijing', 'Osaka']
print('####################')
print('This is how a list looks like:')
print(a_list)
print('Mind the use of square brackets [ ]')

a_tuple = (37435191, 29399141, 26317104, 21846507, 21671908, 20484965, 20283552, 20185064, 20035455, 19222665)
print('####################')
print('This is how a tuple looks like:')
print(a_tuple)
print('Mind the use of parenthesis ( )')


a_dict = {
    'cities': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City', 'Cairo', 'Dhaka', 'Mumbai', 'Beijing', 'Osaka'],
    'population': (37435191, 29399141, 26317104, 21846507, 21671908, 20484965, 20283552, 20185064, 20035455, 19222665),
    'source': 'http://worldpopulationreview.com/world-cities/'
}
print('####################')
print('This is how a dict looks like:')
print(a_dict)
print('Mind the use curly brackets { } and the internal arrangement of variables and other data structures')

print('####################')
print('There are two ways for calling out elements from those structures')
print('First: Numeric Indexes from 0 to n. They apply to both lists and tuples')
print('This is the value of position 3 in "a_list": ' + a_list[2])
print('This is the value of position 5 in "a_tuple": ' + str(a_tuple[4]))

print('####################')
print('Second: Labeled indexes. They only apply to dictionaries')
print('This is the value labeled as "source" in "a_dict": ' + a_dict['source'])

print('####################')
print('Keep in mind indexes, they are useful for loops and conditionals')
