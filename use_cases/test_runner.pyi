import os
import typing

import use_cases

class TestRunner:
    root_dir: str
    tests: list[use_cases.TestCase]
    grpc_client = None

    def run_tests(self, test_dir: str) -> None: ...
    def discover(self, test_dir: str) -> None: ...
    def parse_file(self, test_dir: str) -> typing.Optional[use_cases.TestCase]: ...
