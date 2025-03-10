
from math import log10

class Solution:

    def miniLength(self, s):
        X, Y = s.split()

        res = log10(X - pow(26, Y))
        return res if int(res) >= res else res + 1