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
                                    html.H6(["Selecione as Classes Processuais"], className="subtitle padded"),
                                    dcc.Dropdown(
                                        id="filter-classes",
                                        options=[{'label': i, 'value': i} for i in sgt_classes['codigo'].unique()],
                                        value='5760',
                                        multi=True,
                                    ),
                                    html.H6(["Selecione os Assuntos"], className="subtitle padded"),
                                    dcc.Dropdown(
                                        id="filter-assuntos",
                                        options=[{'label': i, 'value': i} for i in sgt_assuntos['codigo'].unique()],
                                        value='5760',
                                        multi=True,
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