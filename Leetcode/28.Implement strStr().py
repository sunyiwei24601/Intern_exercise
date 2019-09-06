class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            needle_len = len(needle)
            stack_len = len(haystack)
            
            for i in range(stack_len - needle_len + 1): 
                if haystack[i:i+needle_len] == needle:
                    return i 
            return -1

if __name__ == "__main__":
    s = Solution()
    print(s.strStr("mississipi", 'issip'))