import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_ex_mov = pd.read_csv(DATA_PATH.joinpath("df_ex_mov.csv"))

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H3("Metodologia"),
                                    html.Br([]),
                                    dcc.Markdown('''
                                        Esse relatório tem como foco analisar indicadores gerais sobre os processos, bem como as transições das movimentações, de um tribunal, independente do tipo da ação. 
                                        A figura ilustra um exemplo em que há dois processos distintos com suas respectivas movimentações. O processo 1 apresenta um total de 5 movimentações, enquanto o processo 2 possui 4 movimentações. Cada letra representa uma situação do processo (Distribuição, Petição, Remessa, Decurso de Prazo, Conclusão etc). Cada par representa uma transição de movimentação, e o número entre as letras ilustra o tempo que levou para a transição.
                                        ''')
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Perguntas que orientam este relatório", className="subtitle padded"
                                    ),
                                    dcc.Markdown('''                                      
                                        Quais os tipos de transição de movimentação são mais frequentes?

                                        Quais os tipos de transição de movimentação levam mais tempo?
                                        
                                        Como está o desempenho em um tipo de transição de movimentação do meu órgão em relação aos demais que fazem parte do tribunal?
                                    '''),
                                    html.H6(
                                        "Métricas criadas para responder as questões", className="subtitle padded"
                                    ),
                                    dcc.Markdown('''                                      
                                        **Frequência da Transição de Movimentação (FTM):**  quantidade de movimentos por transição encontrados em todos os  processos dos órgãos do tribunal;
                                        
                                        **Tempo Médio da Transição (TMT):** mediana da soma dos dias que a transição leva ao longo de todos os processos dos órgãos do tribunal. 

                                        Desse modo, é possível que o tribunal, e seus respectivos órgãos, verifiquem quais são as transições mais recorrentes, bem como aquelas que mais levam tempo. A comparação entre órgãos permite que os gestores públicos aloquem mais recursos naquelas transições mais importantes e/ou recorrentes, e identifiquem possíveis gargalos em algumas transições específicas.
                                    '''),
                                    html.H6(
                                        "Movimentação de processos", className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("linha_proc.png"),
                                        className="linha_proc",
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Exemplo de movimentação"], className="subtitle padded",),
                                    html.Div(
                                        [
                                            html.Table(
                                                make_dash_table(df_ex_mov)
                                            )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )