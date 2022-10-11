# 1
# triple all the numbers given in list
# from Tools.scripts.mailerdaemon import x

# numbers = (1, 2, 3, 4, 5, 6, 7)
# print("Original list: ", numbers)
# result = map(lambda x: x + x + x, numbers)
# print("\nTriple of said list numbers:")
# print(list(result))

# 2
# Separate even odd number from given list

# Python code to split into even and odd lists
# Function to split
def Split(mix):
    ev_li = []
    od_li = []
    for i in mix:
        if (i % 2 == 0):
            ev_li.append(i)
        else:
            od_li.append(i)
    print("Even lists:", ev_li)
    print("Odd lists:", od_li)
  
# Driver Code
mix = [2, 5, 13, 17, 51, 62, 73, 84, 95]
Split(mix)  


# 3
# Print all string in lower case from given tuple
# myStr = "How ARE You TODAY?";
# print(myStr.lower());


# 4
# Print square root of numbers given in list
from typing import List


def square_num(n):
    return n * n


nums = [4, 5, 2, 9]
print("Original List: ", nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))

# 5
# Eliminate duplicate letter from given string
string = "geeksforgeeks"
p = ""
for char in string:
    if char not in p:
        p = p + char
print(p)
k = list("geeksforgeeks")

# 6
# Print table of any number
# n = int(input("Enter the number: "))
# for i in range(1, 11):
#  print(n, "x", i, "=", n * i)

# 7
# Add two list

list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = [1, 2, 3]
list4 = []
for i in range(0, len(list1)):
    list4.append(list1[i] + list2[i] + str(list3[i]))
print(*list4)

# 8
#  built in function from given list.

num = 9.3

print('type:',
      type(num).__name__)
num = int(num)

print('converted value:', num,
      ', type:', type(num).__name__)

# 9
# Reverse given set

seqTuple = ('a', 'f', 'z', 'a', 'l')
print(list(reversed(seqTuple)))

seqRange = range(1, 5)
print(list(reversed(seqRange)))

# 10
# Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case
car_dict = {'a': 'Mercedes-Benz', 'b': 'BMW', 'c': 'Ferrari', 'd': 'Lamborghini', 'e': 'jeep'}
# adding an'_'to the end of each value car_dict=
dict(map(lambda x: (x[0], x[1] + '_'), car_dict.items()))
print('The modified dictionary is :')
print(car_dict)
