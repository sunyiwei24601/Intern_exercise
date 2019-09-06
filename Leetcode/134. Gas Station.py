class Solution:
    def canCompleteCircuit(self, gas, cost):
        len_ = len(gas)
        cur, start, total = 0,0,0
        for i in range(len_):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i + 1
        
        if total < 0:
            return -1
        else:
            print(total)
            return start

if __name__ == "__main__":
    s = Solution()
    gas = [4,5,2,6,5,3]
    cost = [3,2,7,3,2,9]
    print(s.canCompleteCircuit(gas, cost))