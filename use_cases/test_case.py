import json
import typing

import pydantic
import domain.test_case


class TestCase(pydantic.BaseModel):
    name: str = pydantic.Field("Test Case")
    settings: domain.test_case.Settings = pydantic.Field(default_factory=domain.test_case.Settings)
    depends_on: typing.List[str] = pydantic.Field(default_factory=list)
    query_meta: list[dict[str, str]] = pydantic.Field(default_factory=list)
    query_arguments: dict = pydantic.Field(default_factory=dict)
    response_meta: list[dict[str, typing.Union[int, str]]] = pydantic.Field(default_factory=list)
    response_string: typing.Optional[str] = pydantic.Field(default=None)
    response_json: typing.Optional[dict] = pydantic.Field(default=None)

    def load_from_file(path: str) -> "TestCase":
        # load json from file
        with open(path, "r") as file:
            json_data = json.loads(file.read())
        return TestCase(**json_data)

    def save_to_file(self, path: str) -> None:
        with open(path, "r") as file:
            json.dump(self.model_dump(), file)
