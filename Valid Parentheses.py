class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={'(': ')', '{': '}', '[':']'}
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if not stack or stack[-1]!=match[char]:
                    print(False)
                    break
        if not stack:
            print(True)
        else:
            print(False)
    
