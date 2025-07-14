def solutionEnd(word, ending):
    return ending == word[-(len(ending)):]      

print(solutionEnd("abcd", "cd"))            # word[-2:] -> -2, -1
print(solutionEnd("Hello", "ell"))
print(solutionEnd("Hello", "llo"))

def solutionFront(word, front):
    return front == word[:len(front)]

print(f"\n{solutionFront("abcd", "ab")}")          # word[:2] -> 0, 1
print(solutionFront("abcd", "bc"))
print(solutionFront("abcd", "cd"))

#! string[start:end]                        -> start, start+1, start+2, ..., end-1

#^ Cara sederhana
def solutionEnd(word, ending):
    return word.endswith(ending)

def solutionFront(word, front):
    return word.startswith(front)

print("="*15)
print(solutionEnd("abcd", "cd"))          
print(solutionEnd("Hello", "ell"))
print(solutionEnd("Hello", "llo"))

print(f"\n{solutionFront("abcd", "ab")}")         
print(solutionFront("abcd", "bc"))
print(solutionFront("abcd", "cd"))
