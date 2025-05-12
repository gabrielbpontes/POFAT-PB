from datetime import datetime

import dashboard
import simulator
import sobre
import streamlit as st

st.set_page_config(
    page_title='POFAT - PB', page_icon='🚗', initial_sidebar_state='expanded'
)

st.markdown(
    """
    <style>
    /* Desabilitar opções de tema e layout */
    .stDeployButton {
        display: none !important;
    }
    .stApp > header {
        display: none !important;
    }
    .stApp > div:first-child {
        display: none !important;
    }

    /* Forçar tema escuro */
    .stApp {
        background: linear-gradient(180deg, #0E1117 0%, #1A1D24 100%) !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A1D24 0%, #0E1117 100%) !important;
        padding: 1.5rem 1rem;
    }

    /* Logo e título */
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
    }
    .logo-container::after {
        content: '';
        position: absolute;
        bottom: -0.75rem;
        left: 30%;
        width: 40%;
        height: 1px;
        background: linear-gradient(90deg, transparent, #FF5000, transparent);
    }
    .logo {
        color: #FF5000;
        font-size: 1.75rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #808495;
        font-size: 0.9rem;
        letter-spacing: 0.2px;
    }

    /* Botões de navegação */
    .nav-button {
        background: rgba(30, 30, 30, 0.3);
        border: 1px solid rgba(255, 80, 0, 0.1);
        border-radius: 6px;
        padding: 0.75rem 1.25rem;
        margin: 0.5rem 0;
        width: 100%;
        text-align: center;
        color: #FFFFFF;
        font-size: 0.9rem;
        font-weight: 500;
        letter-spacing: 0.2px;
        transition: all 0.3s ease;
        cursor: pointer;
        backdrop-filter: blur(5px);
    }
    .nav-button:hover {
        background: rgba(255, 80, 0, 0.1);
        border-color: #FF5000;
        transform: translateX(4px);
    }
    .nav-button.active {
        background: rgba(255, 80, 0, 0.15);
        border-color: #FF5000;
    }

    /* Links úteis */
    .links-section {
        margin-top: 2rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 80, 0, 0.1);
    }
    .links-title {
        color: #FF5000;
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 1rem;
        text-align: center;
    }
    .link-item {
        display: flex;
        align-items: center;
        padding: 0.5rem 0.75rem;
        margin: 0.25rem 0;
        color: #808495;
        font-size: 0.8rem;
        text-decoration: none;
        transition: all 0.3s ease;
        border-radius: 4px;
    }
    .link-item:hover {
        background: rgba(255, 80, 0, 0.1);
        color: #FFFFFF;
        transform: translateX(4px);
    }
    .link-icon {
        margin-right: 0.5rem;
        color: #FF5000;
    }

    /* Footer */
    .footer {
        margin-top: 2rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255, 80, 0, 0.1);
        text-align: center;
    }
    .version {
        color: #FF5000;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.2px;
    }
    .copyright {
        color: #808495;
        font-size: 0.7rem;
        letter-spacing: 0.2px;
        margin-top: 0.5rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown(
        """
        <div class="logo-container">
            <div class="logo">POFAT - PB</div>
            <div class="subtitle">Análise e Previsão de Acidentes</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button('Sobre', key='home_btn', use_container_width=True):
        st.query_params['page'] = 'sobre'
    if st.button('Dashboard', key='dashboard_btn', use_container_width=True):
        st.query_params['page'] = 'dashboard'
    if st.button('Simulador', key='simulator_btn', use_container_width=True):
        st.query_params['page'] = 'simulator'

    current_year = datetime.now().year

    st.markdown(
        '<div class="footer"><p class="version">Versão: 2.0.0</p></div>',
        unsafe_allow_html=True,
    )

pagina = st.query_params.get('page', 'sobre')

if pagina == 'sobre':
    sobre.exibir()
elif pagina == 'dashboard':
    dashboard.exibir()
elif pagina == 'simulator':
    simulator.exibir()
