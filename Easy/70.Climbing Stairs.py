"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

my analysis:
after write down the out come:
n = 0 1 2 3 4 5 6...
a = 0 1 2 3 5 8 13...
"""
#initial simple recursion solution:
# Time Exceed
class Solution(object):
    def climbStairs(self, n):
        if (n<3):
            return n
        else:
            return (self.climbStairs(n-1)+self.climbStairs(n-2))