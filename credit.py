from cs50 import get_string,get_int

number = get_string("Card Number: ")

def Luhn(string):
    sum1 = 0 
    #first list incorporates the numbers which are going to be multiplied by 2 
    first = []
    
    # second list will incorporate the numbers other than those which are multiplied by 2
    second = []
    
    size = len(string)
    
    #reversed range to iterate the given string
    for i in range(size-2,-1,-2):
        if i<0:
            break
        first.append(int(number[i]) *2)
    for k in range(size-1,-1,-2):
        if k<0:
            break
        second.append(int(number[k]))
    for m in first:
        m = str(m)
        if len(m) == 2:
            sum1 += int(m[0]) + int(m[1])
        else:
            sum1 += int(m)
    for l in second:
        sum1 += int(l)
    if sum1%10 == 0:
        return True
    return False
    
#the function in which all the checking are being made
def check_validation(n):
    size = len(n)
    if size != 13 and size != 15 and size != 16:
        return False
    else:
        if Luhn(n):
            return True
        else:
            return False
        
#the function that determinate the fact that where a card number belong to
def check_type(number):
    if number[0] == "4" :
        print("VISA")
    elif number[0:2] == "34" or number[0:2] == "37":
        print("AMEX")
    elif number[0] == "5" and (number[1] == "1" or number[1] == "2" or number[1] == "3" or number[1] == "4" or number[1] == "5"):
        print("MASTERCARD")
    

if Luhn(number) and check_validation(number):
    check_type(number)
else:
    print("INVALID")
