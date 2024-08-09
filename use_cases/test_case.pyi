import json
import typing

import pydantic
import domain.test_case
import use_cases


class TestCase(pydantic.BaseModel):
    name: typing.Optional[str]
    settings: domain.test_case.Settings
    depends_on: typing.List[str]
    query_meta: list[dict[str, str]]
    query_arguments: dict
    response_meta: list[dict[str, typing.Union[int, str]]]
    response_string: typing.Optional[str]
    response_json: typing.Optional[dict]

    @staticmethod
    def load_from_file(path: str) -> "TestCase":...

    def save_to_file(self, path: str) -> None:...

    def run(self, iterator: use_cases.TestRunner):...


class TestCaseDefaults(TestCase):
    name: typing.Optional[str] = pydantic.Field("Test Case")
    settings: domain.test_case.SettingsDefault = pydantic.Field(default_factory=domain.test_case.SettingsDefault)
    depends_on: typing.List[str] = pydantic.Field(default_factory=list)
    query_meta: list[dict[str, str]] = pydantic.Field(default_factory=list)
    query_arguments: dict = pydantic.Field(default_factory=dict)
    response_meta: list[dict[str, typing.Union[int, str]]] = pydantic.Field(default_factory=list)
    response_string: typing.Optional[str] = pydantic.Field(default=None)
    response_json: typing.Optional[dict] = pydantic.Field(default=None)

    @staticmethod
    def load_from_file(path: str) -> "TestCase":
        # load json from file
        with open(path, "r") as file:
            json_data = json.loads(file.read())
        return TestCaseDefaults(**json_data)
