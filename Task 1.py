# -*- coding: utf-8 -*-
"""

@author: shirz babish
ID 208849109

"""

# Task A: Writing a function

def my_func(x1, x2, x3):   
    func = ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
    
    if (x1+x2+x3)==0:
        return "Not a number – denominator equals zero"
    if x1 != float(x1):
       print("Error: parameters should be float")
    if x2 != float(x1):
        print("Error: parameters should be float")
    if x3 != float(x1):
       print("Error: parameters should be float")
         
    return func

# print(my_func(-3.0,1.0,24.0))


# Task B

def convert(hours, minutes):
    
    if(hours <= 0 or minutes <= 0):
        return("Input error!")
    
    return(hours * 60 * 60 + minutes * 60)

# for example
#print(convert(5,45))