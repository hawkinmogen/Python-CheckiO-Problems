# Link to my solution on CheckiO:
# https://py.checkio.org/mission/reverse-roman-numerals/publications/hawkinmogen/python-3/brute-force/share/c66e9dc3af41f7a4fd759ce448a2bda4/
def reverse_roman(roman_string):
    result=0
    NUMERALS={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,
              'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    pairs=[]
    skip=False
    
    if len(roman_string)==1:
        result+=NUMERALS[roman_string[0]]
        return result
        
    for x in roman_string:
        
        if roman_string.index(x)==len(roman_string)-1:
              break
        #if x is larger than the charcter after it and skip==False, append it to 'pairs'
        if NUMERALS[x]>=NUMERALS[roman_string[roman_string.index(x)+1]] and skip==False:
            pairs.append(x)
       
        # else add x and the charcter next to it, skip is used to skip over charcters already in 'pairs'
        elif skip==False:
            pairs.append(x+roman_string[roman_string.index(x)+1])
            skip = not skip
        
        #if needed, this will change skip back to False after 'skipping' the statements above
        else:
            skip = not skip
   
    #adds the last character to 'pairs' if it has not been already
    if roman_string[-1]!= pairs[-1] and len(pairs[-1])!=2:
        pairs.append(roman_string[-1])
        
    for x in pairs:  
         result+=NUMERALS[x]
            
    return result
