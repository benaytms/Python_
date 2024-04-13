def minRemoveToMakeValid(s: str) -> str:
    # we make the string a list so we can iterate it
        S = list(s)

    # stack where there'll be the index of the invalid parentheses
        stack = []
    
    # if it's an opening parenthesis, then stack.append
    
    # if it's a closing parenthesis, then check if already there's a '(' 
    # if True then we remove the '(' with stack.pop from the stack because we found a valid match
    # if False then it means it's trying to close the parenthesis without even opening so we remove it by doing S[i] == ''
    
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            elif S[i] == ')': 
                if stack:
                    stack.pop()
                else: 
                    S[i] = ''

    # in case there were opening parentheses non-closed, we remove them passing through the string and if the index matches the
    # list of index from the stack, we remove the invalid parenthesis making it = ''
        for j in range(len(stack)):
            S[stack[j]] = ''

    # and after that we join the string again and return it
        return "".join(S) 

def main () -> None:
    # test string
    word = "(a(b(c))d)(())))"
    # print function return
    print(minRemoveToMakeValid(word))

if __name__ == '__main__':
    main()
