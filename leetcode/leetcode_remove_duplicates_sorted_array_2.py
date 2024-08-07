class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        n = len(nums)
        k = n
        count = 1
        val = nums[0]
        while i < n:
            if val == -100000:
                break
            if val == nums[i]:
                count += 1
                if count > 2:
                   del nums[i]
                   nums.insert(n-1, -100000)
                   k -= 1
                   i -= 1 
            else:
                val = nums[i]
                count = 1
            i += 1       
            
        return k