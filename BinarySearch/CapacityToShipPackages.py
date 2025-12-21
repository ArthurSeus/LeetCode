import math
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        k = math.ceil(len(weights) / days)
        left = 0
        index = left
        right = min(left + k, len(weights) - 1)
        largest = 0
        while (index <= right):
            largest += weights[index]
            index += 1

        curr = largest
        while (right < len(weights) - 1):
            curr -= weights[left]
            curr += weights[right + 1]
            largest = max(curr, largest)
            left += 1
            right += 1

        right = largest
        left = 1
        smallest = right
        while(left <= right):
            curr = (left + right) // 2
            index = 0
            day = 0
            while (index < len(weights)):
                if (day > days):
                    break
                package = curr
                day += 1
                while(index < len(weights)):
                    package -= weights[index]
                    if(package >= 0):
                        index += 1
                    else:
                        break
            if (day <= days):
                right = curr - 1
                smallest = min(smallest, curr)
            else:
                left = curr + 1
        
        return smallest

# ---------- Helpers para teste local ----------

def run_case(weights: List[int], days: int, expected: int | None = None) -> None:
    sol = Solution()
    got = sol.shipWithinDays(weights, days)
    if expected is None:
        print(f"weights={weights}, days={days} -> {got}")
    else:
        ok = "OK" if got == expected else "FAIL"
        print(f"{ok} | weights={weights}, days={days} -> got={got}, expected={expected}")


if __name__ == "__main__":
    run_case([1,5,4,4,2,3], 3, expected=8)
    run_case([2, 4, 6, 1, 3, 10], 4, expected=10)
    run_case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, expected=15)
    run_case([3, 2, 2, 4, 1, 4], 3, expected=6)
    run_case([1, 2, 3, 1, 1], 4, expected=3)
