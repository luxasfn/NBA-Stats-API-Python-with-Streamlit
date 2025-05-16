
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NBA Explorer", layout="wide")
st.title("🏀 NBA Explorer - Times, Jogadores e Jogos")

@st.cache_data
def load_data():
    teams = pd.read_csv("data/teams.csv")
    players = pd.read_csv("data/players.csv")
    games = pd.read_csv("data/games.csv")
    return teams, players, games

teams, players, games = load_data()

tab1, tab2, tab3 = st.tabs(["📋 Times", "👤 Jogadores", "📅 Jogos"])

with tab1:
    st.subheader("Lista de Times")
    st.dataframe(teams)
    st.bar_chart(teams["division"].value_counts())

with tab2:
    st.subheader("Distribuição de Jogadores por Posição")
    if "position" in players.columns:
        st.bar_chart(players["position"].value_counts())
    st.subheader("Jogadores por Time (Top 10)")
    if "team" in players.columns:
        team_names = players["team"].dropna().apply(lambda x: eval(x)["full_name"] if isinstance(x, str) and "full_name" in x else "Desconhecido")
        st.bar_chart(team_names.value_counts().head(10))

with tab3:
    st.subheader("Número de Jogos por Temporada")
    if "season" in games.columns:
        st.bar_chart(games["season"].value_counts().sort_index())

    st.subheader("Times Mandantes x Visitantes")
    if {"home_team", "visitor_team"}.issubset(games.columns):
        home = games["home_team"].apply(lambda x: eval(x)["abbreviation"] if isinstance(x, str) and "abbreviation" in x else "N/A")
        visitor = games["visitor_team"].apply(lambda x: eval(x)["abbreviation"] if isinstance(x, str) and "abbreviation" in x else "N/A")
        st.write("Top mandantes")
        st.bar_chart(home.value_counts().head(10))
        st.write("Top visitantes")
        st.bar_chart(visitor.value_counts().head(10))

st.markdown("---")
st.caption("Dados via API balldontlie.io — visualização baseada apenas em /teams, /players, /games.")
