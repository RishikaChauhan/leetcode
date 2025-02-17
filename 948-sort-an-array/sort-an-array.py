class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            mid_left = merge_sort(arr[:mid])
            mid_right = merge_sort(arr[mid:])
            return merge(mid_left, mid_right)

        def merge(l,r):
            sorted_list = []
            i = 0
            j = 0
            while i<len(l) and j<len(r):
                if l[i]<r[j]:
                    sorted_list.append(l[i])
                    i+=1
                else:
                    sorted_list.append(r[j])
                    j+=1
            sorted_list.extend(l[i:])
            sorted_list.extend(r[j:])

            return sorted_list

        return merge_sort(nums)