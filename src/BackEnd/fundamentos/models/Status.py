from enum import Enum
class Status(str,Enum):
    PREPARED = "Prepared"
    ACTIVE = "Active"
    ONGOING = "Ongoing"
    FINISHED = "Finished"
    PENDING = "Pending"