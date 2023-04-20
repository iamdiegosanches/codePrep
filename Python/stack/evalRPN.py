class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack.append(tokens[0])
        i = 1
        while i < len(tokens):
            if tokens[i] in ['+', '-', '*', '/']:
                x = stack.pop()
                y = stack.pop()
                result = eval(y + tokens[i] + x)
                stack.append(str(math.floor(result) if result > 0 else math.ceil(result)))
            else:
                stack.append(tokens[i])
            i += 1
            
        return int(stack[0])
