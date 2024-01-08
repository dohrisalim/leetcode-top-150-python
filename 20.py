class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rightChars = set([")","}","]"])
        for char in s:
            if char == '(': stack.append(')')
            if char == '{': stack.append('}')
            if char == '[': stack.append(']')

            if char in rightChars and len(stack) == 0: return False

            if char in rightChars and len(stack) > 0:
                if char != stack[-1]:
                    print('here')
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False