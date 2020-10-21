import dash_html_components as html
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import dash_core_components as dcc

# get relative data folder
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
            # page 5
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Comparar"], className="subtitle padded"
                                    ),
                                    html.P(
                                        [
                                            "Esta página foi criada para que dois órgãos julgadores possam ser comparados."
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                    html.Br()
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            dcc.Dropdown(
                                id="filters-select",
                                options=[{'label': i, 'value': i} for i in df_dados['codOrgao'].unique()],
                                value='5760',
                                className="six columns"
                            ),
                            dcc.Dropdown(
                                id="filters-select",
                                options=[{'label': i, 'value': i} for i in df_dados['codOrgao'].unique()],
                                value='5760',
                                className="six columns"
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )