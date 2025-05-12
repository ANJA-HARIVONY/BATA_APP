"""The table page."""

import reflex as rx

from ..backend.table_state import TableState
from ..templates import template
#from ..views.table import main_table


@template(route="/incidencia_page", title="Incidencias")
def table_incidencia() -> rx.Component:
    """The table page.

    Returns:
        The UI for the table page.

    """
    return rx.vstack(
        rx.heading("Table", size="5"),
        #main_table(),
        rx.text("Bienvenue dans la page des incidences"),
        spacing="8",
        width="100%",
    )
