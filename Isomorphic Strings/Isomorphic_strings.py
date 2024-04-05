def isIsomorphic(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    
    mapS = {}
    mapT = {}

    for Schar, Tchar in zip(s, t):

        if Schar in mapS:
            if mapS[Schar] != Tchar:
                return False
        
        else:
            if Tchar in mapT:
                return False
            
            mapS[Schar] = Tchar
            mapT[Tchar] = Schar
    
    return True

def main() -> None:
    print(isIsomorphic('apricot', 'cazique'))

main()