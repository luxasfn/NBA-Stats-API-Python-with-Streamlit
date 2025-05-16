
# Projeto de Ciência de Dados com NBA Stats API

Este projeto tem como objetivo realizar análises exploratórias, estatísticas e visuais com dados obtidos da API oficial da NBA (https://www.balldontlie.io).

## Objetivos

- Coletar dados dinâmicos de jogadores e partidas da NBA
- Analisar estatísticas de desempenho (pontos, assistências, rebotes, etc.)
- Criar visualizações interativas e dashboards
- Identificar padrões e tendências entre jogadores, times e temporadas

## Tecnologias Utilizadas

- Python 3.x
- Requests
- Pandas
- Matplotlib / Seaborn / Plotly
- Jupyter Notebook
- Streamlit

## Estrutura

```
nba_stats_api_project/
├── data/                 # Dados salvos localmente
├── notebooks/            # Notebooks exploratórios
├── src/                  # Scripts Python para coleta e processamento
├── output/plots/         # Gráficos e resultados
├── nba_stats_app.py      # App interativo em Streamlit
├── diario_de_bordo.md    # Relato da construção do projeto
└── README.md
```

## Como Executar

1. Instale as dependências:
```bash
pip install requests pandas matplotlib seaborn plotly streamlit
```

2. Coleta de dados:
```bash
python src/api_request.py
python src/fetch_game_stats.py
```

3. Análises:
Abra os notebooks na pasta `/notebooks` para explorar os dados com Jupyter.

## Executando o App com Streamlit

Este projeto inclui um aplicativo interativo desenvolvido com [Streamlit](https://streamlit.io/) para explorar os dados de forma visual.

### Instalação do Streamlit

Caso não tenha instalado, execute:
```bash
pip install streamlit
```

### Como rodar o app

Estando na raiz do projeto, execute:

```bash
streamlit run nba_stats_app.py
```

O app irá abrir no seu navegador padrão e permitirá navegar pelas seguintes análises:

- Top 10 jogadores por pontos, rebotes e minutos jogados
- Ranking de eficiência combinada (PTS + REB + AST)
- Visualização interativa com filtros por temporada

## Licença

MIT License
