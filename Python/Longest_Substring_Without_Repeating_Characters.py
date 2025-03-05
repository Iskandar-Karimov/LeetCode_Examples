class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        seen_letters = {}
        longest_seen = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in seen_letters:
                stop = seen_letters[s[r]] + 1
                while l < stop:
                    del(seen_letters[s[l]])
                    l += 1
            longest_seen = max(longest_seen, r-l+1)
            seen_letters[s[r]] = r
            r += 1
        return longest_seen
                