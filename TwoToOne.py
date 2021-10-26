"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters 
- each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

s1 = "xyaabbbccccdefww"
s2 = "xxxxyyyyabklmopq"

def longest(s1, s2):
    # make it a list, sort it and convert it to set to exclude doubles
    s1 = list(s1)
    s1.sort()
    set1 = s1
    set1 = set(set1)
    s1 = set1

    s2 = list(s2)
    s2.sort()
    set2 = s2
    set2 = set(set2)
    s2 = set2
    
    if s1 > s2:  
        return s1
    else:
        return s2

print(longest(s1,s2))