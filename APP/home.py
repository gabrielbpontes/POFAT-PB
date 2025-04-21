import streamlit as st

def exibir():
    st.title("POFAT - PB")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <h4 style='color: #FF5000;'> Objetivo do Projeto</h3>
        <p style='font-size:16px; color: white;'>
        O projeto tem como objetivo analisar e prever a ocorrência de feridos em acidentes
        de trânsito no estado da Paraíba.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h4 style='color: #FF5000;'> Metodologia</h3>
        <p style='font-size:16px; color: white;'>
        Os dados utilizados neste estudo foram obtidos por meio de um processo robusto de ETL, realizado a partir da base de dados abertos sobre
        acidentes de trânsito disponibilizada pela Polícia Rodoviária Federal (PRF). Para o desenvolvimento do modelo preditivo, foram implementados
        e comparados algoritmos de aprendizado de máquina supervisionado, com destaque para Regressão Logística e Árvores de Decisão, visando identificar
        a abordagem mais eficiente para a previsão de feridos em acidentes de trânsito no estado da Paraíba.
        </p>
        """, unsafe_allow_html=True)


    st.markdown("""
    <p style='font-size:14px; color: gray;'>
    UFPB - <strong>Aprendizagem Supervisionada</strong><br>
    Professor: <strong>Alessio Tony</strong><br>
    Alunos: <strong>Gabriel Pontes</strong> e <strong>Nercino Neto</strong>
    </p>
    """, unsafe_allow_html=True)


