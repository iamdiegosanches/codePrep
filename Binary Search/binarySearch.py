class Solution:
    def search(self, nums: List[int], target: int) -> int:
        init = 0
        end = len(nums)-1
        mid = 0
        while init <= end:
            mid = init + ((end - init) // 2)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                init = mid + 1
            else:
                return mid
        return -1
