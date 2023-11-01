import sys
import json


# Where should the file be saved?
path_to_report = 'report.json'
# Now NO output to console for '... > file.txt'


class Solution:

    @staticmethod
    def read_json(path_to_file: str) -> dict:
        with open(path_to_file) as f:
            data = json.load(f)
        
        return data
    

    @staticmethod
    def write_report(data: dict) -> None:
        with open(path_to_report, 'w') as f:
            json.dump(data, f, indent=2)


    @staticmethod
    def get_value_by_id(id: int, values: dict) -> str:
        vals = values.get('values')
        for d in vals:
            if d.get('id') == id:
                return d.get('value')
        
        return ''


    @staticmethod
    def fill_values(test: dict, values: dict) -> None:
        """
            Update data in test dict
        """
        for _, val in list(test.items()):
            if isinstance(val, list):
                for v in val:
                    Solution.fill_values(v, values)
            
            test["value"] = Solution.get_value_by_id(test.get('id'), values)


    @staticmethod
    def task3(tests_filepath: str, values_filepath:str) -> dict:
        """
            Fill report.json based tests.json and values_json.
            Input: tests.json values.json
            Output: report.json
        """

        tests = Solution.read_json(tests_filepath)
        values = Solution.read_json(values_filepath)

        Solution.fill_values(tests, values)

        return tests


def main():
    report = Solution.task3(sys.argv[1], sys.argv[2])
    Solution.write_report(report)
    #print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
