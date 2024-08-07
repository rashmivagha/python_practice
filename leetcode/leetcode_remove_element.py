class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = n
        i = 0
        while i < n:
            if nums[i] == val:
                del nums[i]
                nums.insert(n-1, -1)
                k -= 1
                i -= 1
            i += 1
        return k