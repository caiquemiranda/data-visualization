import dash
import dash_html_components as html

app =dash.Dash(__name__)

app.layout = html.Div(children= [
    html.H1('Demo: Plotly Express in dash with tips dataset'),
    html.H2('"I"m a sub-header'),

])

app.run_server(debug=True)