from CodeChallenge10.stack import Stack

def stackparanthesis(s):
        stack = Stack()
        if len(s)==1:
            return False
        x = [*s]
        for i in x:
            print(i)
            if i not in "()[]{}":
                pass
            elif i in '([{':
                stack.push(i)
            else:
                if stack.get_size() == 0 or i == ")" and stack.top.value != '(' or i == "]" and stack.top.value != '[' or i == "}" and stack.top.value != '{':
                    return False
                elif i != "]" or i != ")" or i != "}":
                    stack.pop()
                    
        if stack.get_size() > 0:
            return False
        else:
            return True
        
print(stackparanthesis("{}{Code}[Fellows](())"))