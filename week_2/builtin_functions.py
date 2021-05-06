# absolute value

print (abs(2))  

# convert an integer in binary 

print (bin(4))          

# Return number rounded to ndigits precision after the decimal point.

print (round(5.65))  

print (round(5.45))

print (round(5.45589, 2))

print (round(5.658942135, 3))


# represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops. 

print (list(range(10)))

print(list(range(1, 11)))

print(list(range(0, 30, 5)))  # range(start, stop, step)


# adds the items of an iterable and returns the sum: sum(iterable, start)
    # iterable - iterable (list, tuple, dict, etc). The items of the iterable should be numbers.
    # start (optional) - is added to the sum of items of the iterable. The default value of start is 0 (if omitted)

print (sum([1, 3], 2))

print (sum([1, 1 , 1, 1,1], 1))

# eturns a slice object that can use used to slice strings, lists, tuple etc.  slice(start, stop, step)

result1 = slice(3)
print(result1)

result2 = slice(1, 5, 2)
print(slice(1, 5, 2))

py_string = 'Python'

slice_object = slice(3) 
print(py_string[slice_object])  # pyt

print(py_string[0:3])  # pyt

slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn

print(py_string[1:5:2]) # yh

slice_object = slice(-1, -4, -1)
print(py_string[slice_object])   # noh




        # Get sublist and sub-tuple

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h')    

slice_object = slice(-1, -4, -1) 
print(py_list[slice_object])  # ['n', 'o', 'h']

slice_object = slice(-1, -5, -2)
print(py_tuple[slice_object]) # ('n', 'h')

