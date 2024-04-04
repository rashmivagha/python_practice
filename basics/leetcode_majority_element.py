class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        cnt = 0
        for i in range(0, len(nums)):
            if nums[i] == ele:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                cnt = 1
                ele = nums[i]
        return ele