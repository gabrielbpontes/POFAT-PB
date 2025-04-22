import logging

import streamlit as st

logger = logging.getLogger(__name__)

STYLES = {
    'main': """
        <style>
        /* Estilos gerais */
        .stApp {
            background: linear-gradient(180deg, #0E1117 0%, #1A1D24 100%);
            color: #FFFFFF;
        }
        
        /* Container principal */
        .main-container {
            max-width: 700px;
            margin: 0 auto;
            padding: 1rem 1.5rem;
        }
        
        /* Título */
        .title-container {
            text-align: center;
            margin-bottom: 1.5rem;
            position: relative;
            padding-top: 0.5rem;
        }
        .title-container::after {
            content: '';
            position: absolute;
            bottom: -0.75rem;
            left: 30%;
            width: 40%;
            height: 1px;
            background: linear-gradient(90deg, transparent, #FF5000, transparent);
        }
        .title {
            color: #FF5000;
            font-size: 3rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }
        
        /* Seções */
        .section {
            background: rgba(30, 30, 30, 0.3);
            border: 1px solid rgba(255, 80, 0, 0.1);
            border-radius: 6px;
            padding: 1.25rem 2rem;
            margin: 0 0.75rem 1.25rem 0.75rem;
            transition: all 0.3s ease;
            width: calc(100% - 1.5rem);
            min-height: 160px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            backdrop-filter: blur(5px);
        }
        .section:hover {
            border-color: #FF5000;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(255, 80, 0, 0.1);
        }
        .section-title {
            color: #FF5000;
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            letter-spacing: 0.5px;
            text-align: center;
        }
        .section-content {
            color: #808495;
            font-size: 0.9rem;
            line-height: 1.5;
            letter-spacing: 0.2px;
            text-align: justify;
            padding: 0 0.75rem;
            flex: 1;
            display: flex;
            align-items: center;
        }
        
        /* Footer */
        .footer {
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255, 80, 0, 0.1);
            color: #808495;
            font-size: 0.8rem;
            letter-spacing: 0.4px;
            text-align: center;
        }
        .footer strong {
            color: #FF5000;
        }

        /* Ajustes para elementos do Streamlit */
        .stMarkdown {
            background: transparent !important;
        }
        .stMarkdown p {
            color: #808495 !important;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
            color: #FF5000 !important;
        }
        </style>
    """,
    'title': 'color: #FF5000; font-size: 2rem; font-weight: 600; letter-spacing: 0.5px;',
    'text': 'color: #808495; font-size: 0.9rem; line-height: 1.5; letter-spacing: 0.2px;',
    'footer': 'color: #808495; font-size: 0.8rem; letter-spacing: 0.4px;',
}


def create_section(title: str, content: str) -> None:
    """Helper function to create consistent styled sections"""
    st.markdown(
        f"""
        <div class="section">
            <div class="section-title">{title}</div>
            <div class="section-content">{content}</div>
        </div>
    """,
        unsafe_allow_html=True,
    )


def exibir():
    try:
        st.markdown(STYLES['main'], unsafe_allow_html=True)

        st.markdown('<div class="main-container">', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="title-container">
                <div class="title">POFAT - PB</div>
                <p style='color: #808495; font-size: 1.1rem; letter-spacing: 0.5px;'>
                    Análise e Previsão de Acidentes de Trânsito na Paraíba
                </p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        create_section(
            'Objetivo do Projeto',
            'O projeto tem como objetivo analisar e prever a ocorrência de feridos em acidentes '
            'de trânsito no estado da Paraíba.',
        )

        create_section(
            'Metodologia',
            'Os dados utilizados neste estudo foram obtidos por meio de um processo robusto de ETL, '
            'realizado a partir da base de dados abertos sobre acidentes de trânsito disponibilizada '
            'pela Polícia Rodoviária Federal (PRF). Para o desenvolvimento do modelo preditivo, foram '
            'implementados e comparados algoritmos de aprendizado de máquina supervisionado, com destaque '
            'para Regressão Logística e Árvores de Decisão, visando identificar a abordagem mais eficiente '
            'para a previsão de feridos em acidentes de trânsito no estado da Paraíba.',
        )

        st.markdown(
            """
            <div class="footer">
                <p>UFPB - <strong>Aprendizagem Supervisionada</strong></p>
                <p>Professor: <strong>Alessio Tony</strong></p>
                <p>Alunos: <strong>Gabriel Pontes</strong> e <strong>Nercino Neto</strong></p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        logger.error(f'Erro ao exibir a página inicial: {str(e)}')
        st.error(
            'Ocorreu um erro ao carregar a página inicial. Por favor, tente novamente.'
        )
