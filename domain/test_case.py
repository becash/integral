import enum

import pydantic


class TestType(enum.StrEnum):
    rest = "rest"
    graphql = "graphql"
    grpc = "grpc"


class Settings(pydantic.BaseModel):
    type: TestType


class SettingsDefault(Settings):
    type: TestType = pydantic.Field(default=TestType.rest)
