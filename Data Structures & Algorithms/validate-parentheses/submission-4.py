class Solution:
    def isValid(self, s: str) -> bool:
        brace_map = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        stack = []
        for char in s:
            if char in brace_map:
                if not stack or stack.pop() != brace_map[char]:
                    return False
                continue
            
            stack.append(char)
        return len(stack) == 0