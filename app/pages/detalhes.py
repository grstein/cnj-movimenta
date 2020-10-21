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
            # page 4
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Órgão Julgador"], className="subtitle padded"),
                                    html.P(),
                                    html.P(['Esta página foi criada para que o usuário possa selecionar um Órgão Julgador específico\
                                    e visualizar a métrica específicas dele. O objetivo é que o usuário que conheça mais da realidade\
                                    específica daquela unidade compreenda de forma geral o padrão de movimentação dos processos.']),
                                    html.P(['O filtro foi criado para que o usuário explore dados de outras serventias, com o objetivo principal\
                                    de que ele encontre padrões de movimentação mais eficiêntes que em sua própria Vara e busque \
                                    informações com estes órgãos, a fim de incorporar as mesmas práticas em seu dia a dia.']),
                                    html.P(['Logo abaixo encontra-se um filtro do tipo "De -> Para" que foi criado com o intúito de facilitar a análise\
                                    das movimentações. Com ele é possível selecionar todos os pares de movimentação em que o Movimento 1 seja, por exemplo, "Petição" \
                                    e verificar quais seriam os Movimentos Subsequentes e suas estatísticas.']),
                                    dcc.Dropdown(
                                        id="filters-select",
                                        #options=[{'label': i, 'value': i} for i in df_dados['codOrgao'].unique()],
                                        options=[{'label': j, 'value': i} for (i,j) in df_dados[['codOrgao','Serventia']].drop_duplicates().values],
                                        value='5760',
                                    ),
                                    #html.H6(["Filtro De -> Para"], className="subtitle padded"),
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="filters-from",
                                                options=[{'label': i, 'value': i} for i in np.sort(df_dados['Movimento 1'].unique())],
                                                placeholder="Filtro pelo movimento 1",
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
                                                placeholder="Filtro pelo movimento subsequente",
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
                                    html.H6(["Árvore de movimentos"], className="subtitle"),
                                    html.P(),
                                    html.P(['Este gráfico apresenta as informações de movimentação dos processos em forma de árvore\
                                    onde cada cor e, portanto, os retângulos mais externos, representam o Movimento 1 e dentro destes, os\
                                    retângulos representam o Movimento Subsequente. Experimente clicar neles, a árvore irá se ajustar à\
                                    visualização do movimento desejado. Este gráfico também obedece o filtro da serventia lá em cima e se atualiza junto com a tabela.']),
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