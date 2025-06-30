#factorial code with recurssion function 
def factorial(n):  
    if n ==0 :      # base recrsion to stop the infinite loop 
        return 1 
    else :
         return n* factorial(n-1)   # recursive here the function is calling itself  
print(factorial(6))





