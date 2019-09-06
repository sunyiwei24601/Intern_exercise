import collections
class Solution:
    def groupAnagrams(self, strs):
        result = collections.defaultdict(list)

        for s in strs:
            serials = [0] * 26
            for i in s:
                serials[ord(i) - ord('a')] += 1
            result[tuple(serials)].append(s)
        return list(result.values())

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
