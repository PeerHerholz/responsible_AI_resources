import dash
from dash import html
import dash_bootstrap_components as dbc


def sidebar():
    # Define the order of the topics
    topic_order = [
        "topic-publications",
        "topic-presentations",
        "topic-workshops",
        "topic-policies",
        # Add more paths as needed
    ]

    # Sort the page registry according to the defined order
    sorted_pages = sorted(
        dash.page_registry.values(),
        key=lambda page: topic_order.index(page["path"]) if page["path"] in topic_order else float('inf')
    )

    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in sorted_pages
                if page["path"].startswith("/topic")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )
