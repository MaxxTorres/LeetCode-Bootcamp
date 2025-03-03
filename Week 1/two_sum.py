class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        sum = 0
        l_ind= 0
        r_ind = len(numbers)-1

        while sum != target:
            sum = numbers[l_ind] + numbers[r_ind]

            if sum == target:
                return [l_ind+1, r_ind+1]
            elif sum > target:
                r_ind -= 1
            else:
                l_ind += 1