class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validSemiPalindrome(s: str, l, r):
            while l < r:
                if (s[l] != s[r]):
                    return False
                r -= 1
                l += 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if (s[l] != s[r]):
                return validSemiPalindrome(s, l + 1, r) or validSemiPalindrome(s, l, r - 1)
            r -= 1
            l += 1
        
        return True
        pass


# ---------- Helpers para teste local ----------

def run_case(s: str, expected: bool | None = None) -> None:
    sol = Solution()
    got = sol.validPalindrome(s)
    if expected is None:
        print(f"s={s!r} -> {got}")
    else:
        ok = "OK" if got == expected else "FAIL"
        print(f"{ok} | s={s!r} -> got={got}, expected={expected}")


if __name__ == "__main__":
    run_case("acdccba", expected=False)
    run_case("abbadc", expected=False)
    run_case("abca", expected=True)   # remove 'b' ou 'c'
    run_case("abc", expected=False)
    run_case("deeee", expected=True)
