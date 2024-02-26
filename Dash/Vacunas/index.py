# %%
import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
#import dash_core_components as dcc
#import dash_html_components as html
from dash.dependencies import Input, Output, State

# %%
df = pd.read_csv(r'DataSets/Covid19VacunasAgrupadas.csv')
df.head()

# %%
app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.H1('Vacunados por Covid'),
        html.Img(src='assets/vacunados.jpg')
    ], className='banner')
])

# %%
if __name__ == '__main__':
    app.run_server(debug=True)

# %%
