import dash_html_components as html
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import dash_core_components as dcc

# get relative data folder
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
                                            "Esta página deverá ser projetada para adicinar ao fluxo que o usuário já vinha a ideia da comparação entre as serventias.\
                                            Ela já iniciará carregada com informações das duas últimas serventias escolhidas na página anterior e convidará\
                                            o usuário a selecionar outras nos filtos. Os dados apresentados deverão adicionar um elemento de Gamefication, que\
                                            gere um sentimento de competitividade e o induza a buscar como as outras serventias resolvem problemas que ele também tem."
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
                                options=[{'label': j, 'value': i} for (i,j) in df_dados[['codOrgao','Serventia']].drop_duplicates().values],
                                value='5760',
                                className="six columns"
                            ),
                            dcc.Dropdown(
                                id="filters-select",
                                options=[{'label': j, 'value': i} for (i,j) in df_dados[['codOrgao','Serventia']].drop_duplicates().values],
                                value='5766',
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