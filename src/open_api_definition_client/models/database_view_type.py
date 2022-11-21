from enum import Enum


class DatabaseViewType(str, Enum):
    MONGODB = "mongodb"
    POSTGRESQL = "postgresql"

    def __str__(self) -> str:
        return str(self.value)
