def allPaths(current, end, possibleSteps, path, result):
    # Returns all possible permutations of staircase paths...
    # where 'end' is the length of the staircase and 'possibleSteps' are...
    # the different sized steps you are allowed to take. i.e. 1 step, 2 steps, etc.
   
   if current>end:
        return
    if current==end:
        result.append(path)
        return
    for step in possibleSteps:
        allPaths(current+step, end, possibleSteps, path+[step], result)
    return result

def checkio(numbers):
    numbers.append(0)
    possibleSums=[]
    # calls allPaths on a staircase length of len(numbers) where you can take...
    # either 1 or 2 steps at a time
    possiblePaths=allPaths(0, len(numbers), [1,2], [], [])
    
    #calculate the sum of all possible paths and then return the max sum
    for x in possiblePaths:
        pathValue=0
        i=-1
        for j in x:
          i+=j
          pathValue+=numbers[i]
        possibleSums.append(pathValue)
    return max(possibleSums)
