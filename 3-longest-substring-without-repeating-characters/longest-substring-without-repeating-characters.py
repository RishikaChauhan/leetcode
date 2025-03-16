class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i = j = 0
        # ss = ''
        # res = 0
        # while j<len(s):
        #     # ss = s[i:j]
        #     # res = max(len(ss), res)
        #     if s[j] in ss:
        #         i+=1
        #         ss = ss[i:j]
        #     else:
        #         ss+=s[j]
        #         res = max(res, len(ss))
        #         j+=1

        # return res
        i = j = 0
        ss = ''
        res = 0
        
        while j < len(s):  # Corrected loop condition
            if s[j] in ss:  # Check if character exists in substring
                i += 1
                ss = s[i:j]  # Update substring by removing leftmost character
            else:
                ss += s[j]  # Add current character
                res = max(res, len(ss))  # Update max length
                j += 1  # Move forward
        
        return res