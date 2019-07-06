from collections import defaultdict
class Solution:
    def generateSubDomains(self, domain):
        sd = domain.split('.')
        res = []
        for i in range(len(sd)):
            temp = ""
            for j in range(i, len(sd)):
                temp += sd[j] + '.'
            res.append(temp.strip('.'))
        return res
            
        
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainDict = defaultdict(int)
        
        for cp in cpdomains:
            count, domain = cp.split()
            subDomains = self.generateSubDomains(domain)
            for domain in subDomains:
                domainDict[domain] += int(count)
        
        countList = []
        for key, value in domainDict.items():
            temp = "%d %s" % (domainDict[key], key)
            countList.append(temp)
        
        return countList
        
            