from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []
        res: List[int] = [] #need to fill with all zeroes
        for i in range(len(temperatures)):
            res.append(0)
        for i in range(len(temperatures)):
            #compare if it is bigger then current in stack, if it is found a bigger one, add to the res the subtraction between current and on the stack on that position
            while (stack and temperatures[i] > temperatures[stack[-1]]):
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res


def run_tests():
    s = Solution()

    # Example 1
    temps1 = [30, 38, 30, 36, 35, 40, 28]
    print("Input :", temps1)
    print("Output:", s.dailyTemperatures(temps1))  # expected [1, 4, 1, 2, 1, 0, 0]

    print("-" * 40)

    # Example 2
    temps2 = [22, 21, 20]
    print("Input :", temps2)
    print("Output:", s.dailyTemperatures(temps2))  # expected [0, 0, 0]


if __name__ == "__main__":
    run_tests()
