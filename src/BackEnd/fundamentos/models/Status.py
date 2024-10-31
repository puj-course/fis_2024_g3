from enum import Enum
class Status(str,Enum):
    prepared = "Prepared"
    active = "Active"
    onGoing = "OnGoing"
    finish = "Finished"
    pendiente = "Pendiente"