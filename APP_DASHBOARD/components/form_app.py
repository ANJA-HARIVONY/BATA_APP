import reflex as rx

def form_field(
    label: str,
    placeholder: str,
    type: str,
    name: str,
    icon: str,
    default_value: str = "",
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.hstack(
                rx.icon(icon, size=16, stroke_width=1.5),
                rx.form.label(label),
                align="center",
                spacing="2",
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type, default_value=default_value
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def item_dialog() -> rx.Component:
    """Composant de dialogue pour la saisie d'items."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Ajouter un item", size="3", variant="surface"),
        ),
        rx.dialog.content(
            rx.form(
                form_field(
                    label="Nom",
                    icon="user",
                    placeholder="Nom de l'item",
                    type="text",
                    name="name",
                ),
                form_field(
                    label="Prix",
                    icon="dollar",
                    placeholder="Prix de l'item",
                    type="number",
                    name="price",
                ),
                form_field(
                    label="Date",
                    icon="calendar",
                    placeholder="Date de l'item",
                    type="date",
                    name="date",
                ),
            ),
            margin_top="4",
            spacing="4",
            border_radius="10px",
            border_width="1px",
            padding="4",
        ),
    )
