class Solution:
    memo = {}
    def myPow(self, x: float, n: int) -> float:
        if n == 1: return x 
        if n == 0: return 1
        if n == -1: return 1/x
        if self.memo.get(n):
            return self.memo.get(n)
        else:
            i = n // 2
            j = n - i
            self.memo[n] = self.myPow(x, i) * self.myPow(x, j)
            return self.memo[n]
            
if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.1,3))