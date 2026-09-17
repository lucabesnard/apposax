import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px

# ----------------------------------------------------------------------- #
# Page
# ----------------------------------------------------------------------- #

dash.register_page(
    __name__,
    path="/page2",
    name="Page 2"
)

# ----------------------------------------------------------------------- #
# Sources
# ----------------------------------------------------------------------- #

# Récupération du dataset Iris
df = px.data.iris()

# Variables disponibles pour les axes
var = [
    {
        "label": s.replace("_", " ").capitalize(),
        "value": s
    }
    for s in df.columns[0:3]
]

# ----------------------------------------------------------------------- #
# Interface
# ----------------------------------------------------------------------- #

layout = html.Div([

    html.Div([
        html.H1(
            "🌸 Iris Dataset",
            style={
                "fontSize": "45px",
                "fontWeight": "800",
                "marginBottom": "5px"
            }
        ),

        html.P(
            "Analysez les caractéristiques des différentes espèces d'Iris.",
            style={
                "fontSize": "18px",
                "opacity": "0.8",
                "marginBottom": "35px"
            }
        )
    ]),

    html.Div([

        html.Div([
            html.H4("↔️ Axe horizontal"),
            dcc.Dropdown(
                id="x",
                options=var,
                value=var[0]["value"],
                clearable=False
            )
        ], style={
            "width": "45%"
        }),

        html.Div([
            html.H4("↕️ Axe vertical"),
            dcc.Dropdown(
                id="y",
                options=var,
                value=var[1]["value"],
                clearable=False
            )
        ], style={
            "width": "45%"
        })

    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "backgroundColor": "white",
        "padding": "25px",
        "borderRadius": "15px",
        "boxShadow": "0 5px 20px rgba(0,0,0,0.1)",
        "marginBottom": "20px"
    }),

    html.Div([
        dcc.Graph(
            id="scatter",
            figure={}
        )
    ], style={
        "backgroundColor": "white",
        "padding": "15px",
        "borderRadius": "15px",
        "boxShadow": "0 5px 20px rgba(0,0,0,0.1)"
    })

], style={
    "padding": "40px",
    "maxWidth": "1400px",
    "margin": "auto"
})

# ----------------------------------------------------------------------- #
# Callback
# ----------------------------------------------------------------------- #

@callback(
    Output(
        component_id="scatter",
        component_property="figure"
    ),
    Input(
        component_id="x",
        component_property="value"
    ),
    Input(
        component_id="y",
        component_property="value"
    )
)
def update_graph(x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color="species",
        labels={
            x: x.replace("_", " ").capitalize(),
            y: y.replace("_", " ").capitalize()
        },
        title="Scatter Plot of the Iris Dataset"
    )

    return fig