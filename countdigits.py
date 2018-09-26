def countDigit(n): 
    if n == 0: 
        return 0
    return 1 + countDigit(n // 10) 
 
 
n = 98401398045
print ("Number of digits : % d"%(countDigit(n))) 
