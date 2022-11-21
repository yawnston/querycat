from enum import Enum


class DatabaseInitType(str, Enum):
    MONGODB = "mongodb"
    POSTGRESQL = "postgresql"

    def __str__(self) -> str:
        return str(self.value)
