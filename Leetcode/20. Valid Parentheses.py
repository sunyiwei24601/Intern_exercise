def check_pair(c1, c2):
    if abs(ord(c2) - ord(c1)) <=2:
        return True
    else:
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char in ("(", "[", "{")):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_element = stack[-1]
                if check_pair(last_element, char):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0 :
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("({)}"))