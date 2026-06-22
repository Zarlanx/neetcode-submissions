class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tracker = 1
        res = [1]*(len(nums))
        print(res)

        for i in range(len(nums)):
            res[i] = tracker
            tracker *= nums[i]

        tracker = 1
        for i in range((len(nums) - 1), -1, -1):
            res[i] *= tracker
            tracker *= nums[i]
        return res
