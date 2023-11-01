import sys
import math

class Solution:

    @staticmethod
    def read_file(path_to_file: str) -> list:
        result = []

        with open(path_to_file, 'r') as f:
            for line in f:
                result.append(line)
        
        return result
    

    @staticmethod
    def get_circle_data(specific_data: list) -> tuple:
        """
            line_1: c_x c_y
            line_2: c_r
        """

        c_x, c_y = specific_data[0].split()
        c_r = specific_data[1]

        return float(c_x), float(c_y), float(c_r)


    @staticmethod
    def get_points_data(specific_data: list) -> list:
        """
            line_1: p1_x, p1_y
            line_2: p2_x, p2_y
            ...
            line_n: pn_x, pn_y
        """
        
        points = []

        for d in specific_data:
            p_x, p_y = d.split()
            points.append((float(p_x), float(p_y)))
        
        return points


    @staticmethod
    def task2(cirle_filepath: str, points_filepath: str) -> list:
        """
            Find the position of points relative to the circle.
            file1 - coordinates of the circle center and radius;
            file2 - point coordinates.

            0 - point lies on the circle
            1 - point inside
            2 - point outside   
        """

        c_x, c_y, c_r = Solution.get_circle_data(Solution.read_file(cirle_filepath))
        points = Solution.get_points_data(Solution.read_file(points_filepath))

        # (c_x - p_x)^2 + (c_y - p_y)^2 == r^2
        answers = []
        r_sq = c_r ** 2

        for p_x, p_y in points:
            left_exp = (c_x - p_x) ** 2 + (c_y - p_y) ** 2

            if math.isclose(left_exp, r_sq): answers.append(0)
            elif left_exp < r_sq: answers.append(1)
            else: answers.append(2)
        
        return answers




def main():
    result = Solution.task2(sys.argv[1], sys.argv[2])

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
