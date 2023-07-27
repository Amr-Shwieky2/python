# from math import pi 
# def radios(r):
#     return pi * pow(r,2)
# print(radios(int(input("Please enter the radius of the circle: "))))

# ===================================
# import math 
# def angleCos(angle):
#     return math.cos(angle)
# print(angleCos(int(input("Please enter the angle: "))))

# ===================================
# import random

# random.seed(789)
# lst = list(range(2,674,34))
# randomLst = [random.choice(lst) for num in lst]
# print(randomLst[1])

# ===================================
# lst = list(range(0,201))
# lst_num = [num for num in lst if num % 5 == 0 if num % 7 == 0]
# print(lst_num)

# ===================================
# def modify_list(lst):
#     lst_num = [(num /2)*3 for num in lst]
#     print (lst_num)

# modify_list([1,2,3,4,5])
#=========================================
# def remove_duplicates(*args):
#     lst = [ele for ele in args]
#     temp = list(set(lst))
#     temp.sort()
#     return temp 

# print(remove_duplicates('Avi','Dani','Yossi','Gal','Ben','Avi','Ben','Tom','Gal','Yossi'))
#=========================================
# num = int(input("Please enter a number: "))

# def square():
#     global num
#     number = num **2

# square()
# print(num)

#=========================================
# def dict_mean(dic):
#     for ele in dic:
#         dic[ele] += dic[ele]
#     return dic[ele] / len(dic)
      
# my_dict = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5
# }
# dict_mean(my_dict)      
        
#=========================================
# def swap_index(lst):
#      numbers = input("Please enter 2 numbers with comma: ").split(",")
#      temp = lst[int(numbers[0])]
#      lst[int(numbers[0])] = lst[int(numbers[1])]
#      lst[int(numbers[1])] = temp
#      return lst

# # print(swap_index(['a','b','c','d','e']))  
# print(swap_index([1,'b','c',2,'e']))

#=========================================
# def replace_letter(str, let1, let2):
#     # temp =""
#     # for s in str:
#     #     if s == let1:
#     #         temp += let2
#     #     else:
#     #         temp += s
#     if not str:
#         return ""  # Return an empty string if the input string is empty

#     temp = [let2 if s == let1 else s for s in str]
#     print("".join(temp))
                     
# replace_letter("Hello World", 'o', 'O')    

#=========================================
# def mod_tuples(tup1, tup2):
#     return tuple([i % j for i,j in zip(tup1,tup2)])
# print(mod_tuples((10, 4, 5, 6),(5, 6, 7, 5)))

#=========================================
def build_dict(lst1, lst2):
    return {val1:val2 for val1,val2 in zip(lst1, lst2)}
    
print(build_dict([1, 2, 3, 4], ['a', 'b', 'c', 'd']))