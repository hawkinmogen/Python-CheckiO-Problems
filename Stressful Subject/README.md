https://py.checkio.org/mission/stressful-subject/publications/hawkinmogen/python-3/first/share/e284223d31fc37ba99f66dc7e1de7478/

The function should recognise if a subject line is stressful. 
A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks, 
and/or contains at least one of the following “red” words: "help", "asap", "urgent". 
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", 
even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.

Input: Subject line as a string.

Output: Boolean.

Example:

is_stressful("Hi") == False

is_stressful("I neeed HELP") == True
