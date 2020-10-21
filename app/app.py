# -*- coding: utf-8 -*-
import pathlib
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from utils import generate_table
from dash.dependencies import Input, Output
from pages import (
    overview,
    metodologia,
    minhaVara,
    detalhes,
    distributions,
    newsReviews,
)

# obter diretório relativo de dados
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()
ASSETS_PATH = PATH.joinpath("./assets").resolve()

### lendo DataFrame pré-processado
df_dados = pd.read_csv(DATA_PATH.joinpath("pares.csv"))
df_dados = df_dados.dropna()
df_dados.columns = ['Transição','Tribunal','codOrgao','Quantidade','Tempo mínimo','Tempo máximo','Tempo médio','C1','C2','Movimento 1', 'Movimento Subsequente']

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],suppress_callback_exceptions=True
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Callback que cria a tabela de movimentos filtrada
@app.callback(
    Output('my-output', 'children'),
    [Input('filters-select', 'value'),
    Input('filters-from', 'value'),
    Input('filters-to', 'value')]
)
def update_output_div(fselect,ffrom,fto):
    filtered_df = df_dados[df_dados['codOrgao'] == int(fselect)]
    if ffrom != 'None':
        filtered_df = filtered_df[filtered_df['Movimento 1'] == ffrom]
    if fto != 'None':
        filtered_df = filtered_df[filtered_df['Movimento Subsequente'] == fto]
    print(ffrom)
    plt.figure(figsize=(200,200))
    df_pivot = filtered_df.pivot('C1','C2','Tempo médio')   
    return generate_table(filtered_df[['Movimento 1', 'Movimento Subsequente','Quantidade','Tempo mínimo','Tempo máximo','Tempo médio']].sort_values('Quantidade',ascending=False))

# Callback que cria a arvore de quadros
@app.callback(
    Output('square-map', 'figure'),
    [Input('filters-select', 'value')]
)
def update_output_div(input_value):
    filtered_df = df_dados[df_dados['codOrgao'] == int(input_value)]
    #fig = px.scatter(filtered_df, x="Quantidade", y="Tempo médio", hover_name="Transição")
    fig = px.treemap(filtered_df, path=['Movimento 1','Movimento Subsequente'], values='Quantidade')
    return fig

# Atualizar página
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/movimenta/metodologia":
        return metodologia.create_layout(app)
    elif pathname == "/movimenta/minha-vara":
        return minhaVara.create_layout(app)
    elif pathname == "/movimenta/detalhes":
        return detalhes.create_layout(app)
    elif pathname == "/movimenta/distributions":
        return distributions.create_layout(app)
    elif pathname == "/movimenta/news-and-reviews":
        return newsReviews.create_layout(app)
    elif pathname == "/movimenta/full-view":
        return (
            overview.create_layout(app),
            metodologia.create_layout(app),
            minhaVara.create_layout(app),
            detalhes.create_layout(app),
            distributions.create_layout(app),
            newsReviews.create_layout(app),
        )
    else:
        return overview.create_layout(app)

if __name__ == "__main__":
    app.run_server(debug=True,host='0.0.0.0')