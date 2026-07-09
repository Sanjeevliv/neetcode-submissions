class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0

        # Phase 1: Find meeting point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find duplicate
        ptr = 0
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return slow