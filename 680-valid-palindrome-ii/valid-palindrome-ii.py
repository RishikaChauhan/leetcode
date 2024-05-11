class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s) # Length of string
        r = s[::-1] # Reversed string

        # The string is already a palindrome
        if s == r:
            return True

        for i in range(l):
            # Loop until first mismatch
            if s[i] == r[i]:
                continue

            # Check if if the string (s) is a palindrome by removing the character
            # at the current index (i) and the reversed index (l - i - 1) from the
            # reversed string (r), then compare.
            # If not, check again by removing the character at the reversed index 
            # (l - i - 1) from the string (s) and the character at index (i) 
            # from the reversed string (r), then compare.
            if (s[:i] + s[i + 1:] == r[:l - i - 1] + r[l - i:] 
                    or r[:i] + r[i + 1:] == s[:l - i - 1] + s[l - i:]):
                return True
            
            # Once the first mismatch is found, there is no need to continue the loop.
            # Since we have already checked two indexes above, we know that it will
            # be false because a valid palindrome + one extra character will always
            # have exactly two mismatched characters between the string (s) and the 
            # reversed string (r).
            return False