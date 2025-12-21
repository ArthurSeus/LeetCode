from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(nums: List[int], target: int, left, right) -> int:
            if (left > right):
                return left
            
            index = (left + right) // 2
            num = nums[index]
            if (num > target):
                return binarySearch(nums, target, left, index - 1)
            if (num < target):
                return binarySearch(nums, target, index + 1, right)
            
            return index
        
        result = binarySearch(nums, target, 0, len(nums) - 1)

        return result
        #     num = nums[left]
        # else:
        #     num = nums[0]
        # if (num > target):
        #     result = left - 1
        #     if (result >= 0):
        #         return result
        #     return 0
        
        # return left + 1

# ---------- Helpers para teste local ----------

def run_case(nums: List[int], target: int, expected: int | None = None) -> None:
    sol = Solution()
    got = sol.searchInsert(nums, target)
    if expected is None:
        print(f"nums={nums}, target={target} -> {got}")
    else:
        ok = "OK" if got == expected else "FAIL"
        print(f"{ok} | nums={nums}, target={target} -> got={got}, expected={expected}")


if __name__ == "__main__":
    run_case([-1, 0, 2, 4, 6, 8], 5, expected=4)
    run_case([-1, 0, 2, 4, 6, 8], 10, expected=6)
    run_case([-1, 0, 2, 4, 6, 8], -5, expected=0)
    run_case([1, 3, 5, 6], 5, expected=2)
    run_case([1, 3, 5, 6], 2, expected=1)
    run_case([1, 3, 5, 6], 7, expected=4)
