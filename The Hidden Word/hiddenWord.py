# Link to my solution on CheckiO:
# https://py.checkio.org/mission/hidden-word/publications/hawkinmogen/python-3/rows-and-columns/share/3dc3c668466f552b39e35657b8845c95/

def checkio(text, word):
    text=text.lower()
    word=word.lower()
    text=text.replace(' ','')
    text=text.split("\n")
    wordLength=len(word)
    verticalSlices=[]
    result=[]
    
    #If word is in one row, return indices as requested
    for x in text:
      if word in x:
        result.append(text.index(x)+1)
        result.append(x.index(word)+1)
        result.append(text.index(x)+1)
        result.append(x.index(word)+wordLength)
        return result
    
    #else, make all rows the same length and make a list containing each column
    maxLineLength=len(max(text))
    for line in text:
        if len(line)!=maxLineLength:
          text[text.index(line)]=line.ljust(maxLineLength,'.')
    for line in text:
        if len(line)>maxLineLength:
            difference=(len(line)-maxLineLength)*-1
            text[text.index(line)]=line[0:difference]
    
    #adds each column to the list 'verticalSlices'
    for letter in range(0,maxLineLength):
        verticalSlice=""
        for line in range(0,len(text)):
            verticalSlice+=(text[line][letter])
        verticalSlices.append(verticalSlice)
    
    #if the word is in a column, return its indices as requested
    for slices in verticalSlices:
        if word in slices:
         result.append(slices.index(word)+1)
         result.append(verticalSlices.index(slices)+1)
         result.append(slices.index(word)+wordLength)
         result.append(verticalSlices.index(slices)+1)
         return result
