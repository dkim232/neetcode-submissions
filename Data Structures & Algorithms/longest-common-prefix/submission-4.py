class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstWord = strs[0]

        for i in range(len(firstWord)): #only iterate over the length of the first word
            for word in strs[1:]: #other words
                if i == len(word) or word[i] != firstWord[i]:
                    return firstWord[:i]
                #else, continue since valid
        #here: all words same
        return firstWord