# Link to my solution on CheckiO:
# https://py.checkio.org/mission/roman-numerals/publications/hawkinmogen/python-3/first/share/7e771838405cfd368ffb68b6f0e16292/

def checkio(data):
    result=""
    NUMERALS=(('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),
              ('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1))
    #Adds the largest roman numeral that is < 'data' to 'result' and substracts the value from 'data'...
    #until 'data'= 0
    for numeral, number in NUMERALS:
        while number<=data:
            data-=number
            result+=numeral
    return result
