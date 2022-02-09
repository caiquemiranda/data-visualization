from multiprocessing.sharedctypes import Value
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px


tips = px.data.tips()
col_options = [dict(label=x, value=x) for x in tips.columns]

app =dash.Dash(__name__)

app.layout = html.Div(children= [
    html.H1('Demo: Plotly Express in dash with tips dataset'),
    dcc.Dropdown(id='x', options=col_options),
    dcc.Graph(id='graph', figure=px.scatter(tips)),

])

@app.callback(Output('graph','figure'), [Input('x', 'value')])

def cb(x):
    return px.scatter(tips, x=x)

app.run_server(debug=True)