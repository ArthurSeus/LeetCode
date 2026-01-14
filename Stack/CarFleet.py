from typing import List, Tuple


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pos = position.copy()
        # spe = speed.copy()
        fleets = []

        for p, s in zip(position, speed):
            fleets.append((p, s))

        fleets.sort()
        
        stack = []

        while fleets:
            for i in range(len(fleets)):
                fleets[i][0] = fleets[i][0] + fleets[i][1]
                stack.append(fleets[i])                
            
        results = 0

        # while arr:
        #     for i in range(len(position)):
        #         if i not in arr:
        #             continue
        #         position[i] = position[i] + speed[i]
        #         p = 0
        #         while arr and p < i:
        #             if position[p] >= position[i]:
        #                 arr.remove(p)
        #             else:
        #                 p = p + 1
        #         if (position[i] >= target and i in arr):
        #             arr.remove(i)
        #             results = results + 1
                    
        return 0


def run_tests():
    s = Solution()

    # Example 1
    target = 10
    position = [1, 4]
    speed = [3, 2]
    print("Input :", target, position, speed)
    print("Output:", s.carFleet(target, position, speed))  # expected 1

    print("-" * 40)

    # Example 2
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print("Input :", target, position, speed)
    print("Output:", s.carFleet(target, position, speed))  # expected 3


if __name__ == "__main__":
    run_tests()
