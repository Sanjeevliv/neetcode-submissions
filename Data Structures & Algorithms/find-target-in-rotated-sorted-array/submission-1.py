class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find pivot
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # Define the two sorted segments
        left_start, left_end = 0, pivot - 1
        right_start, right_end = pivot, len(nums) - 1
        
        # Check if target is in right segment
        if nums[right_start] <= target <= nums[right_end]:
            return binary_search(right_start, right_end)
        else:
            return binary_search(left_start, left_end)