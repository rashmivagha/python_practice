class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        k = n
        while i < n-1:
            if nums[i] == -1000:
                break
            if nums[i] == nums[i+1]:
                del nums[i]
                nums.insert(n-1, -1000)
                k -= 1
                i -= 1
            i += 1
        
        return k