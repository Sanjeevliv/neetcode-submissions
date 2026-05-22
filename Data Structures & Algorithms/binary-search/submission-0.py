class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        L = 0
        R = n-1

        while L<=R:
            mid=L+ (R-L)//2
            if nums[mid] < target:
                L=mid+1
            elif nums[mid] > target:
                R=mid-1
            else:
                return mid
            
        return -1
            