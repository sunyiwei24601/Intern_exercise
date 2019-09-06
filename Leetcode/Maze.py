class Solution:
    def find_route(self, mazes, start):
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        len_ = len(mazes)
        routes = []
        final_position = (len_ - 1, len_ - 1)

        def back(pos_list, current_position):
            if current_position == final_position:
                routes.append(pos_list)
                print("successful")
                return True
            for i,j in directions:
                next_position = (current_position[0] + i, current_position[1] + j)
                if self.isValid( len_, mazes, next_position):
                    # create new pos list in case conflicts with each other
                    new_pos_list = pos_list[:] + [next_position]
                    mazes[next_position[0]][next_position[1]] = 0
                    back(new_pos_list, next_position)
                    # set mazes back to the past to make sure this backtrack will not influence the others
                    mazes[next_position[0]][next_position[1]] = 1
        back([], start)
        return(routes)

    def isValid(self, nums, mazes, next_position):
        i = next_position[0]
        j = next_position[1]
        # we can use range to test whether i,j is over boundaries
        if i in range(nums) and j in range(nums) and mazes[i][j]:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    nums = [[1, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0], 
            [0, 0, 1, 0, 1, 0], 
            [0, 1, 1, 1, 0, 0], 
            [0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 1]]
    print(s.find_route(nums, (0,0)))
