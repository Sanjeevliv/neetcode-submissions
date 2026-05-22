class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
            
                if i!=j:
                    product=product*nums[j]
                else:
                    continue
            sol.append(product)
        return sol

        # NOT OPTIMAL SOL