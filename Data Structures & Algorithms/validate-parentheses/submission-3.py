class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                continue
            else: 
                if not stack: #not empty
                    return False
                prevInput = stack.pop()
                if (char == ")" and prevInput == "(") or (char == "}" and prevInput == "{") or (char == "]" and prevInput == "["):
                    continue
                else:
                    return False
        if stack: #not empty
            return False

        return True