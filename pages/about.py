from dash import html
import dash

dash.register_page(__name__, top_nav=True)

layout = html.Div(
    style={'display': 'flex', 'marginTop': '40px'},
    children=[
        # Text Column
        html.Div(
            style={'width': '50%', 'textAlign': 'justify', 'paddingLeft': '10px', 'fontSize': '17px'},
            children=[
                html.P("""
                    The goal of this project is to equip everyone interested with the knowledge and tools necessary to navigate the landscape of responsible AI. By offering a centralized resource for high-quality, vetted information on responsible AI, the people behind the project hope to foster a deeper understanding and commitment to ethical AI practices among all stakeholders in the field.
                """),
            ]
        ),
            ]
        )
