# Third-Party Libraries
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

from src.application.usecases.create_workout import CreateWorkouts
from src.infra.repositories.workout import WorkoutsRepository
from src.infra.web.dropdowns.divisions import divisions
from src.infra.web.dropdowns.exercises import exercises
from src.infra.web.plots.plots import plot


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Div(id="loro"),
        html.Div([
            html.Nav([
                dbc.Button(
                    "Add treino", id="open-modal", className="me-1 navbar-items", n_clicks=0
                ),
                html.Div([
                    dcc.Dropdown(
                        divisions(),
                        id="division",
                        placeholder="Division",
                        className="col-md-12 navbar-items",
                    ),
                    dcc.Dropdown(
                        ["mês", "dia"],
                        id="period",
                        placeholder="Period",
                        className="col-md-12 navbar-items",
                    ),
                ], className="navbar-filter"),
            ], className="navbar"),

            html.Div([
                html.Div([dcc.Graph(figure=plot("chest"), className="graph")]),
                html.Div([dcc.Graph(figure=plot("back"), className="graph")]),

            ], className="graph-container")
        ], className="xaps"),
        dbc.Modal([
            dbc.ModalBody(
                [
                    dbc.Form(
                        dbc.Row([
                            dbc.Col(
                                dbc.Input(
                                    type="date",
                                    placeholder="Enter date",
                                    id="workout-date",
                                ),
                                className="col-md-12 graph-fields",
                            ),
                            dcc.Dropdown(
                                exercises(),
                                placeholder="Exercise",
                                id="workout-name",
                                className="col-md-12 graph-fields",
                            ),
                            dbc.Col(
                                dbc.Input(
                                    type="number",
                                    placeholder="Enter weight",
                                    id="workout-weight",
                                ),
                                className="col-md-12 graph-fields",
                            ),
                            dcc.Dropdown(
                                divisions(),
                                id="workout-type",
                                placeholder="Division",
                                className="col-md-12 graph-fields",
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "Submit",
                                    color="primary",
                                    n_clicks=0,
                                    id="workout-submit",
                                    href="/",
                                    external_link=True,
                                ),
                                width="auto",
                                className="graph-fields",
                            ),
                        ], className="col-md-8 graph-fields",
                        )
                    )
                ],
            )
        ], id="modal-training", is_open=False)
    ],
)


@app.callback(
    Output("loro", "children"),
    [
        Input("workout-date", "value"),
        Input("workout-name", "value"),
        Input("workout-weight", "value"),
        Input("workout-type", "value"),
        Input("workout-submit", "n_clicks"),
    ],
)
def create_workout(date, name, weight, type, submit):

    workout = {"date": date, "name": name, "weight": weight, "type": type}

    if submit == 1:
        repo = WorkoutsRepository()
        create = CreateWorkouts(repo)
        create.execute(workout)


@app.callback(
    Output("modal-training", "is_open"),
    Input("open-modal", "n_clicks"),
    State("modal-training", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open



