from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def safePop(lst: List[int]) -> int:
            return lst.pop() if lst else 0
        stack = []
        for op in operations:
            if op.lstrip("+-").isdigit():
                stack.append(int(op))
            elif op == '+':
                n1 = safePop(stack)
                n2 = safePop(stack)
                r = n1 + n2
                stack.append(n2)
                stack.append(n1)
                stack.append(r)
            elif op == 'C':
                safePop(stack)
            elif op == 'D':
                n1 = safePop(stack)
                r = n1 * 2
                stack.append(n1)
                stack.append(r)
        return sum(stack)
        pass


# ---------- Helpers para teste local ----------

def run_case(ops: List[str], expected: int | None = None) -> None:
    sol = Solution()
    got = sol.calPoints(ops)
    if expected is None:
        print(f"ops={ops} -> {got}")
    else:
        ok = "OK" if got == expected else "FAIL"
        print(f"{ok} | ops={ops} -> got={got}, expected={expected}")


if __name__ == "__main__":
    run_case(["5","-2","4","C","D","9","+","+"], expected=27)
    run_case(["5", "2", "C", "D", "+"], expected=30)
    run_case(["10"], expected=10)
    run_case(["3", "D", "D", "+", "C"], expected=18)
