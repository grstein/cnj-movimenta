import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

from utils import Header, make_dash_table, generate_table
import pandas as pd
import numpy as np
import pathlib
import dash_table as dt

# obter diretório relativo de dados
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# lendo DataFrame pré-processado
df_dados = pd.read_csv(DATA_PATH.joinpath("pares.csv"))
df_dados = df_dados.dropna()
df_dados = df_dados.drop('transicao_movimento',axis=1)
df_dados.columns = ['Tribunal','codOrgao','Quantidade','Tempo mínimo','Tempo máximo','Tempo médio','C1','C2','Movimento 1', 'Movimento Subsequente']

df_dados = df_dados.astype({'C1': 'object'})
df_dados = df_dados.astype({'C2': 'object'})
df_dados = df_dados.astype({'codOrgao': 'object'})

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 4
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Órgão Julgador"], className="subtitle padded"),
                                    dcc.Dropdown(
                                        id="filters-select",
                                        options=[{'label': i, 'value': i} for i in df_dados['codOrgao'].unique()],
                                        value='5760',
                                    ),
                                    #html.H6(["Filtro De -> Para"], className="subtitle padded"),
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="filters-from",
                                                options=[{'label': i, 'value': i} for i in np.sort(df_dados['Movimento 1'].unique())],
                                                placeholder="Filtre pelo movimento",
                                                value='None',
                                            ),
                                        ],
                                        className="six columns",
                                    ),
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="filters-to",
                                                options=[{'label': i, 'value': i} for i in np.sort(df_dados['Movimento Subsequente'].unique())],
                                                placeholder="Filtre pelo movimento subsequente",
                                                value='None',
                                            ),
                                        ],
                                        className="six columns",
                                    ),
                                    html.Br(),
                                    # Desenha a tabela de principais movimentações
                                    html.Table(id='my-output')
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Heatmap"], className="subtitle"),
                                    dcc.Graph(
                                        id='square-map'
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )