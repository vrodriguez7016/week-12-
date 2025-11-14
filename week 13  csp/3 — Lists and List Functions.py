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

# # Examples:

# my_list = ['apple', 'banana', 'cherry']
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
# foods = ["Pizza, pasta, salad, tortilla fish, salchipapas."]
# # Print the second and last item.
# print(foods[1:5])
# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.
