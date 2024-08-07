class Solution:
    def reverse_array(self, nums: List[int], start: int, end: int) -> List[int]:
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return nums
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        # for i in range(0,k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)

        nums = self.reverse_array(nums, 0, n-1)
        nums = self.reverse_array(nums, 0, k-1)
        nums = self.reverse_array(nums, k, n-1)