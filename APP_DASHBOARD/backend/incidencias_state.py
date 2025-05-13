import csv
from pathlib import Path
from typing import List
import reflex as rx
from sqlmodel import String, asc, cast, desc, func, or_, select


# This is the incidencia class.   
class Incidencia(rx.Base):
    """The incidencia class."""

    name: str
    phone: str
    address: str
    motivo: str
    usuario: str
    date: str
    status: str
    bitrix: str

# Description: This is the table state class.
class IncidenciasState(rx.State):
    """The state class."""

    incidencias: List[Incidencia] = []

    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    total_incidencias: int = 0
    offset: int = 0
    limit: int = 12  # Number of rows per page

    @rx.var(cache=True)
    def filtered_sorted_incidencias(self) -> List[Incidencia]:
        incidencias = self.incidencias

        # Filter items based on selected item
        if self.sort_value:
            if self.sort_value in ["name"]:
                incidencias = sorted(
                    incidencias,
                    key=lambda incidencia: float(getattr(incidencia, self.sort_value)),
                    reverse=self.sort_reverse,
                )
            else:
                incidencias = sorted(
                    incidencias,
                    key=lambda incidencia: str(getattr(incidencia, self.sort_value)).lower(),
                    reverse=self.sort_reverse,
                )

        # Filter items based on search value
        if self.search_value:
            search_value = self.search_value.lower()
            incidencias = [
                incidencia
                for incidencia in incidencias
                if any(
                    search_value in str(getattr(incidencia, attr)).lower()
                    for attr in [
                        "name",
                        "phone",
                        "address",
                        "motivo",
                        "usuario",
                        "date",
                        "status",
                        "bitrix",
                    ]
                )
            ]

        return incidencias
    
    # Fonction pour la pagination
    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return (self.total_incidencias // self.limit) + (
            1 if self.total_incidencias % self.limit else 1
        )

    @rx.var(cache=True, initial_value=[])
    def get_current_page(self) -> list[Incidencia]:
        start_index = self.offset
        end_index = start_index + self.limit
        return self.filtered_sorted_incidencias[start_index:end_index]

    def prev_page(self):
        if self.page_number > 1:
            self.offset -= self.limit

    def next_page(self):
        if self.page_number < self.total_pages:
            self.offset += self.limit

    def first_page(self):
        self.offset = 0

    def last_page(self):
        self.offset = (self.total_pages - 1) * self.limit
    # Fin de la fonction pour la pagination

    # Fonction pour charger les entrées
    @rx.event
    def load_entries(self) -> list[Incidencia]:
        """Get all incidencias from the database."""
         # get all items for pagination
        # with rx.session() as session:
        #     query = select(Incidencia)
        # self.incidencias_all= session.exec(query).all()
        # self._get_total_items(session)

        """Get all incidencias from the database and paginate them"""
        with rx.session() as session:
            query = select(Incidencia)
            query = query.offset(self.offset).limit(self.limit)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Incidencia, field).ilike(search_value)
                            for field in Incidencia.get_fields()
                            if field not in ["id"]
                        ]
                    )
                )

            if self.sort_value:
                sort_column = getattr(Incidencia, self.sort_value)
                order = (
                    desc(func.lower(sort_column))
                    if self.sort_reverse
                    else asc(func.lower(sort_column))
                )
                query = query.order_by(order)
            self.incidencias = session.exec(query).all()
            self.total_incidencias = len(self.incidencias)

    # Fonction pour trier les entrées
    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()
