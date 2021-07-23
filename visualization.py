import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


def start_visualization(server):
    dash_app = dash.Dash(server=server, name="Dashboard", url_base_pathname="/dashboard/")

    df = pd.read_csv("NBA_training_dataset.csv")

    dash_app.layout = html.Div(
        children=[
            html.H1(children="Data Visualization"),
            html.A("Home", href="/"),
            html.Br(),
            html.Br(),

            html.H2(children="Histogram of Number of NBA Players In Each BPM Range:"),
            dcc.Graph(
                id="bpm-histogram",
                figure=px.histogram(df, x="NBABPM"),
            ),
            html.Br(),
            html.Br(),

            html.H2(children="Feature Correlation Heatmap:"),
            html.H4(children="(Zoom in for more detail.)"),
            dcc.Graph(
                id="correlation-heatmap",
                figure=px.imshow(df.corr())
            ),
            html.Br(),
            html.Br(),

            html.H2(children="Scatterplot of Relationship Between NCAA BPM and NBA BPM:"),
            dcc.Graph(
                id="bpm-scatterplot",
                figure=px.scatter(df, x="NCAABPM", y="NBABPM")
            ),
            html.Br(),
            html.Br()
        ]
    )

    return dash_app
