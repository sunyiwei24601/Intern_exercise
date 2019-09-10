class Solution:
    def longestPalindrome(self, s):
        memory = {}
        if len(s) == 0:
            return ""
        def check_pattern(i, j):
            if (i,j) in memory:
                return memory[(i,j)]
            print(s[i:j+1])
            if i == j :
                if (i,j) not in memory:
                    memory[(i,j)] = True, s[i]
                return True,s[i]
            if i == j - 1:
                if s[i] == s[j]:
                    if (i,j) not in memory:
                        memory[(i,j)] = True, s[i:j+1]
                    return True,s[i:j+1]
            
            if s[i] == s[j]:
                result = check_pattern(i + 1, j - 1)
                if result[0]:
                    if (i,j) not in memory:
                        memory[(i,j)] = True, s[i] + result[1] + s[j]
                    return True, s[i] + result[1] + s[j]
                
            
            result_left = check_pattern(i+1, j)
            result_right = check_pattern(i, j-1)
            print(result_left, ",", result_right)
            if len(result_left[1]) > len(result_right[1]):
                if (i,j) not in memory:
                    memory[(i,j)] = False, result_left[1]
                return False, result_left[1]
            else:
                if (i,j) not in memory:
                    memory[(i,j)] = False, result_right[1]
                return False, result_right[1]
        
        result =  check_pattern(0, len(s) - 1)[1]
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("vaomxdtiuwqlwhgutkhxxhccsgvyoaccuicgybnqnslogtqhblegfudagpxfvjdacsxgevvepuwthdtybgflsxjdmmfumyqgpxatvdypjmlapccaxwkuxkilqqgpihyepkilhlfkdrbsefinitdcaghqmhylnixidrygdnzmgubeybczjceiybowglkywrpkfcwpsjbkcpnvfbxnpuqzhotzspgebptnhwevbkcueyzecdrjpbpxemagnwmtwikmkpqluwmvyswvxghajknjxfazshsvjkstkezdlbnkwxawlwkqnxghjzyigkvqpapvsntojnxlmtywdrommoltpbvxwqyijpkirvndwpgufgjelqvwffpuycqfwenhzrbzbdtupyutgccdjyvhptnuhxdwbmdcbpfvxvtfryszhaakwshrjseonfvjrrdefyxefqfvadlwmedpvnozobftnnsutegrtxhwitrwdpfienhdbvvykoynrsbpmzjtotjxbvemgoxreiveakmmbbvbmfbbnyfxwrueswdlxvuelbkrdxlutyukppkzjnmfmclqpkwzyylwlzsvriwomchzzqwqglpflaepoxcnnewzstvegyaowwhgvcwjhbbstvzhhvghigoazbjiikglbqlxlccrwqvyqxpbtpoqjliziwmdkzfsrqtqdkeniulsavsfqsjwnvpprvczcujihoqeanobhlsvbzmgflhykndfydbxatskf"))
        


            
            