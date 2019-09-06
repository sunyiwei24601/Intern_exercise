class Solution:
    def candy(self, ratings):
        new_slope = 0
        old_slope = 0
        up = 0
        down = 0
        len_ = len(ratings)
        candies = 0

        for i in range(1, len_):
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            elif ratings[i]  < ratings[i - 1]:
                new_slope = -1
            else:
                new_slope = 0
            
            # first one means i is in the valley of  a hill
            # second one means i is the last up road of ratings
            if (new_slope >= 0 and old_slope < 0) or (old_slope > 0 and new_slope == 0 ):
                # max(up, down) is to add the peak , the peak don't need to add 1 because the valley (1) is calculated in another slope actually
                candies += self.count(up) + self.count(down) + max(up, down)
                up = 0
                down = 0

            if (new_slope > 0):
                up += 1
            if (new_slope < 0):
                down += 1
            if (new_slope == 0):
                candies += 1
            
            old_slope = new_slope
        # this line add the last hill 
        candies += self.count(up) + self.count(down) + max(up, down) + 1
        
        return candies
            



    def count(self, n):
        return  (n * (n + 1) )/ 2

if __name__ == "__main__":
    s = Solution()
    print(s.candy([1,2,3,4,5,3,2,1,2,6,5,4,3,3,2,1,1,3,3,3,4,2]))