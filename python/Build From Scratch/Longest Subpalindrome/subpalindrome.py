
def longest_subpalindrome(text):
    if text == '': 
        return (0,0)
    
    candidates = [grow(text,start, end)
                    for start in range(len(text))
                    for end in (start, start+1)]

    return max(candidates, key = lambda x: x[1] - x[0] )


def grow(text, start, end):
    while start > 0 and end < len(text) and text[start - 1].upper() == text[end].upper():
        start -= 1
        end += 1
    return (start, end)


    
print(longest_subpalindrome("tenet"))

