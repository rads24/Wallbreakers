class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        #create a list of morse rep for each word
        morseList = []
        for word in words:
            temp = ""
            for char in word:
                temp += code[ord(char) - 97]
            morseList.append(temp)
            
        return len(set(morseList))