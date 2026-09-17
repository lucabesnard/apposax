from dash import Dash, html, page_container
import dash

app = Dash(__name__, use_pages=True)
server = app.server # Indispensable pour Render

app.layout = html.Div([
    html.H1("Notre Application Collaborative"),
    html.Div([
        html.A(page['name'], href=page["relative_path"], style={"marginRight": "15px"})
        for page in dash.page_registry.values()
    ]),
    html.Hr(),
    page_container
])

if __name__ == '__main__':
    app.run(debug=True)