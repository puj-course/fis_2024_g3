from enum import Enum


class Role(str, Enum):
    admin = "Admin"
    gerente = "Gerente"
    lider = "Líder"
    empleado = "Empleado"
