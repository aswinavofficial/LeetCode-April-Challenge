class Solution(object):
    def isHappy(self, n):
        t = n
        r = 0
        l = []
        l.append(n)
        while True:
            r =0
            while t > 0:
                r = r+ pow(t%10,2)
                t = t//10
            if r == 1:
                return True
            if r in l or r == 0:
                return False
            l.append(r)
            t = r
