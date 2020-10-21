import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("datajud-logo.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("Metodologia", id="learn-more-button"),
                        href="/movimenta/metodologia",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Relatório de Movimentação Processual")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Relatório completo",
                                href="/movimenta/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Visão Geral",
                href="/movimenta/overview",
                className="tab first",
            ),
            #dcc.Link(
            #    "Metodologia",
            #    href="/movimenta/price-performance",
            #    className="tab",
            #),
            dcc.Link(
                "Minha Vara",
                href="/movimenta/minha-vara",
                className="tab",
            ),
            dcc.Link(
                "Movimentações", href="/movimenta/detalhes", className="tab"
            ),
            dcc.Link(
                "Comparar",
                href="/movimenta/distributions",
                className="tab",
            ),
            dcc.Link(
                "Destaques",
                href="/movimenta/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Funcao que retrna plot com filtro para página "Minha Vara"
def plot_with_filter(data, xlabel, ylabel, title):
    # plotly
    fig = go.Figure()

    # set up ONE trace
    fig.add_trace(go.Scatter(x=data.index, y=data[data.columns[0]], visible=True))
    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel
    )
    updatemenu = []
    buttons = []

    # button with one option for each dataframe
    for col in data.columns:
        buttons.append(
            dict(
                method='restyle',
                label=col,
                visible=True,
                args=[{'y':[data[col]], 'x':[data.index],'type':'scatter'}, [0]],
            )
        )

    # some adjustments to the updatemenus
    updatemenu = []
    your_menu = dict()
    updatemenu.append(your_menu)

    updatemenu[0]['buttons'] = buttons
    updatemenu[0]['direction'] = 'down'
    updatemenu[0]['showactive'] = True

    # add dropdown menus to the figure
    fig.update_layout(showlegend=False, updatemenus=updatemenu)
    return fig