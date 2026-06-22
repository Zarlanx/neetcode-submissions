class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        unique = set()
        max_len = 0

        while r < len(s):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            length = (r - l + 1)
            max_len = max(max_len, length)
            r += 1
        return max_len

