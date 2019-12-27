"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

class Solution(object):

    def climbStairs(self, n):
        self.memo = {0: 1, 1: 1}  # store the initial results in the dictionray

        def climb(n):  #interviewers like to see that you know object oriented programming
            """
            :type n: int
            :rtype: int
            """
            if n in self.memo:
                return self.memo[n]

            m = climb(n - 1) + climb(n - 2)

            self.memo[n] = m  #store the value of m into a dictionary representing the calculation number 9

            return m

        climb(n)
        return self.memo[n]


t = Solution()
print(t.climbStairs(32))