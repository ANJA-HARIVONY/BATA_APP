import reflex as rx

from ..backend.incidencias_state import Incidencia, IncidenciasState
from ..components.status_badge import status_badge
from ..components.form_app import form_field
from ..backend.operador_state import OperadorState


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
        rx.table.cell(
            rx.hstack(
                update_incidencia_dialog(incidencia),
                delete_incidencia_dialog(incidencia),
            )
        ),
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



def add_customer_button() -> rx.Component:
    """Add a new customer to the database."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Agregar nuevo incidencia", size="4", display=["none", "none", "block"]),
                variant="surface",
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Agregar nueva incidencia",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Rellene el formulario con la información de la incidencia",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(

                    rx.flex(
                        # Name
                        form_field(
                            "Nombre",
                            "Nombre del cliente",
                            "text",
                            "name",
                            "user",
                        ),
                        # Phone
                        form_field("Teléfono", "Teléfono del cliente", "tel", "phone", "phone"),
                        # Address
                        form_field("Dirección", "Dirección del cliente", "text", "address", "home"),
                        # Motivo
                        form_field(
                            "Motivo", "Motivo de la incidencia", "text", "motivo", "pen"
                        ),
                        # Usuario
                        rx.select(
                            OperadorState.nombres,
                            name="usuario",
                            direction="row",
                            as_child=True,
                            required=True,
                            placeholder="Selecciona un usuario",
                        ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("list-todo", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Solucionada", "Pendiente", "Tarea Creada"],
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        # Bitrix
                        form_field(
                            "Bitrix", "¿Es una incidencia de Bitrix?", "number", "bitrix", "wrench"
                        ),

                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="surface",
        
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Agregar incidencia", variant="solid"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=IncidenciasState.add_incidencia_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def update_incidencia_dialog(user):
    """Update a customer in the database."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                size="2",
                variant="surface",
                color_scheme="sky",
                on_click=lambda: IncidenciasState.get_incidencia(user),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Editar incidencia",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Edite la información de la incidencia",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Name
                        form_field(
                            "Name",
                            "Nombre del cliente",
                            "text",
                            "name",
                            "user",
                            user.name,
                        ),
                        # Phone
                        form_field(
                            "Phone",
                            "Teléfono del cliente",
                            "tel",
                            "phone",
                            "phone",
                            user.phone,
                        ),
                        # Address
                        form_field(
                            "Address",
                            "Dirección del cliente",
                            "text",
                            "address",
                            "home",
                            user.address,
                        ),
                        # Motivo
                        form_field(
                            "Motivo", "Motivo de la visita", "text", "motivo", "pen",
                            user.motivo,
                        ),
                        # Usuario
                        rx.select(
                            ["Esther", "Juanita", "Restituta", "Estelina", "Anja", "Crecensia"],
                            name="usuario",
                            direction="row",
                            as_child=True,
                            required=True,
                            default_value=user.usuario,
                        ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("truck", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Solucionada", "Pendiente", "Tarea Creada"],
                                default_value=user.status,
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        # Bitrix
                        form_field(
                            "Bitrix", "Tarea#  ", "number", "bitrix", "wrench",
                            user.bitrix,
                        ),  
                        
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="surface",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Actualizar incidencia"),
                                variant="surface",
                                color_scheme="accent",
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=IncidenciasState.update_incidencia_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )

def delete_incidencia_dialog(user):
    """Delete a customer from the database."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("trash-2", size=22), size="2", variant="surface"),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(rx.icon("trash-2", size=34), color_scheme="red", radius="full", padding="0.65rem"),
                rx.vstack(rx.dialog.title("Eliminar incidencia", weight="bold", margin="0"), rx.dialog.description("¿Está seguro de que desea eliminar la incidencia de " + user.name + "?"), spacing="1", height="100%", align_items="start"),
            ),
            rx.dialog.close(
                rx.hstack(
                    rx.button("Cancelar", variant="surface"),
                    rx.button("Eliminar", on_click=lambda: IncidenciasState.delete_incidencia(user.id)),
                    spacing="3",
                    mt="4",
                    justify="end",
                )
            ),
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
            add_customer_button(),
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
                    _header_cell("Acciones", "hummer"),
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
