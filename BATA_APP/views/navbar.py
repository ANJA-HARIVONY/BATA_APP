import reflex as rx


def navbar():
    return rx.flex(
        rx.badge(
            rx.icon(tag="radio-tower", size=28),
            rx.heading("CONEXXIA - Atención al cliente", size="6"),
            color_scheme="green",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.spacer(),
        rx.hstack(
            #rx.image(src="radio-tower.png", width="100px", height="100px"),
            rx.color_mode.button(),
            align="center",
            spacing="3",
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="2em",
    )

def footer():
    return rx.flex(
        rx.text("© 2025 CONEXXIA - Atención al cliente ",
                font_size="0.8em",
                ),
                dialog_info(),
        direction="column",
        align="center",
        width="100%",
        padding_bottom="1em",
        justify="center",
    )

def dialog_info() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            #rx.button(rx.icon("user", size=22), color_scheme="blue", size="2", variant="solid"),
            rx.link("Contact para más información", font_size="0.8em", text_decoration="none")
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(rx.icon("user", size=34), color_scheme="blue", radius="full", padding="0.65rem"),
                rx.vstack(rx.dialog.title("Informacion", weight="bold", margin="0"), 
                        rx.dialog.description("ANJA - HARIVONY : 222 304 981 "), 
                        rx.text("Version 1.5", size="2"),
                        spacing="1", height="100%", align_items="start"),
            ),
            rx.dialog.close(
                rx.hstack(
                    rx.button("OK", variant="solid", color_scheme="blue"),
                    spacing="3",
                    mt="4",
                    justify="end",
                )
            ),
        ),
    )
