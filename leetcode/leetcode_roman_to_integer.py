class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        num = 0
        previous = 0
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(n):
            c = s[i]
            value = values.get(c)
            if value > previous:
                num += value - 2*previous
            else:
                num += value
            previous = value
        return num