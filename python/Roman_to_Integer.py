

def romanToInt(number):
    val = ""
    while number > 0:
        temp = helper(number)
        if temp == "M":
            number -= 1000
            val += temp 
        elif temp == "D":
            number -= 500
            val += temp 
        elif temp == "C":
            number -= 100
            val += temp 
        elif temp == "L":
            number -= 50
            val += temp 
        elif temp == "X":
            number -= 10
            val += temp 
        elif temp == "V":
            number -= 5
            val += temp 
        elif temp == "I":
            number -= 1
            val += temp 
    return val           
        
        
def helper(number):
    if number >= 1000:
        return "M"
    elif number >= 500:
        return "D"
    elif number >= 100:
        return "C"
    elif number >= 50:
        return "L"
    elif number >= 10:
        return "X"
    elif number >=  5:
        return "V"
    elif number >=  1:
        return "I"        

print(romanToInt(12))    
print(romanToInt(27))    