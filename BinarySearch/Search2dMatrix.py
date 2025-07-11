from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums, target, left, right, closest):
            if (left > right):
                return closest
            
            index = (left + right) // 2
            num = nums[index]

            if num == target:
                return num
            if num > target:
                return search(nums, target, left, index - 1, num)
            
            return search(nums, target, index + 1, right, num)

        list_left, list_right = 0, len(matrix) - 1

        while list_left <= list_right:
            current_list_index = (list_left + list_right) // 2
            current_list = matrix[current_list_index]
            closest = search(current_list, target, 0, len(current_list) - 1, None)
            if closest == target:
                return True
            if closest > target:
                list_right = current_list_index - 1
            elif closest < target:
                list_left = current_list_index + 1
            
        return False

# Teste no VSCode
matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15

print(Solution().searchMatrix(matrix, target))  # Esperado: False

target = 20
print(Solution().searchMatrix(matrix, target))  # Esperado: True
