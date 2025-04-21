import streamlit as st
import home
import dashboard
import simulator

st.set_page_config(page_title="POFAT - PB", layout="wide")

# Barra lateral com selectbox
st.sidebar.title("Menu de Navegação")
pagina = st.sidebar.selectbox(
    "Selecione:",
    ("Home", "Dashboard Interativo", "Simulador de Previsões")
)

# Carregar a página correta
if pagina == "Home":
    home.exibir()
elif pagina == "Dashboard Interativo":
    dashboard.exibir()
elif pagina == "Simulador de Previsões":
    simulator.exibir()

