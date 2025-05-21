import reflex as rx
from typing import List


class Operador(rx.Model, table=True):
    """The operador model."""
    nombre: str
    telefono: str
    email: str
    status: str

class OperadorState(rx.State):
    """The state class."""
    operadores: list[Operador] = [
        {
        "nombre" : "Irene",
        "telefono" :" 222 333 444",
        "email" : "anja@yahoo.fr",
        "status" : "Active"
        },
               {
        "nombre" : "Deo",
        "telefono" :" 222 333 555",
        "email" : "harivony@yahoo.fr",
        "status" : "Active"
        },
               {
        "nombre" : "Mohin",
        "telefono" :" 222 333 666",
        "email" : "amohin@yahoo.fr",
        "status" : "False"
        },
    ]

    nombres = [operador["nombre"] for operador in operadores]

    
