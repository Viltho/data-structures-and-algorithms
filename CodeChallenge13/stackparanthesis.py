from CodeChallenge10.stack import Stack

def stackparanthesis(s):
        stack = Stack()
        if len(s)==1:
            return False
        x = [*s]
        for i in x:
            indx = x.index(i)
            if i not in "(){}[]":
                x.pop(indx)
        for i in x:
            if i in '([{':
                stack.push(i)
            else:
                if stack.get_size() == 0:
                    return False
                elif i == ")" and stack.top.value != '(':
                    return False
                elif i == "]" and stack.top.value != '[':
                    return False
                elif i == "}" and stack.top.value != '{':
                    return False
                else:
                    stack.pop()
                    
        if stack.get_size() > 0:
            return False
        else:
            return True