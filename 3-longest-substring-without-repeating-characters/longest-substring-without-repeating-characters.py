class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length