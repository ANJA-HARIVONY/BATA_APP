import reflex as rx

from ..backend.incidencias_state import Incidencia, IncidenciasState
from ..components.status_badge import status_badge
from ..components.form_app import item_dialog

# c'est le composant pour le header de la table 
def _header_cell(text: str, icon: str) -> rx.Component:
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def _show_item(incidencia: Incidencia, index: int) -> rx.Component:
    bg_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 1),
        rx.color("accent", 2),
    )
    hover_color = rx.cond(
        index % 2 == 0,
        rx.color("gray", 3),
        rx.color("accent", 3),
    )
    return rx.table.row(
        rx.table.row_header_cell(incidencia.name),
        rx.table.cell(incidencia.phone),
        rx.table.cell(incidencia.address),
        rx.table.cell(incidencia.motivo),
        rx.table.cell(incidencia.usuario),
        rx.table.cell(incidencia.date),
        rx.table.cell(status_badge(incidencia.status)),
        rx.table.cell(incidencia.bitrix),
        style={"_hover": {"bg": hover_color}, "bg": bg_color},
        align="center",
    )


def _pagination_view() -> rx.Component:
    return (
        rx.hstack(
            rx.text(
                "Page ",
                rx.code(IncidenciasState.page_number),
                f" of {IncidenciasState.total_pages}",
                justify="end",
            ),
            rx.hstack(
                rx.icon_button(
                    rx.icon("chevrons-left", size=18),
                    on_click=IncidenciasState.first_page,
                    opacity=rx.cond(IncidenciasState.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(IncidenciasState.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-left", size=18),
                    on_click=IncidenciasState.prev_page,
                    opacity=rx.cond(IncidenciasState.page_number == 1, 0.6, 1),
                    color_scheme=rx.cond(IncidenciasState.page_number == 1, "gray", "accent"),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-right", size=18),
                    on_click=IncidenciasState.next_page,
                    opacity=rx.cond(
                        IncidenciasState.page_number == IncidenciasState.total_pages, 0.6, 1
                    ),
                    color_scheme=rx.cond(
                        IncidenciasState.page_number == IncidenciasState.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevrons-right", size=18),
                    on_click=IncidenciasState.last_page,
                    opacity=rx.cond(
                        IncidenciasState.page_number == IncidenciasState.total_pages, 0.6, 1
                    ),
                    color_scheme=rx.cond(
                        IncidenciasState.page_number == IncidenciasState.total_pages,
                        "gray",
                        "accent",
                    ),
                    variant="soft",
                ),
                align="center",
                spacing="2",
                justify="end",
            ),
            spacing="5",
            margin_top="1em",
            align="center",
            width="100%",
            justify="end",
        ),
    )


def main_table() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.cond(
                    IncidenciasState.sort_reverse,
                    rx.icon(
                        "arrow-down-z-a",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=IncidenciasState.toggle_sort,
                    ),
                    rx.icon(
                        "arrow-down-a-z",
                        size=28,
                        stroke_width=1.5,
                        cursor="pointer",
                        flex_shrink="0",
                        on_click=IncidenciasState.toggle_sort,
                    ),
                ),
                rx.select(
                    [
                        "name",
                        "phone",
                        "address",
                        "motivo",
                        "usuario",
                        "date",
                        "status",
                        "bitrix",
                    ],
                    placeholder="Sort By: Name",
                    size="3",
                    on_change=IncidenciasState.set_sort_value,
                ),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    rx.input.slot(
                        rx.icon("x"),
                        justify="end",
                        cursor="pointer",
                        on_click=IncidenciasState.setvar("search_value", ""),
                        display=rx.cond(IncidenciasState.search_value, "flex", "none"),
                    ),
                    value=IncidenciasState.search_value,
                    placeholder="Search here...",
                    size="3",
                    max_width=["150px", "150px", "200px", "250px"],
                    width="100%",
                    variant="surface",
                    color_scheme="gray",
                    on_change=IncidenciasState.set_search_value,
                ),
                align="center",
                justify="end",
                spacing="3",
            ),
            # c'est le composant pour le bouton d'ajout
            item_dialog(),
            # c'est le composant pour le bouton d'exportation
            rx.button(
                rx.icon("arrow-down-to-line", size=20),
                "Export",
                size="3",
                variant="surface",
                display=["none", "none", "none", "flex"],
                on_click=rx.download(url="/items.csv"),
            ),
            spacing="3",
            justify="between",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Name", "user"),
                    _header_cell("Phone", "phone"),
                    _header_cell("Address", "map-pin"),
                    _header_cell("Motivo", "notebook-pen"),
                    _header_cell("Usuario", "user"),
                    _header_cell("Date", "calendar"),
                    _header_cell("Status", "notebook-pen"),
                    _header_cell("Bitrix", "notebook-pen"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    IncidenciasState.get_current_page,
                    lambda incidencia, index: _show_item(incidencia, index),
                )
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        _pagination_view(),
        width="100%",
    )
