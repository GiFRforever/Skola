class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        temp = ""
        max_len = 0
        cur_len = 0
        for l in s:
            if temp.find(l) == -1:
                temp += l
                cur_len += 1
            else:
                max_len = max(max_len, len(temp))
                temp = temp.split(l)[-1] + l
                cur_len = len(temp)
        return max(max_len, len(temp))


testcases = ["abcabcbb", "bbbbb", "pwwkew"]

for s in testcases:
    print(Solution().lengthOfLongestSubstring(s))
