# Third-Party Library
import plotly.graph_objs as go


def build_figure(data):
    figure = []

    for name in data["name"].unique():
        workout_filter = data[data["name"] == name]
        figure.append(
            {
                "orientation": "v",
                "type": "bar",
                "x": workout_filter["date"],
                "y": workout_filter["weight"],
                "showlegend": True,
                "name": name,
            }
        )

    layout = {
        "barmode": "group",
        "legend": {
            "orientation": "h", "y": -0.3},
        "margin": {"t": 60, "r": 50, "b": 100},
        "title": {"text": data["type"][0].capitalize(), "pad": {"l": 250, "r": 250}},
        "yaxis": {"title": "Weight"},
        "xaxis": {"title": "Date"},
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
    }

    return go.Figure(data=figure, layout=layout)
