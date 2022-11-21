from enum import Enum


class JobType(str, Enum):
    MODELTOCATEGORY = "ModelToCategory"
    CATEGORYTOMODEL = "CategoryToModel"

    def __str__(self) -> str:
        return str(self.value)
