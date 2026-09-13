class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_string = float("inf")

        for string in strs:
            smallest_string = min(smallest_string, len(string))

        result = []
        
        for i in range(smallest_string):
            char_to_compare = strs[0][i]
            for string in strs:
                if string[i] != char_to_compare:
                    return ''.join(result)
            
            result.append(char_to_compare)

        return ''.join(result)


        