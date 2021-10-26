import string
import unittest

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


class myTest(unittest.TestCase):
    def test(self):
        self.assertEquals(longest("aretheyhere", "yestheyarehere"), "aehrsty")