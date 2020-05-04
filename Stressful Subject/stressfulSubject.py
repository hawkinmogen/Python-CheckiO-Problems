#Link to my solution on CheckiO:
# https://py.checkio.org/mission/stressful-subject/publications/hawkinmogen/python-3/first/share/e284223d31fc37ba99f66dc7e1de7478/

#remove_duplicate removes consecutively repeated letters as well as any non-alphabetical characters
# remove_duplicate('hhhheeeeellllppp')='help' and remove_duplicate('h!e!l!p')= 'help'
def remove_duplicate(subj):
    subj=subj.lower()
    result=""
    current=""
    for x in subj:
        if x!=current and x.isalpha()==True or x==' ':
            result+=x
        current=x
    return result

def is_stressful(subj):
    keywords=['help','asap','urgent']
    
    #if 'subj' is all uppercase or ends with 3 or more exclamation points, return true
    if subj.isupper()==True or subj[len(subj)-3:].count('!')>=3:
        return True
    
    #call remove_duplicate on 'subj', if it contains any words in 'keywords' return True, otherwise return False
    condensed = remove_duplicate(subj)
    if any(x in condensed for x in keywords):
        return True
    else:
        return False
