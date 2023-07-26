def poli(str):
    strRev = str[::-1]
    if strRev == str:
        return True
    return False

############################
def coded_string(str):
    temp =""
    char_map = {
        "P": "9",
        "T": "0",
        "S": "1",
        "H": "6",
        "A": "8",
    }
    for char in str:
        temp += char_map.get(char, char)
    # for i in str:
    #     if i == "P":
    #         temp += "9"
    #     elif i == "T":
    #         temp += "0"    
    #     elif i == "S":
    #         temp += "1"    
    #     elif i == "H":
    #         temp += "6"    
    #     elif i == "A":
    #         temp += "8"
    #     else:
    #         temp += i          
    return temp 
    
############################
def reverse_even_length(str):
    temp = str.split(" ")
    newStr = []
    for i in temp:
        if len(i) % 2 == 0:
            newStr.append(i[::-1])
        else:
            newStr.append(i)    
    return " ".join(newStr)
############################
def remove_vowels(str):
    char_str = {
        "a":"",
        "e":"",
        "i":"",
        "o":"",
        "u":"",
    }
    temp =""
    for char in str:
        temp += char_str.get(char, char)
    return temp    
############################
def perfect_numbers(number):
    if number < 0:
        return []

    perfect = []

    for num in range(2, number + 1):
        to = int(num / 2) + 1
        divisors_sum = sum([i for i in range(1, to) if num % i == 0])
        if divisors_sum == num:
            perfect.append(num)

    return perfect

# print(perfect_numbers(500))
############################
def quadratic_result():
    number1 = input("Please enter the first list: ").split(" ")
    number2 = input("Please enter the second list: ").split(" ")
    if len(number1) != len(number2):
        return "Error"
        
    new_lst = []
    for i in range(len(number1)):
        if pow(int(number1[i]), 2) == int(number2[i]):
            new_lst.append(int(number1[i]) + int(number2[i]))
        else:
            return
    return(new_lst)                    
# print(quadratic_result())
############################
def is_bigger(*args):
    for num in range(len(args) - 1):
        if args[num] + 2 == args[num + 1]:
            continue
        else:
            return False
    return True    
# print(is_bigger(1,3,5,7,9))

############################
def print_details(name, salary = 9000):
    if not name:
        return "You must enter a name"

    return f"Name: {name}, Salary: {salary}"
# print(print_details("Dani", 7800))

############################
def Integer():
    number = int(input("Please enter a number: "))
    lst= []
    counter = 1
    
    while number != -1:
        lst.append(number)
        number = int(input("Please enter a number: "))
    
    lst.sort()
    print("The numbers are")    
    
    for num in range(len(lst) - 1 ):
       if lst[num] == lst[num + 1]:
           counter+=1
       else:
           print(f"entered {counter} times {lst[num]}")
           counter = 1  
    
    if lst:  # Check if the list is not empty
        print(f"entered {counter} times {lst[-1]}")        
        
# Integer()        
                
    