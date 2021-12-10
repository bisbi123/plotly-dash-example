import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
)

# Plottin against a data set that looks like the following
# Country,      Year,   Status,     Life expectancy,    Population, GDP,        Schooling,  continent
# Afghanistan,  2015,   Developing, 65,                 33736494,   584.25921,  10.1,       Asia
# Afghanistan,  2014,   Developing, 59.9,               327582,     612.696514, 10,         Asia
# Afghanistan,  2013,   Developing, 59.9,               31731688,   631.744976, 9.9,        Asia
# Afghanistan,  2012,   Developing, 59.5,               3696958,    669.959,    9.8,        Asia
# Afghanistan,  2011,   Developing, 59.2,               2978599,    63.537231,  9.5,        Asia

fig = px.scatter(
    df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])

if __name__ == "__main__":
    app.run_server(debug=True)