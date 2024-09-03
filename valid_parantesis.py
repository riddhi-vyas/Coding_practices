class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                my_stack.append(s[i])
            elif s[i] == ')':
                if len(my_stack) != 0 and my_stack[-1] == '(':
                    my_stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if len(my_stack) != 0 and my_stack[-1] == '[':
                    my_stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(my_stack) != 0 and my_stack[-1] == '{':
                    my_stack.pop()
                else:
                    return False
            
        if len(my_stack) != 0:
            return False

        return True
