class Solution:
    def generateParenthesis(self, n: int):
        solution = []
        def backtrack(st='', left=0, right=0):
            if len(st) == 2*n:
                solution.append(st)
                return 0
            if left > right:
                backtrack(st+')', left, right+1)
            if left < n :
                backtrack(st+'(', left+1, right)
                
        backtrack()
        return solution

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(4))     