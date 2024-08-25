"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from string import whitespace

import reflex as rx
from docutils.parsers.rst.directives.tables import align


class DataTable(rx.State):
    data: list[dict[str, str]] = [
        {
            "profile": "https://cdn.githubraw.com/jbcodefr/Files-For-Tuto/main/PythonReflex/3d-bunny-digital-avatar-midjourney-prompt.jpg",
            "name": "John Doe",
            "job": "Software Engineer",
            "email": "johndoe@example.com",
            "phone": "+1 234 567 8901"
        },
        {
            "profile": "https://cdn.githubraw.com/jbcodefr/Files-For-Tuto/main/PythonReflex/caribbean-man-summer-avatar-midjourney.jpg",
            "name": "Jane Smith",
            "job": "Project Manager",
            "email": "janesmith@example.com",
            "phone": "+1 987 654 3210"
        },
        {
            "profile": "https://cdn.githubraw.com/jbcodefr/Files-For-Tuto/main/PythonReflex/cute-penguin-midjourney-prompt.jpg",
            "name": "Sophia Martinez",
            "job": "Accountant",
            "email": "sophia.martinez@example.com",
            "phone": "+1 333 444 5555"
        },
        {
            "profile": "https://cdn.githubraw.com/jbcodefr/Files-For-Tuto/main/PythonReflex/futuristic-digital-avatar-midjourney-prompt.jpg",
            "name": "Liam Riley",
            "job": "Web Developer",
            "email": "liamriley@example.com",
            "phone": "+1 999 888 7777"
        }
    ]
    color_map: dict[str, str] = {
        "Software Engineer": "red",
        "Project Manager": "cyan",
        "Accountant": "pink",
        "Web Developer": "blue"
    }

def create_data_row(data: dict[str, str]) :
    return rx.table.row(
        rx.table.cell(
            rx.hstack(
                rx.avatar(src=data["profile"], size="1"),
                rx.text(data["name"], color_scheme="gray", weight="medium"),
            )
        ),
        rx.table.cell(
            rx.badge(data["job"],color_scheme=DataTable.color_map[data["job"]],weight="medium"),
        ),
        rx.table.cell(
            rx.text(data["email"],color_scheme="gray",weight="medium",text_decoration="underline"),
        ),
        rx.table.cell(
            rx.text(data["phone"], color_scheme="sky", weight="medium", text_decoration="underline"),
        ),
        rx.table.cell(
            rx.icon(tag="pencil",color="plum",weight="medium"),
        ),
        rx.table.cell(
            rx.icon(tag="trash", color="red", weight="medium"),
        ),
        align="center",
        whitespace="nowrap"
    )

@rx.page("/","DATA TABLE")
def index():
    return rx.box(rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    ["Worker","Job Title","Email","Phone Number","",""],
                    lambda title:
                    rx.table.column_header_cell(
                        rx.text(title,font_size="12px",weight="bold"),
                    )
                )
            )
        ),
        rx.table.body(
            rx.foreach(DataTable.data,create_data_row)
        ),
        width="100%",
        max_width="900px",
    ),
        rx.color_mode.button(position="top-right")
        ,width="100%",height="100vh",align="center",padding="2em")

app = rx.App()
