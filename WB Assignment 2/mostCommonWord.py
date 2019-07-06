import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]',' ',paragraph)
        paragraphList = paragraph.split()
        
        wordCount = collections.Counter(paragraphList)
        
        mostCommonWords = wordCount.most_common()
        
        for word, count in mostCommonWords:
            if word not in banned:
                return word