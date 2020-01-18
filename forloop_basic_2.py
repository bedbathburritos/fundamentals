# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_pos(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def total(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def avg(lst):
    avg = 0
    for i in lst:
        avg += i
    return float(avg) / float(len(lst))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(lst):
    length = 0
    for i in lst:
        length += 1
    return length

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(lst):
    result = lst[0]
    if len(lst) == 0:
        return False
    for val in lst:
        if val < result:
            result = val
    return result

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(lst):
    if len(lst) == 0:
        return False

    result = lst[0]
    for val in lst:
        if val > result:
            result = val
    return result

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate(lst):
    new_dict = {
        'sumTotal': None
        'average': None
        'minimum': None
        'maximum': None
        'length': 0
    }
    if len(lst) == 0:
        return new_dict
    else:
        result['sum_total'] = 0
        result['maximum'] = 0
        result['minimum'] = 0
    for i in lst: 
        if i > result['maximum']:
            result['maximum'] = i
        elif i < result['minimum']:
            result['minimum'] = i
        result['sumTotal'] += i
        result['length'] += 1
    result['average'] = result['sumTotal'] / len(lst)


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def rev(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]
    return lst