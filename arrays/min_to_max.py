class Solution:
    def count_non_minimum(self, nums):
        # write your logic here
        if not nums:
            return 0
        min_num=min(nums)
        min_cnt=nums.count(min_num)
        return len(nums)-min_cnt


sol = Solution()

test_cases = [
    [1, 2],
    [2, 2, 3, 4],
    [1]
]

for nums in test_cases:
    result = sol.count_non_minimum(nums)
    print(result)