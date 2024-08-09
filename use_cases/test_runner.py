import os

import use_cases


class TestRunner:
    root_dir = None
    tests = []

    def run_tests(self, test_dir: str) -> None:
        self.discover(test_dir)
        print(f"Found tests count:{len(self.tests)}")

    def discover(self, test_dir: str) -> None:
        for tc_name in os.listdir(test_dir):
            if not tc_name.endswith(".json"):
                continue

            test_cases = use_cases.TestCase.load_from_file(f"{test_dir}/{tc_name}")
            self.tests.append(test_cases)
