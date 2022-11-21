from enum import Enum


class JobStatus(str, Enum):
    DEFAULT = "Default"
    READY = "Ready"
    RUNNING = "Running"
    FINISHED = "Finished"
    CANCELED = "Canceled"

    def __str__(self) -> str:
        return str(self.value)
