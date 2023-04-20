class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        items = path.split("/")
        for item in items:
            if item == "..":
                if stack: stack.pop()
            elif item and item != '.':
                stack.append(item)
            
        return '/' + '/'.join(stack)
