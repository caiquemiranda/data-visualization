import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app =dash.Dash(__name__)

app.layout = html.Div(children= [
    html.H1('Demo: Plotly Express in dash with tips dataset'),
    dcc.Input(id='x'),
    html.H2(id='x_out'),

])

@app.callback(Output('x_out','children'), [Input('x', 'value')])

def cb(x):
    return x

app.run_server(debug=True)