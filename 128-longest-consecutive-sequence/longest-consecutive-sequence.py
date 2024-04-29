class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        num_set = set(nums)
        for n in num_set:
            if n-1 not in num_set:
                length  = 1
                while n+length in num_set:
                    length +=1
                    longest = max(longest, length)
        if len(nums)==0: return 0
        
        return longest
