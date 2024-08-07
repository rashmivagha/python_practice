class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        if n!= 0:
            for i in range(0, m+n):
                if j < n: #because nums2 can be empty
                    if nums1[i] >= nums2[j]: # example 1,3
                        nums1.insert(i, nums2[j]) 
                        nums1.pop()
                        j += 1
                    elif i >= m+j: # number of valid elements in nums1 plus number of elements added
                        nums1.insert(i, nums2[j])
                        nums1.pop()
                        j += 1