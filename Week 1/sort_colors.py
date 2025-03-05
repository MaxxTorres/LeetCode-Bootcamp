class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_ind = 0
        r_ind = len(nums)-1
        curr_ind = 0

        while curr_ind <= r_ind:
            if nums[curr_ind] == 0:
                nums[l_ind], nums[curr_ind] = nums[curr_ind], nums[l_ind]
                l_ind += 1
                curr_ind +=1
            elif nums[curr_ind] == 1:
                curr_ind += 1
            else:
                nums[curr_ind], nums[r_ind] = nums[r_ind], nums[curr_ind]
                r_ind -= 1