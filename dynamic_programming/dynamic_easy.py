class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return 1 #only one way to climb 1 step
        
        a, b = 1, 1 #ways(0) = 1, ways(1) = 1

        for _ in range(2, n + 1):
            a, b = b, a + b #fibbonaci
        return b