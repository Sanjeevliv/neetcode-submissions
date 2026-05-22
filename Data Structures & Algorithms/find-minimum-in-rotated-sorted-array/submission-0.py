class Solution:
    def findMin(self, nums: List[int]) -> int:
        n= len(nums)
        maxnum=float('inf')
        for i in range(n):
            if nums[i]< maxnum:
                maxnum=nums[i]
        return maxnum