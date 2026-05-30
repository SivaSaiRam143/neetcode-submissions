class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for x in s:
            if x in ['{', '(', '[']:
                my_stack.append(x)
            else:
                if len(my_stack) > 0:
                    if (x == '}' and my_stack[-1] == '{') or (x == ']' and my_stack[-1] == '[') or (x == ')' and my_stack[-1] == '('):
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
            print(x)
            print(my_stack)
        print(my_stack)
        return len(my_stack) == 0

        