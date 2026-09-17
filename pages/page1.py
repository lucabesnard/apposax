import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px

# ----------------------------------------------------------------------- #
# Page
# ----------------------------------------------------------------------- #

dash.register_page(
    __name__,
    path="/page1",
    name="Page 1"
)

# ----------------------------------------------------------------------- #
# Sources
# ----------------------------------------------------------------------- #

# Récupération du dataset Gapminder
df = px.data.gapminder()

# Minimum et maximum des années disponibles
min_year, max_year = df.year.min(), df.year.max()

# Création des marqueurs pour le slider
slider_marks = {
    str(year): str(year)
    for year in df.year.unique()
}

# Récupération de la liste des continents
opt = df.continent.unique()

# État initial de la checklist
etat_initial = ["Asia"]

# ----------------------------------------------------------------------- #
# Interface
# ----------------------------------------------------------------------- #

layout = html.Div([

    html.Div([
        html.H1(
            "🌍 Gapminder",
            style={
                "fontSize": "45px",
                "fontWeight": "800",
                "marginBottom": "5px"
            }
        ),

        html.P(
            "Explorez les relations entre richesse, population et espérance de vie.",
            style={
                "fontSize": "18px",
                "opacity": "0.8",
                "marginBottom": "35px"
            }
        )
    ]),

    html.Div([
        html.H4("🌎 Continents"),
        dcc.Checklist(
            id="checklist",
            options=opt,
            value=etat_initial,
            inline=True
        )
    ], style={
        "backgroundColor": "white",
        "padding": "20px",
        "borderRadius": "15px",
        "marginBottom": "20px",
        "boxShadow": "0 5px 20px rgba(0,0,0,0.1)"
    }),

    html.Div([
        dcc.Graph(
            id="graph-gdp",
            figure={}
        )
    ], style={
        "backgroundColor": "white",
        "padding": "15px",
        "borderRadius": "15px",
        "boxShadow": "0 5px 20px rgba(0,0,0,0.1)",
        "marginBottom": "20px"
    }),

    html.Div([
        html.H4("📅 Année sélectionnée"),

        dcc.Slider(
            id="slider",
            min=min_year,
            max=max_year,
            value=max_year,
            marks=slider_marks,
            step=None
        )
    ], style={
        "backgroundColor": "white",
        "padding": "25px",
        "borderRadius": "15px",
        "boxShadow": "0 5px 20px rgba(0,0,0,0.1)"
    })

], style={
    "padding": "40px",
    "maxWidth": "1400px",
    "margin": "auto"
})

# ----------------------------------------------------------------------- #
# Serveur / Callback
# ----------------------------------------------------------------------- #

@callback(
    Output(
        component_id="graph-gdp",
        component_property="figure"
    ),
    Input(
        component_id="slider",
        component_property="value"
    ),
    Input(
        component_id="checklist",
        component_property="value"
    )
)
def update_graph(year_value, continent_value):

    df_update = df[
        (df.year == year_value)
        & df.continent.isin(continent_value)
    ]

    fig = px.scatter(
        df_update,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        size_max=60,
        title=f"Life expectancy by GDP per capita and population in {year_value}"
    )

    fig.update_xaxes(range=[-5000, 50000])
    fig.update_yaxes(range=[0, 100])

    return fig