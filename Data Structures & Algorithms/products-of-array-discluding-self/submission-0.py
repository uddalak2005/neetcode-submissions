class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1] * len(nums)
        post_product = [1] * len(nums)

        for i in range(1, len(nums)):
            pre_product[i] = pre_product[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2 , -1, -1):
            post_product[i] = post_product[i + 1] * nums[i + 1] 

        result = []
        for i in range(len(nums)):
            result.append(pre_product[i] * post_product[i])

        return result