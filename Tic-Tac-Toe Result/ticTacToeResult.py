#Link to my solution on CheckiO:
#https://py.checkio.org/mission/x-o-referee/publications/hawkinmogen/python-3/first/share/42015b116729e32664cb83915fb94233/

from typing import List

def checkio(result: List[str]) -> str:
    for x in result:
        if x.count('X')==3:
            return 'X'
        elif x.count('O')==3:
            return 'O'
    for x in range(0,3):
        if result[0][x]==result[1][x]==result[2][x] and result[0][x]!='.':
            return result[0][x]
    if result[0][0]==result[1][1]==result[2][2] or result[0][2]==result[1][1]==result[2][0]:
        if result[1][1]!='.':
         return result[1][1]
        else:
         return 'D'
    else:
        return 'D'
