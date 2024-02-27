from dash import html
import dash

dash.register_page(__name__, path="/", top_nav=True)

layout = html.Div(
    style={'display': 'flex', 'marginTop': '40px'},
    children=[
        # Text Column
        html.Div(
            style={'width': '50%', 'textAlign': 'justify', 'paddingLeft': '10px', 'fontSize': '17px'},
            children=[
                html.P("""
                    In an age where Artificial Intelligence is rapidly advancing, the landscape is often marred by the development of AI systems that inadvertently perpetuate biases and overlook ethical considerations. This outlines the imperative need for a responsible approach to AI.
                """),
                html.P([
                    "This website aims to offer a curated repository of resources centered on Responsible AI. Unlike a platform for active engagement, it provides a comprehensive library where visitors can access and query a wealth of information and tools to understand and advocate for ethical AI practices. The ",
                    html.A("About page", href="https://peerherholz-responsible-ai-resources.hf.space/about"),
                    " provides further information and an overview of the website and its purpose."
                ]),
                html.P([
                    "The repository includes thorough publications analyzing the ethical dimensions of AI, insightful talks and presentations exploring the nuances of responsibility in AI development, interactive workshops designed to instill ethical AI practices, and comprehensive policies to guide the development of unbiased and equitable AI solutions. Please have a look at the ",
                    html.A("Resources page", href="https://peerherholz-responsible-ai-resources.hf.space/resources"),
                    " to explore these and other resources further."
                ]),
                html.P([
                    "The idea was initially conceived at the first ",
                    html.A("MILA summer school on responsible AI and human rights", href="https://mila.quebec/en/summer-school-responsible-ai/"),  
                    " and would not have been possible without it. Tremendous thanks and kudos to the organizers and participants of the summer school for their contributions and support, as well as being a beacon concerning this highly important topic and development."
                ]),
            ]
        ),

        # Icons Column
        html.Div(
            style={'width': '50%', 'textAlign': 'center', 'paddingRight': '10px'},
            children=[
                html.A(href="https://www.zotero.org/groups/5081008/responsible_ai_human_rights_mila_2023",
                       children=[html.Img(src="https://www.zotero.org/support/_media/logo/zotero_512x512x32.png", style={'height': '40px', 'marginRight': '10px'})]
                ),
                html.A(href="https://github.com/PeerHerholz/responsible_AI_resources",
                       children=[html.Img(src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png", style={'height': '50px', 'marginRight': '10px'})]
                ),
                html.A(href="https://huggingface.co/spaces/peerherholz/responsible_AI_resources/tree/main",
                       children=[html.Img(src="https://cdn-lfs.huggingface.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/942cad1ccda905ac5a659dfd2d78b344fccfb84a8a3ac3721e08f488205638a0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo.svg%3B+filename%3D%22hf-logo.svg%22%3B&response-content-type=image%2Fsvg%2Bxml&Expires=1709292612&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcwOTI5MjYxMn19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5odWdnaW5nZmFjZS5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzLzk0MmNhZDFjY2RhOTA1YWM1YTY1OWRmZDJkNzhiMzQ0ZmNjZmI4NGE4YTNhYzM3MjFlMDhmNDg4MjA1NjM4YTA%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=UqcNXH6zgVENFXZadBssIsnnqSj6E4xGMNLuV2IdzJnhuZwK19wsmLNKWY-W454OzD8hCcc0Qp4lWWNE9BjTrWuvowUs92XNRdjtu7ngHhqYCe07OgzN4UDESionLZhJ8PC7Py0ECd1tcJ98iV4Guf2cqVM4%7E-gvEJsgiai-RM4vb02uZuT6l6bOxTUFF-StgTU29FpoSuIjyinOkV7qV5jocTfWcWKaL4zRM3sUAoT6e8Z-Lgf858AEs5EWPhKH7YJXV8HQ%7EXIhSextKgxRp-wuFDusBuk06x6f9tLw07OovFbVDo0E72nifZDiLRu7ZSQgeKy5R3yfJyYfQXD4Kw__&Key-Pair-Id=KVTP0A1DKRTAX", style={'height': '50px'})]
                ),
                html.A(href="https://osf.io/hgfbx/",
                       children=[html.Img(src="https://tse1.mm.bing.net/th?id=OIP.Y1A1So_sYtPkkVBZYdi8UQHaCy&pid=Api", style={'height': '50px'})]
                )
            ]
        )
    ]
)
