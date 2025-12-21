from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l <= r:
            lc = s[l]
            rc = s[r]
            s[l] = rc
            s[r] = lc
            l += 1
            r -= 1
        pass


# ---------- Helpers para teste local ----------

def run_case(s: List[str], expected: List[str]) -> None:
    sol = Solution()
    sol.reverseString(s)
    ok = "OK" if s == expected else "FAIL"
    print(f"{ok} | got={s}, expected={expected}")


if __name__ == "__main__":
    run_case(["n", "e", "e", "t"], ["t", "e", "e", "n"])
    run_case(["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "c", "e", "c", "a", "r"])
    run_case(["a"], ["a"])
    run_case([], [])
