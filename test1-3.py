# Using the higher order function reduce(), write a function max_in_list()
# that takes a list of numbers and returns the largest one. Then ask
# yourself: why define and call a new function, when I can just as well
# call the reduce() function directly?

from functools import reduce


def max_in_list( num_list ):
    return reduce( max, num_list )

print(max_in_list([2,22,222]))
