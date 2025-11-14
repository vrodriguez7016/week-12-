# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#ltsts are part of the collections family in Python
# Creating a list
my_list1 = [1, 2, 3, 4, 5]
print(my_list1) # [1, 2, 3, 4, 5]
print(len(my_list1)) # 5
print(type(my_list1)) # <class 'list'>
print(my_list1[0]) # 1
print(my_list1[1:4]) # [2, 3, 4]
print(my_list1[1:]) # [2, 3, 4, 5]
print(my_list1[:-1]) # [1, 2, 3, 4]
# reverse the list
print(my_list1[::-1])
# modifying a list
my_list1.append(6) # adds 6 to the end of the list
print(my_list1) # [1, 2, 3, 4, 5]
# add 7 and 8 to the end of the list
my_list1.extend([7, 8])
print(my_list1) # [1, 2, 3, 4, 5, 6, 7, 8]

my_list1.extend([9, 10, 11])
print(my_list1) # 
# remove the last item
my_list1.pop()
print(my_list1) # [1, 2, 3, 4, 5, 6, 7]
# remove the item at index 2
my_list1.pop(2)
print(my_list1) # [1, 2, 3, 4, 5, 6, 7]
# sort the list in ascending order
my_list1.sort()
print(my_list1) # [1, 2, 3, 4, 5, 6, 7]
# reverse the list
my_list1.reverse()
print(my_list1) # [7, 6, 5, 4, 3, 2, 1]
#.remove to remove a specific value
my_list1.remove(4)
print(my_list1) # [7, 6, 5, 2, 1]
# remove the last item using negative index
my_list1.pop(-1)
print(my_list1)
# add 50 more to the end of the list
new_list = list(range(12, 120))
print(new_list)
my_list1.append(new_list)
print(my_list1)
# my_list1.extend(new_list)
# print(my_list1)
# add 500 more
new_list1 = list(range(120, 620))
my_list1.extend(new_list1)
print(len(my_list1))
# print every 3rd item in the list
print(my_list1[ : : 3])
# print every 10th number
print(my_list1[ : : 10])
# print every 20th number
print(my_list1[ : : 20])
# remove every 3rd item in the list
del my_list1[ : : 3]
print(len(my_list1))
print(my_list1)

# list functions
# .append() - adds an item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - removed and returns an item at a given index
# (default is the last item)
# .remove() - removes the first occurencen of a specific value
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list
################################################
# why is a list more useful than a variable?
# A list can hold multiple values,
# while a variable can hold one value at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
# access the first item
print(cakes[0]) # chocolate
# access the last item
print(cakes[-1]) # carrot
# want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes) # ['strawberry', 'vanilla', 'red velvet', 'carrot']
# add a new cake to the end of the list
cakes.append('lemon')
print(cakes) # ['strawberry', 'chocolate', 'red velvet', 'carrot', 'lemon']
#remove the last cake
cakes.pop(0)
print(cakes) # ['strawberry', 'chocolate', 'red velvet',
# insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes) # ['strawberry', 'chocolate', 'funfetti',


# # Examples:

my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.
foods = ["Pizza, pasta, salad, tortilla fish, salchipapas"]
print(foods)
# # Print the second and last item.
print(foods[1])
print(foods[-1])
# # Add a new item using .append().
foods.append('hot dog')
print(foods)
# # Remove the first item using .pop(0).
foods.pop(0)
print(foods)
# # Reverse your list using .reverse().
foods.reverse()
print(foods)

# sets = {1, 2, 3}
# sets are unordered collections of unique items
# sets do not support indexing or slicing
# sets are mutable, meaning you can add or remove items
# sets are created using curly braces{}
my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}
print(type(my_set)) # <class 'set'>
# add an item to the set
my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}
# remove an item from the set
my_set.remove(3)
print(my_set) # {1, 2, 4, 5, 6}

# check if an item is in the set
print(4 in my_set) # True
print(3 in my_set) # False

# tuples are ordered collections of tems
# tuples are immutable, meaning you cannot modify them after creation
# tuples are created using parentheses ()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) # (1, 2, 3, 4, 5)
print(type(my_tuple)) # <class 'tuple'>
print(my_tuple[0]) # 1
print(my_tuple[1:4]) # (2, 3, 4)
# try to modify the tuple (will raise an error)
