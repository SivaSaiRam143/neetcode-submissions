class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for x in tokens:
            if x in ["+", "-", "*", "/"]:
                a = my_stack.pop()
                b = my_stack.pop()
                if x == "+":
                    my_stack.append(int(a)+int(b))
                elif x == "-":
                    my_stack.append(int(b)-int(a))
                elif x == "/":
                    my_stack.append(int(b)/int(a))
                elif x == "*":
                    my_stack.append(int(b)*int(a))
            else:
                my_stack.append(x)
        return int(my_stack[0])       