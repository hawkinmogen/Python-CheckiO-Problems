# Link to my solution on CheckiO:
# https://py.checkio.org/mission/similar-triangles/publications/hawkinmogen/python-3/tested-using-sidesideside/share/727d31105da5498376f29f2b56bed085/

from typing import List, Tuple
Coords = List[Tuple[int, int]]
import math
def side_lengths(coords_1):
    triangleSides=[]
    
    #Calculate the length of each line using the distance formula with two points
    side1= math.sqrt((abs((coords_1[0][0]-coords_1[1][0]))**2)+(abs((coords_1[0][1]-coords_1[1][1]))**2))
    side2= math.sqrt((abs((coords_1[1][0]-coords_1[2][0]))**2)+(abs((coords_1[1][1]-coords_1[2][1]))**2))
    side3= math.sqrt((abs((coords_1[0][0]-coords_1[2][0]))**2)+(abs((coords_1[0][1]-coords_1[2][1]))**2))
    triangleSides.append(side1)
    triangleSides.append(side2)
    triangleSides.append(side3)
    
    #sort the sides by length so that later each triangle side is compared with the correct side of the 2nd triangle
    triangleSides.sort()
    return triangleSides


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    sides1= side_lengths(coords_1)
    sides2= side_lengths(coords_2)
    
    #Test for similarity between two triangles using the 'side,side,side' method
    # If all side lengths of both triangles are in the same ration, the two triangles are similar (return True)
    if sides1[0]/sides2[0]==sides1[1]/sides2[1]==sides1[2]/sides2[2]:
      return True
    else:
        return False
