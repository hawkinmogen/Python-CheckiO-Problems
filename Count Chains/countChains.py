# My solution on CheckiO:
# https://py.checkio.org/mission/count-chains/publications/hawkinmogen/python-3/first/share/49303c9a48845ce11947722bea71b74f/

from typing import List, Tuple
import math
def testIntersection(a,b):
    #Use the distance formula to find the distance between the centers of two circles
    distSq = (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])  
    radSumSq = (a[2] + b[2]) * (a[2] + b[2])  
    
    if a[2]>b[2]:
        smallerRadius=b[2]
        largerRadius=a[2]
    else:
        smallerRadius=a[2]
        largerRadius=b[2]
    #if the distance**2 is < the (sum of the radii)**2, the two circles are either 'linked'...
    #or one lies completely inside the other
    #if the second condition is True, then one circle does not lie completely within the other...
    # thus they are 'linked' and True is returned 
    if (distSq < radSumSq) and (math.sqrt(distSq)+smallerRadius)>largerRadius: 
        return True
    else:
        return False


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    links=[]
    #appends all chain links to 'links' as well as any circles which are not linked to another
    for circ in circles:
        newchain = [circ]
        notConnected = []
        for chain in links:
            if any(testIntersection(c, circ) for c in chain):
                newchain += chain
            else:
                notConnected.append(chain)
        links = [newchain] + notConnected
    
    return len(links)
