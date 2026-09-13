class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {}
        hash_map["}"] = "{"
        hash_map["]"] = "["
        hash_map[")"] = "("

        stack = []

        for bracket in s:
            if bracket in hash_map:
                if len(stack) == 0 or hash_map[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0