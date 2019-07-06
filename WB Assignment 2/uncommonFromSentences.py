class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # symmetric_difference
        
        listA = A.split()
        setA = set(listA)
        dictA = dict([(k, listA.count(k)) for k in listA])
        listB = B.split()
        setB = set(listB)
        dictB = dict([(k, listB.count(k)) for k in listB])
        
        onlyInOne = list(setA.symmetric_difference(setB))
        res = []
        for word in onlyInOne:
            if word in setA and dictA[word] == 1: 
                res.append(word)
            elif word in setB and dictB[word] == 1:
                res.append(word)
                
        return res
    
    #read about how split works (causing issues)
    # single letters are getting counted twice if I do A.split() in for loop
    