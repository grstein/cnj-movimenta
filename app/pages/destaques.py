import dash_html_components as html
from utils import Header


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Notícias", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "15/10/20 CNJ inaugura o “Sistema Movimenta” que auxiliará não só aos operadores do direito a análise, de modo simplificado, dos gargalos das movimentações, como também ao próprio CNJ a direcionar seus esforços de maneira eficiente e direta."
                                            ),
                                            html.P(
                                                "21/10/20 Nova jurisprudência visa simplificar processos de Execução Fiscal."
                                            ),
                                            html.P(
                                                "23/10/20 Resolução 345/2020 do CNJ regulamenta o “Juízo 100% digital” – “Sistema Movimenta” será utilizado como indicador de produtividade e celeridade previsto no artigo 7º."
                                            ),
                                            html.P(
                                                "29/10/20 Equipe 36 ganha competição do “CNJ Inova” com relatório de movimentação processual interativo."
                                            ),  
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.H6("Outras Informações", className="subtitle padded"),
                                    html.Div(
                                        [
                                            html.P(
                                                "Visando a concretização do princípio constitucional do amplo e célere acesso à Justiça, bem como promover o incremento da celeridade e da eficiência da prestação jurisdicional o Conselho Nacional de Justiça busca a modernização de todo o sistema judiciário, principalmente buscando a utilização de ferramentas computacionais. Assim é que diversas são as diretrizes e projetos instituídas, tais como o Processo Judicial Eletrônico (PJe)."
                                            ),
                                            html.Br([]),
                                            html.P(
                                                "Importa considerar ainda, dentre as atribuições do CNJ (previstas no art. 103-B, §4º da Constituição Federal) o controle de atuação administração e financeira e a coordenação do planejamento estratégico do Poder Judiciário, inclusive na área de tecnologia da informação, tornam-se como pilares para o incremento do novo projeto nominado 'Juízo 100% Digital'."
                                            ),
                                            html.Br([]),
                                            html.P(
                                                "Assim, o “MOVIMENTA ANALYTICS” se caracteriza como ferramenta hábil, estratégia inteligência de controle interno de processos para que se possa, de modo simples, célere e eficaz analisar e alertar sobre possíveis gargalos no tempo de tramitação processual.  Permite também a construção de um diagnóstico para oportunizar ao CNJ a implantação das imprescindíveis medidas assertivas que permitirão a eficiência dos atos. Pode-se mesmo afirmar que será uma ferramenta de grande valia para o “compliance digital” da administração pública."
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )