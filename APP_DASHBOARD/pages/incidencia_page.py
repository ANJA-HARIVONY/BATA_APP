"""The table page."""

import reflex as rx

from ..backend.incidencias_state import IncidenciasState
from ..templates import template
from ..views.incidencia_views import main_table


@template(route="/incidencia_page", title="Incidencias", on_load=IncidenciasState.load_entries)
def table_incidencia() -> rx.Component:
    """The table page.

    Returns:
        The UI for the table page.

    """
    return rx.vstack(
        rx.heading("Incidencias", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
