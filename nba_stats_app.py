
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="NBA Stats Analysis", layout="wide")
st.title("📊 NBA Stats - Análise Interativa")

@st.cache_data
def load_data():
    df = pd.read_csv("data/game_stats.csv")
    df['player_name'] = df['player'].apply(lambda x: eval(x)['first_name'] + ' ' + eval(x)['last_name'])
    df['team'] = df['team'].apply(lambda x: eval(x)['abbreviation'] if pd.notna(x) else 'N/A')
    df['pts'] = pd.to_numeric(df['pts'], errors='coerce')
    df['reb'] = pd.to_numeric(df['reb'], errors='coerce')
    df['ast'] = pd.to_numeric(df['ast'], errors='coerce')
    df['efficiency'] = df['pts'] + df['reb'] + df['ast']
    df['min'] = pd.to_numeric(df['min'].str.replace(":", "."), errors='coerce')
    df['season'] = df['game'].apply(lambda x: eval(x).get('season', 'Unknown'))
    return df

df = load_data()

tab1, tab2, tab3, tab4 = st.tabs(["🏀 Pontuação", "🔁 Rebotes", "⏱️ Minutos", "📈 Eficiência"])

with tab1:
    st.subheader("Top 10 jogadores por pontos totais")
    top_scorers = df.groupby("player_name")["pts"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_scorers)

with tab2:
    st.subheader("Top 10 jogadores por rebotes totais")
    top_rebs = df.groupby("player_name")["reb"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_rebs)

with tab3:
    st.subheader("Top 10 jogadores por minutos jogados")
    top_min = df.groupby("player_name")["min"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_min)

with tab4:
    st.subheader("Top 10 jogadores por eficiência média (PTS + REB + AST)")
    avg_eff = df.groupby("player_name")["efficiency"].mean().sort_values(ascending=False).head(10)
    st.bar_chart(avg_eff)

st.markdown("---")
st.caption("Fonte: API balldontlie.io | Projeto educacional com Python e Streamlit")
