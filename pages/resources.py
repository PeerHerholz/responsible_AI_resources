from dash import html
import dash
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__, name="Resources", top_nav=True)

def layout():
    return dbc.Row([
        dbc.Col(sidebar(), width=2),  # Sidebar
        dbc.Col(  # Main content area
            html.Div([
                html.P("Here, you will find a diverse array of resources aimed at addressing the challenges and biases inherent in current AI technologies.", style={'textAlign': 'justify', 'marginRight': '60px', 'fontSize': '17px', 'marginBottom': '1px'}),
                html.P("These include:", style={'textAlign': 'justify', 'marginRight': '60px', 'fontSize': '17px'}),
                html.Ol([
                    html.Li([
                        html.Strong("Insightful Publications:"), 
                        " Explore a selection of scholarly articles, research papers, and reports delving into the ethical, social, and technical aspects of responsible AI. These publications serve as a foundational resource for understanding the complexities and responsibilities in AI development."
                    ], style={'marginBottom': '10px', 'marginRight': '100px', 'marginLeft': '-20px', 'textAlign': 'justify', 'fontSize': '17px'}),
                    html.Li([
                        html.Strong("Expert Talks and Presentations:"), 
                        " Find recordings and transcripts of talks by leading experts in the field. These presentations shed light on the latest developments, challenges, and solutions in the realm of ethical AI."
                    ], style={'marginBottom': '10px', 'marginRight': '100px', 'marginLeft': '-20px', 'textAlign': 'justify', 'fontSize': '17px'}),
                    html.Li([
                        html.Strong("Educational Workshops Material:"), 
                        " While this endeavor does not host/organize workshops directly, it provides materials and guides from past workshops focused on responsible AI. These resources are ideal for self-learning or for educators to integrate into their curriculum."
                    ], style={'marginBottom': '10px', 'marginRight': '100px', 'marginLeft': '-20px', 'textAlign': 'justify', 'fontSize': '17px'}),
                    html.Li([
                        html.Strong("Guiding Policies and Frameworks:"), 
                        " Discover a collection of policies, guidelines, and frameworks from around the world that aim to steer AI development towards ethical and responsible outcomes. These documents are crucial for policymakers, practitioners, and academics alike."
                    ], style={'marginRight': '100px', 'marginLeft': '-20px', 'textAlign': 'justify', 'fontSize': '17px'})
                ])
            ]),
            width=10
        )
    ])
