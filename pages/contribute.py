import dash

from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, top_nav=True)


layout = html.Div([
    html.P(
        """
        In the ever-evolving landscape of Artificial Intelligence, the pursuit of responsible and ethical practices is a collective journey. The goal of this project is to create an expansive, inclusive repository of resources that caters to the diverse needs and perspectives within the field of AI. To achieve this, we rely on the invaluable contributions of the community — these insights, experiences, and knowledge are the keystones of this shared mission.
        """,
        style={'textAlign': 'justify', 'fontSize': '17px', 'paddingRight': '100px'}
    ),
    html.Strong("Why Your Contribution Matters", style={'fontSize': '18px', 'paddingRight': '100px'}),
    html.P(
        """
        The complexity and breadth of AI ethics require a multitude of voices and a wealth of information. By gathering diverse resources in a community-driven manner, this project aims ensure that this collection remains comprehensive, relevant, and insightful. Your contribution helps in:
        """,
        style={'textAlign': 'justify', 'fontSize': '17px', 'paddingRight': '100px'}
    ),
    html.Ul([
        html.Li("Expanding the Repository: Every new resource enriches the library, offering fresh perspectives and insights.", style={'fontSize': '17px', 'paddingRight': '100px'}),
        html.Li("Ensuring Diversity and Inclusivity: Contributions from a wide range of individuals and organizations help to cover the myriad facets of responsible AI, including underrepresented areas.", style={'fontSize': '17px', 'paddingRight': '100px'}),
        html.Li("Staying Current: The field of AI is rapidly evolving. Your contributions keep this project updated with the latest trends, research, and best practices.", style={'fontSize': '17px', 'paddingRight': '100px'})
    ]),
    html.Strong("How to Contribute", style={'fontSize': '18px', 'paddingRight': '100px'}),
    html.P(
        """
        If you have a resource — be it a publication, a recorded talk, workshop materials, or policy documents — that aligns with the ethos of responsible AI, we encourage you to share it with the community. Here’s how you can contribute:
        """,
        style={'textAlign': 'justify', 'fontSize': '17px', 'paddingRight': '100px'}
    ),
    html.Ul([
        html.Li("Review: Before submitting, please review the information you want to submit to ensure that it aligns with this project's focus on responsible AI.", style={'fontSize': '17px', 'paddingRight': '100px'}),
        html.Li("Prepare Your Submission: Gather all necessary details about your resource, including titles, authors, a brief description, and any relevant links or attachments.", style={'fontSize': '17px', 'paddingRight': '100px'}),
        html.Li("Submit Your Resource: Use the form below to submit your resource. Please provide as much information as possible to help the project team understand the value of your contribution.", style={'fontSize': '17px', 'paddingRight': '100px'}),
        html.Li("Review Process: The project team will review your submission to ensure it aligns with the project's aims. The team may reach out to you for further information if needed.", style={'fontSize': '17px', 'paddingRight': '100px'}),
        html.Li("Publication: Once approved, your resource will be added to the collection and made available to the community of learners and practitioners.", style={'fontSize': '17px', 'paddingRight': '100px'})
    ]),
    html.Strong("Submit Your Resource — Contribution Form", style={'fontSize': '18px', 'paddingRight': '100px'}),
    # Here you would include your form layout
    html.P(
        """
        Your contributions play a vital role in shaping a responsible AI future. Together, let’s build a repository that not only informs but also inspires action towards ethical AI practices. Thank you for being an integral part of this initiative!
        """,
        style={'textAlign': 'justify', 'fontSize': '17px', 'paddingRight': '100px'}
    )
], style={'padding': '20px'})

# Note: You need to add the actual form layout where indicated.
