import reflex as rx


def _badge(status: str):
    badge_mapping = {
        "Solucionada": ("check", "Solucionada", "green"),
        "Pendiente": ("loader", "Pendiente", "yellow"),
        "Tarea Creada": ("ban", "Tarea Creada", "red"),
    }
    icon, text, color_scheme = badge_mapping.get(
        status, ("loader", "Pending", "yellow")
    )
    return rx.badge(
        rx.icon(icon, size=16),
        text,
        color_scheme=color_scheme,
        radius="large",
        variant="surface",
        size="2",
    )


def status_badge(status: str):
    return rx.match(
        status,
        ("Solucionada", _badge("Solucionada")),
        ("Pendiente", _badge("Pendiente")),
        ("Tarea Creada", _badge("Tarea Creada")),
        _badge("Pendiente"),
    )
