class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_positions = []
        for i in range(0,len(nums)):
            for j in range(1,i):
                final_positions.append(j+nums[j])
        if len(nums)-1 in final_positions :
            return True
        else:
            return False