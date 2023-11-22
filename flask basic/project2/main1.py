###############
## Problem 1 ##
###############

# Given the string:
s = 'flask'

# Use indexing to print out the following:
print(s[0])
# 'f'
print(s[3])
# 's'
print(s[2:])
# 'ask'
print(s[1:4])
# 'las'
print(s[-1])
# 'k'

# Bonus: Use indexing to reverse the string
print(s[::-1])

###############
## Problem 2 ##
###############

# Given this nested list:
mylist = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
mylist[2][2]= "goodbye"
print(mylist)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print(f"Hello my dog's name is {name} and he is {age} years old")