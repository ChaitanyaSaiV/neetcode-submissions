class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        length = float("inf")
        for word in strs:
            length = min(len(word), length)
        prev = None
        for i in range(length):
            print(i)
            for word in strs:
                if prev == None:
                    prev = word[counter]
                    continue
                if word[counter] == prev:
                    continue
                else:
                    return strs[0][:counter]
            counter += 1
            prev = None
        return strs[0][:counter]



            
            