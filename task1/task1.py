import sys
import math


class Solution:

    @staticmethod
    def task1(n: int, m: int) -> str:
        """
            Circular array: Find path.
            n - array length;
            m - step length.
        """
        
        # new_index = (index + step) % list_len - 1
        finish_point = 1
        index = 0
        path = [finish_point]

        # is_coprime
        if math.gcd(n, m) != 1:
            return 0
        
        while True:
            index = (index + m) % n - 1
            if index == -1: index = n - 1

            point = index + 1
            if point == finish_point:
                break
            
            path.append(point)
        
        return "".join(str(p) for p in path)


def main():
    print(Solution.task1(int(sys.argv[1]), int(sys.argv[2])))


if __name__ == "__main__":
    main()
