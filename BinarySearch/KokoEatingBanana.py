from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        #possibilities = list(range(min_b, max_b + 1))
        left = 1
        right = max(piles)
        success = right
        while(left <= right):
            curr = (left + right) // 2
            h_left = h
            for banana in piles:
                h_left -= ceil(banana/curr)
            if (h_left >= 0):
                success = min(curr, success)
                right = curr - 1
            else:
                left = curr + 1
            
        return success
        pass


# ---------- Helpers ----------

def run_case(piles: List[int], h: int, expected: int | None = None) -> None:
    sol = Solution()
    got = sol.minEatingSpeed(piles, h)
    if expected is None:
        print(f"piles={piles}, h={h} -> {got}")
    else:
        ok = "OK" if got == expected else "FAIL"
        print(f"{ok} | piles={piles}, h={h} -> got={got}, expected={expected}")


if __name__ == "__main__":
    # exemplos básicos (pode adicionar mais)
    run_case([1, 4, 3, 2], 9, expected=2)
    run_case([3, 6, 7, 11], 8, expected=4)
    run_case([30, 11, 23, 4, 20], 5, expected=30)
    run_case([30, 11, 23, 4, 20], 6, expected=23)