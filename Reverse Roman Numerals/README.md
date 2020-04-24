https://py.checkio.org/en/mission/reverse-roman-numerals/

You are given a Roman number as a string and your job is to convert this number into its decimal representation.

A valid Roman number, in the context of this mission, 
will only contain Roman numerals as per the below table and follow the rules of the subtractive notation.


Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

Input: A roman number as a string.

Output: The decimal representation of the roman number as an int.

Example:

reverse_roman('VI') == 6

reverse_roman('LXXVI') == 76

reverse_roman('CDXCIX') == 499

reverse_roman('MMMDCCCLXXXVIII') == 3888
