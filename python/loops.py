# number = int(input("Please enter a number: "))
# print(number**2)
#################################
# print("a", "b", end="!",sep= "$")
# print("c", "d", end="#",sep= "*")
#################################
# number1 = int(input("Please enter the first number: "))
# number2 = int(input("Please enter the second number: "))
# number3 = int(input("Please enter the third number: "))
# max_number = max(number1, number2, number3)
# min_number = min(number1, number2, number3)
# res = max_number - min_number
# # if number1 < number2 :
# #     if number3 < number2:
# #         if number1 < number3:
# #            res = number2 - number1
# #         else:
# #             res = number2 - number3    
# #     else:
# #         res = number3 - number1    
# # else:
# #     if number3 < number1:
# #         if number3 < number2:
# #             res = number1 - number3
# #         else:
# #             res = number1 - number2
# #     else:
# #         res = number3 - number2      
                         
# print(number1 + res, number2+res, number3+res, sep=" ") 
#################################

# lst = list(range(0,4))                        
# lst *= 3
# lst.insert(4, 100)
# lst.sort()
# print(lst)
#################################
# lst = list(range(10,0,-1))
# lst.sort()
# print(lst)
#################################
# lst = list(range(1,7))
# print(lst[1:4])
#################################
# lst = list(range(0,10))
# print(lst[::2])
#################################
# lst = list(range(0,100,10))
# print(lst)
#################################
# lst = list(range(32,45))
# lst.append(999)
# print(lst)
#################################
# lst = list(range(67,97,3))
# lst.insert(4, 888)
# print(lst)
#################################
# lst = list(range(0,99,14))
# tup = tuple(lst)
# print(tup)
#################################
# index = input("Input some comma seprated numbers : ")
# lst = index.split(",")
# tup = tuple(lst)
# print("List : " ,lst, sep=" ")
# print("Tuple : " ,tup, sep=" ")
##################################
# lst1 = list(range(0,100,10))
# lst2 = list(range(0,1000,100))
# my_dict = dict(zip(lst1, lst2))
# print(my_dict[30])
    
##################################
# lst = list(range(0,10))
# lst_2 = [num * 2 for num in lst]
# lst_3 = [num *3 for num in lst]
# lst_4 = [num *4 for num in lst]
# new_lst = lst_2 + lst_3 + lst_4

# # for num in lst_2:
# #     new_lst.append(num)
# # for num in lst_3:
# #     new_lst.append(num)
# # for num in lst_4:
# #     new_lst.append(num)
# lst = set(new_lst)
# print(len(lst))
##################################

# name = input("Please enter a name: ")
# if name[0] == "M":
#     print(True)
# else:
#     print(False)    
##################################

# name = input("Please enter the file name: ").split(".")
# print(name[-1])
##################################

# numbers = input("Please enter a list of numbers: ").split(" ")
# print(numbers)
##################################

# numbers = input("Please enter a list of numbers: ").split(",")
# New_numbers = [int(num) for num in numbers]
# sum = 0
# for i in New_numbers:
#     sum += i
# print(sum)     
##################################

# number1 = input("Please enter the first list: ").split(" ")
# number2 = input("Please enter the second list: ").split(" ")
# # check = False
# # for i in number1:
# #     if i in number2:
# #         check = True
# #         print(check)
# #         break
# # if check == False:    
# #     print(False)    
# common_elements = any(item in number2 for item in number1)
# print(common_elements)
##################################
number1 = input("Please enter the first number: ")
number2 = input("Please enter the second number: ")
counter = 0
for i in number1:
    if i in number2:
        counter +=1
print(counter)



##################################
