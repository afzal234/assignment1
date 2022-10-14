# 1 Using filter() function filter the list so that only negative numbers are left
test_list = [5, 6, -3, -8, 9, 11, -12, 2]

# printing original list
print("The original list is : " + str(test_list))

# Remove Negative element
res = [ele for ele in test_list if ele > 0]

print("List after filtering : " + str(res))

# 2 using filter function, filter the even numbers so that only odd numbers are passed to the new list
lst1 = [22, 100, 19, 13, 11, 1, 4, 66]
# Type your answer here.
lst2 = list(filter(lambda x: x % 2 == 1, lst1))
print(lst2)

# 3 Using filter() and list() functions and lower() method filter all the vowels in a given string.
str1="Winter Olympics in 2022 will take place in Beijing China"

lst=list(filter(lambda x: True if x.lower() in "aeiou" else False, str1))
print(lst)

# 4 This time swap the map() and filter() functigitons so that map() function is inside filter() function. Convert a
# number to positive if it's negative in the list. Only pass those that are converted from negative to
# positive to the new list.

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]

lst2 = list(filter(lambda x:True if x > 0 else False,map(lambda x:x*-1,lst1)))
print(lst2)