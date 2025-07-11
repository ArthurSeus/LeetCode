from typing import List

def search(nums: List[int], target: int) -> int:
    
    def binarySearch(nums: List[int], target: int, left, right):
        if (left > right):
            return -1
        index = (left + right) // 2
        num = nums[index]
        if (num == target):
            return index
        if (num > target):
            return binarySearch(nums, target, left, index - 1)
        return binarySearch(nums, target, index + 1, right)

    return binarySearch(nums, target, 0, len(nums) - 1)

# Teste
nums = [-1,0,2,4,6,8]
target = 4
print(search(nums, target))  # Saída esperada: 3