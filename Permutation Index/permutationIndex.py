# Link to my solution on CheckiO:
# https://py.checkio.org/mission/permutation-index/publications/hawkinmogen/python-3/first/share/faab6135192124085acf74e388e1ea30/

from typing import Tuple
import math

def permutation_index(numbers: Tuple[int])->int:
    result=0
    succeedingNumbersLessThan=[]
   
   #for each number x, find how many succeeding numbers are less than x and append it to list
    for x in numbers:
        count=0
        for i in numbers[numbers.index(x):]:
            if i<x:
                count+=1
        succeedingNumbersLessThan.append(count)
    #Loop A ^
    
    #enumerates the list such that [1,2,3,4] would become [[3,1],[2,2],[1,3],[0,4]]
    enumerated = list(zip(range(len(succeedingNumbersLessThan)-1, -1, -1), succeedingNumbersLessThan))
   
   # uses the formula: x*3!+y*2!+z*1!+w*0 where x,y,z,w are derived from loop A
    for x in enumerated:
        a=math.factorial(x[0])
        b=x[1]
        result+=a*b
    return result+1
    
