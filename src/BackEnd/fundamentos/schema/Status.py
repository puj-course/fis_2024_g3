# app/schemas/status.py

from enum import Enum

class Status(str, Enum):
    prepared = "Prepared"
    active = "Active"
    ongoing = "onGoing"
    finished = "Finished"
    pendiente = "Pendiente"
