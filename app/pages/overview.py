import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table, plot_with_filter

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

# ler tabela de movimentos
sgt_movimentos = pd.read_csv(DATA_PATH.joinpath('sgt_movimentos.csv'), sep=';')
sgt_movimentos['codigo'] = sgt_movimentos['codigo'].astype(float)
sgt_movimentos.set_index('codigo', inplace=True)

# ler dados básicos 
df_base = pd.read_csv(DATA_PATH.joinpath('dados_basicos.csv'), index_col=0)
df_base['dadosBasicos.dataAjuizamento'] = pd.to_datetime(df_base['dadosBasicos.dataAjuizamento'],format='%Y%m%d%H%M%S', errors='coerce')

# ler dados movimento
df_moves = pd.read_csv(DATA_PATH.joinpath('movimentos.csv'), index_col=0)
df_moves['dataHora'] = pd.to_datetime(df_moves['dataHora'], format='%Y%m%d%H%M%S')

# Quantidade de movimentos do processo
df_base['n_movimentos'] = df_moves.groupby('dadosBasicos.numero').size()
df_base['n_movimentos'].fillna(0, inplace=True)

# Adiona campo de sigla do tribunal para table de dados básicos
df_moves = df_moves.merge(df_base['siglaTribunal'], left_index=True, right_index=True)

qtd_mov = df_moves.groupby(['siglaTribunal', pd.Grouper(freq='M', key='dataHora')]).size().unstack().T
qtd_mov.sort_index(inplace=True)

qtd_proc = df_base.groupby(['siglaTribunal', pd.Grouper(key='dadosBasicos.dataAjuizamento', freq='M')]).size().unstack().T
qtd_proc.index.name = 'Data'
qtd_proc = qtd_proc.loc['2010':'2020'].fillna(0).sort_index()

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H4("Sobre este relatório"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                        Conforme o artigo 3º da Resolução CNJ n. 331 de 20/08/2020, que institui a Base Nacional de Dados do Poder Judiciário – DataJud \
                                        como fonte primária de dados do Sistema de Estatística do Poder Judiciário – SIESPJ, os tribunais devem alimentar a Base com \
                                        dados e metadados processuais relativos a todos os processos físicos ou eletrônicos, públicos ou sigilosos, de qualquer das \
                                        classes previstas nas Tabelas Processuais Unificadas –TPUs, criadas pela Resolução CNJ n. 46/2007.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    html.Div(
                        [
                            html.H6(["Selecione a Justiça que pretente avaliar"], className="subtitle padded"),
                            dcc.RadioItems(
                                options=[
                                    {'label': 'Justiça Eleitoral', 'value': 'JEL', 'disabled': True},
                                    {'label': 'Justiça Estadual', 'value': 'JES'},
                                    {'label': 'Justiça Federal', 'value': 'JFE', 'disabled': True},
                                    {'label': 'Justiça Militar', 'value': 'JUM', 'disabled': True},
                                    {'label': 'Justiça do Trabalho', 'value': 'JTR', 'disabled': True},
                                    {'label': 'Tribunais Superiores', 'value': 'JSU', 'disabled': True}
                                ],
                                value='JES',
                                labelStyle={'display': 'inline-block'}
                            ),
                            dcc.Graph(
                                figure=plot_with_filter(
                                    data=qtd_proc,
                                    title='Quantidade de processos do tribunal',
                                    xlabel='Data',
                                    ylabel='Quantidade de processos'
                                )
                            ),
                            dcc.Graph(
                                figure=plot_with_filter(
                                    data=qtd_mov,
                                    title='Quantidade de movimentações do tribunal',
                                    xlabel='Data',
                                    ylabel='Quantidade de movimentações'
                                )
                            ),
                            #html.H6(["Selecione a Justiça que pretente avaliar"], className="subtitle padded"),

                        ],
                        className="twelve rows",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )