import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table, plot_with_filter
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# Carrega tabelas
sgt_classes = pd.read_csv(DATA_PATH.joinpath('sgt_classes.csv'), sep=';')
sgt_assuntos = pd.read_csv(DATA_PATH.joinpath('sgt_assuntos.csv'), sep=';')

# lendo DataFrame pré-processado
df_dados = pd.read_csv(DATA_PATH.joinpath("pares.csv")).dropna().drop('transicao_movimento',axis=1)
# Obter dados das serventias
mpm_serventias = pd.read_csv(DATA_PATH.joinpath("mpm_serventias.csv"), sep=";").set_index('SEQ_ORGAO')[['NOMEDAVARA']]
df_dados = df_dados.merge(mpm_serventias,left_on="orgaoJulgador.codigoOrgao", right_index=True)
df_dados.columns = ['Tribunal','codOrgao','Quantidade','Tempo mínimo','Tempo máximo','Tempo médio','C1','C2','Movimento 1', 'Movimento Subsequente','Serventia']

df_dados = df_dados.astype({'C1': 'object'})
df_dados = df_dados.astype({'C2': 'object'})
df_dados = df_dados.astype({'codOrgao': 'object'})

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P(
                                        ["Esta página deverá apresentar informações específicas de uma Unidade como métricas e KPIs. Conforme ele seleciona os filtros, os graficos abaixo refletem a seleção."],
                                    ),
                                    html.Br(),
                                    html.H6(["Selecione a Unidade de Origem"], className="subtitle padded"),
                                    dcc.Dropdown(
                                        id="filters-select",
                                        #options=[{'label': i, 'value': i} for i in df_dados['codOrgao'].unique()],
                                        options=[{'label': j, 'value': i} for (i,j) in df_dados[['codOrgao','Serventia']].drop_duplicates().values],
                                        value='5760',
                                    ),
                                    html.H6(["Selecione as Classes Processuais"], className="subtitle padded"),
                                    dcc.Dropdown(
                                        id="filter-classes",
                                        options=[{'label': j, 'value': i} for (i,j) in sgt_classes[['codigo','descricao']].drop_duplicates().values],
                                        #options=[{'label': i, 'value': i} for i in sgt_classes['codigo'].unique()],
                                        value='5760',
                                        multi=True,
                                    ),
                                    html.H6(["Selecione os Assuntos"], className="subtitle padded"),
                                    dcc.Dropdown(
                                        id="filter-assuntos",
                                        options=[{'label': j, 'value': i} for (i,j) in sgt_assuntos[['codigo','descricao']].drop_duplicates().values],
                                        #options=[{'label': i, 'value': i} for i in sgt_assuntos['codigo'].unique()],
                                        value='5760',
                                        multi=True,
                                    ),
                                    html.Br(),
                                    html.Br(),
                                    html.Img(
                                        src=app.get_asset_url("dashboard.png"),
                                        style={'height':'100%', 'width':'100%'},
                                        className="linha_proc"
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="rows",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )