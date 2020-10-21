# Movimenta Analytics

O Movimenta Analytics permite que os tribunais e seus órgãos avaliem o comportamento das movimentações processuais, permitindo o diagnóstico para fundamentar decisões em favor da melhoria do desempenho judicial. A aplicação foca na sistematização e organização das movimentações processuais, por meio da análise dos pares de transição desses movimentos. 

# Entregas:

- [Demo Live](http://192.34.57.12/movimenta/overview)
- [Video]()
-


## Descrição das tecnologias

Esta aplicação foi criada utilizando o framework interarivo do Python [Dash](https://plot.ly/products/dash/) desenvolvido pelo [Plotly](https://plot.ly/). Todas estas tecnologias são open-source e possibilitam o uso de bibliotecas que são o estado da arte na Ciência de Dados. O Dash abstrai toda a tecnologia e protocolos necessários para criar aplicações Web interativas e é uma forma simples e efetiva de apresentar as informações obtidas por meio do processamento com as bibliotecas do Python. Com isso é possível criar painéis e relatórios interativos focados na persona para o qual ele foi concebido, livrando o usuário de ter de interagir com sistemas complexos de Dashboard, como o Kibana. 

O Movimenta Analytics foi pensado de forma que ele possa ser facilmente integrado à tecnologia ElasticSearch, utilizada no sistema Datajud. Esta versão Demo utiliza porções de dados pré-processados, obtidos do Dataset fornecido no desafio. Os algoritmos aplicados nestes pré-processamentos estão documentados no diretório Notebooks, em arquivos do Jupyter Notebooks, que foram criados com objetivo de facilitar sua transcrição na linguagem de consulta do Elasticsearch. Esta implementação traria uma maior performance nas consultas e dispensaria o servidor do Movimenta Analytics para que se dedique a processar apenas a visualização dos dados, já que hoje ele realiza as tarefas de consulta e apresentação dos dados simultaneamente. 

O Dash é uma biblioteca versátil que possibilita a criação de diversos tipos de Dashboards. Nossa equipe optou por utilizar uma interface que se parece com um relatório real, semelhante a um PDF ou mesmo um documento impresso, pensando nas personas indicadas no desafio. Esperamos que as pessoas com menor habilidade em operar o computador não se sintam intimidados por uma interface complexa. Utilizamos as técnicas de Design Thinking e Storytelling buscando inserir os elementos de texto, filtros e as informações dinâmicas de forma gradual dentre as diferentes páginas da aplicação, tomando o cuidado em manter um contexto em cada uma e não sobrecarregar a tela.

## Aonde este relatório pode ser aplicado

Embora nossa equipe tenha focado no assunto código 1116 de Execução Fiscal, que representa o maior volume de processos em praticamente todos os Tribunais Estaduais, a Metodologia de análise do Tempo Médio entre os pares de Movimentação pode ser aplicada em qualquer Classe/Assunto de processo. Para ilustrar esta possibilidade, o relatório apresenta na primeira página um filtro do tipo `Radio Button` para seleção de qual Justiça o usuário pretende analisar. Neste demo este filtro estará travado em Justiça Estadual apenas por estarmos trabalhando com uma base de dados pré-processada.

## Como o app está dividido

O Relatório de Movimentação Processual está subdividido em 5 páginas no menu principal para as informações e 1 página acessada em um botão separado com a metodologia. Espera-se que o usuário siga a ordem das páginas apresentadas no menu principal. A seguir detalharemos cada página.

### Visão Geral

Esta é a página inicial da aplicação em que é apresentado ao usuário o que é o Datajud e de onde vêm as informações dele. Em seguida o usuário já é apresentado a um pequeno filtro, para que ele selecione os dados de qual Justiça serão apresentados no decorrer do relatório. Abaixo deste filtro serão apresentadas KPIs e informações gerais, que apresentem a dimensão e volume de processos entre os órgãos

### Metodologia
### Visão Geral
### Unidade de Origem
### Movimentações 
### Comparar
### Destaques

## Rodando o app localmente

O Movimenta Analytics foi criado utilizando Docker já pensando na melhor forma de integrá-lo à nuvem do CNJ

`$ docker build -t plotly:cnj .`
`$ docker run -v $(pwd)/app:/app  --restart always -p 80:8050 plotly:cnj`

## Tecnologias utilizadas

- [Python]
- [Pandas]
- [R]
- [Dash](https://dash.plot.ly/) - Main server and interactive components
- [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots
