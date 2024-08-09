import os

import use_cases

class TestRunner:
    root_dir: str
    tests: list[use_cases.test_case.TestCase]

    def run_tests(self, test_dir: str) -> None: ...
    def discover(self, test_dir: str) -> None: ...
