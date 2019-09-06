class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        a = list(a)
        a.reverse()
        a = [int(i) for i in a]
        b = list(b)
        b.reverse()
        b = [int(i) for i in b]
        if len_a > len_b:
            b += [0] * (len_a - len_b)
        else:
            a += [0] * (len_b - len_a)
        
        result = []
        count = 0
        for i in range(max(len_a, len_b)):
            p = a[i] + b[i] + count
            result.append( p % 2)
            if p >= 2:
                count = 1
            else:
                count = 0
        
        if count:
            result.append(count)
        result.reverse()
        s = ''
        for i in result:
            s += str(i)
        return s
    
    def addBinary2(self, a: str, b: str) -> str:
        num1 = list(a)
        num2 = list(b)
        c, d, sum = 0, 0, ''
        while num1 or num2:
            x, y = 0, 0
            #take number in the end out, if nothing ,set as -
            if num1:
                x = int(num1.pop())
            if num2:
                y = int(num2.pop())
            # // = int(/)
            c, d = (x + y + c)//2, (x + y + c)%2
            sum = str(d) + sum
        
        if c != 0:
            return str(c) + sum
        else:
            return sum
if __name__ == "__main__":
    s = Solution()
    print(s.addBinary('1011', '1010'))


        