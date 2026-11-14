class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)

        max_length = 0

        for i in range(len(nums)):
            count = 0
            if (nums[i]-1) not in s:
                for j in range(nums[i], nums[i] + len(nums)):
                    if j in s:
                        count += 1
                    else:
                        break

            max_length = max(max_length, count)

        return max_length

                