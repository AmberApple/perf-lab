import sys


class Solution:

    @staticmethod
    def read_file(path_to_file: str) -> list:
        result = []

        with open(path_to_file, 'r') as f:
            for line in f:
                result.append(line)
        
        return result


    @staticmethod
    def task4(numbers_filepath) -> int:
        """
            Find the minimum number of steps required to reduce all elements of the array to one number.
            During the step you can change the number by 1.
            Input: file with numbers of array
        """
        nums = [int(n) for n in Solution.read_file(numbers_filepath)]
        
        nums.sort()
        median = nums[len(nums) // 2]
        
        return sum(abs(median - num) for num in nums)


def main():
    answer = Solution.task4(sys.argv[1])

    print(answer)


if __name__ == "__main__":
    main()
