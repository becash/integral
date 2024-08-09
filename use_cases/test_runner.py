import json
import os

import pydantic

import use_cases


class TestRunner:
    root_dir = None
    tests = []
    grpc_client = None

    def run_tests(self, test_dir: str):
        self.discover(test_dir)
        print(f"Found tests count:{len(self.tests)}")

    def discover(self, test_dir: str):
        for tc_name in os.listdir(test_dir):
            if not tc_name.endswith(".json"):
                continue
            test_case = self.parse_file(f"{test_dir}/{tc_name}")
            if test_case:
                self.tests.append(test_case)

    def parse_file(self, test_path: str):
        try:
            test_case = use_cases.TestCase.load_from_file(test_path)
        except pydantic.ValidationError:
            while True:
                res = input(
                    f"Incomplete test case file {test_path}. "
                    f"Press d + Enter to to fill fith default values or s + Enter to skip test"
                )
                res = res.strip().lower()
                if res == "d":
                    test_case = use_cases.TestCaseDefaults.load_from_file(test_path)
                    test_case.save_to_file(f"{test_path}")
                    print(f"Set default values for test case {test_path}")
                    return test_case
                elif res == "s":
                    break
        except json.decoder.JSONDecodeError:
            while True:
                res = input(
                    f"WARNIG: Invalid test case file {test_path}, All content will be errased. "
                    f"Press d + Enter to set default values or s + Enter to skip test"
                )
                res = res.strip().lower()
                if res == "d":
                    test_case = use_cases.TestCaseDefaults()
                    test_case.save_to_file(f"{test_path}")
                    print(f"Set default values for test case {test_path}")
                    return test_case
                elif res == "s":
                    break
        else:
            return test_case
