class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for x in range(len(nums)):
            if nums[x] > 0:
                break
            l = x+1
            r = len(nums)-1
            while l < r:
                sum = nums[x] + nums[l] + nums[r]
                if sum == 0:
                    if [nums[x], nums[l], nums[r]] not in ans:
                        ans.append([nums[x], nums[l], nums[r]])
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return ans
