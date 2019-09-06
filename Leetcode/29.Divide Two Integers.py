class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = (1 << 31) - 1
    
        if divisor == 0:
            return MAX_INT
        
        minus = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        
        # find the largest base
        count = 0
        origin_divisor = divisor
        while divisor <= dividend:
            divisor = divisor << 1
            count += 1
        divisor = divisor >> 1
        count -= 1
        
        # divide defination
        while dividend >= origin_divisor:
            dividend -= divisor
            res += 1 << count
            
            while dividend > origin_divisor and dividend < divisor:
                divisor = divisor >> 1
                count -= 1
        
        if minus:
            return -res if res <= 1 << 31 else MAX_INT
        else:
            return res if res <= MAX_INT else MAX_INT
    
    def d(self, dividend, divisor):
        MAX_INT = (1<<31) - 1
        # when divisor = 0
        if divisor == 0:
            return MAX_INT
        # when symbol is negative
        minus = (divisor > 0 and dividend < 0) or (dividend > 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        #choose the base divisor
        original_divisor = divisor
        count = 0
        while dividend >= divisor:
            divisor = divisor << 1
            count += 1
        
        #get the max multiple of divisor which smaller than dividend
        divisor = divisor >> 1
        count -= 1

        #imitate the division, divide 2^n times of divisor, dividend minus it, and do it again,each time change the divisor, n decrease
        res = 0
        while dividend >= original_divisor:
            
            dividend -= divisor
            res += 1 << count 
            # when divisor is just smaller than remained dividend, jump out of loop
            # dividend > original_divisor to ensure there is enough numbers to be divided after minus divisor
            while dividend > original_divisor and dividend < divisor:
                divisor = divisor >> 1
                count -= 1
        
        # negative integer ranges more than positive ones
        if minus:
            return -res if res <= 1 << 31 else MAX_INT
        else:
            return res if res <= MAX_INT else MAX_INT
                
if __name__ == "__main__":
    s = Solution()
    print(s.d(288, -5))
