import dash
from dash import html

dash.register_page(
    __name__,
    path="/",
    name="Accueil"
)

layout = html.Div([

    html.Div([
        html.H1(
            "🚀 DATA VISION",
            style={
                "fontSize": "60px",
                "fontWeight": "900",
                "marginBottom": "10px",
                "letterSpacing": "3px"
            }
        ),

        html.H2(
            "Bienvenue dans notre univers de données",
            style={
                "fontSize": "28px",
                "fontWeight": "400",
                "marginBottom": "30px"
            }
        ),

        html.P(
            "Une application interactive réalisée par",
            style={
                "fontSize": "18px",
                "marginBottom": "5px"
            }
        ),

        html.H3(
            "Nolhan Ménard & Luca Besnard",
            style={
                "fontSize": "32px",
                "fontWeight": "700",
                "marginBottom": "40px"
            }
        ),

        html.Div([

            html.Div([
                html.H2("🌍 Gapminder"),
                html.P(
                    "Explorez l'évolution de l'espérance de vie, "
                    "du PIB et de la population à travers le monde."
                ),
                html.A(
                    "Explorer →",
                    href="/page1",
                    style={
                        "textDecoration": "none",
                        "fontWeight": "bold"
                    }
                )
            ], style={
                "padding": "30px",
                "borderRadius": "20px",
                "backgroundColor": "white",
                "boxShadow": "0 10px 30px rgba(0,0,0,0.15)",
                "width": "300px"
            }),

            html.Div([
                html.H2("🌸 Iris"),
                html.P(
                    "Analysez les différentes caractéristiques "
                    "des fleurs Iris grâce à un graphique interactif."
                ),
                html.A(
                    "Explorer →",
                    href="/page2",
                    style={
                        "textDecoration": "none",
                        "fontWeight": "bold"
                    }
                )
            ], style={
                "padding": "30px",
                "borderRadius": "20px",
                "backgroundColor": "white",
                "boxShadow": "0 10px 30px rgba(0,0,0,0.15)",
                "width": "300px"
            })

        ], style={
            "display": "flex",
            "justifyContent": "center",
            "gap": "30px",
            "flexWrap": "wrap"
        })

    ], style={
        "textAlign": "center",
        "padding": "80px 30px",
        "minHeight": "80vh"
    })
])