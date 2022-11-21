from enum import Enum


class DatabaseType(str, Enum):
    MONGODB = "mongodb"
    POSTGRESQL = "postgresql"

    def __str__(self) -> str:
        return str(self.value)
