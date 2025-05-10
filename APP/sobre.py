import logging

import streamlit as st
from utils import footer

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
            'implementados e comparados diferentes algoritmos de aprendizado de máquina supervisionado: '
            'Regressão Logística, K-Nearest Neighbors (KNN) e Random Forest, visando identificar a '
            'abordagem mais eficiente para a previsão de feridos em acidentes de trânsito no estado da Paraíba.',
        )

        create_section(
            'Modelos Disponíveis',
            '<ul><li>Regressão Logística: Modelo estatístico que estima a probabilidade de ocorrência de feridos em acidentes de trânsito, '
            'considerando variáveis como condições climáticas, tipo de via e horário do acidente. Ideal para identificar '
            'fatores de risco mais significativos.</li>'
            '<li>K-Nearest Neighbors (KNN): Algoritmo que classifica novos acidentes baseado em padrões similares já registrados, '
            'considerando características como localização, tipo de colisão e condições da via. Excelente para capturar '
            'relações não-lineares nos dados.</li>'
            '<li>Random Forest: Ensemble de árvores de decisão que analisa múltiplos aspectos dos acidentes simultaneamente, '
            'como condições meteorológicas, tipo de veículo e características da rodovia. Oferece alta precisão e '
            'robustez na previsão de feridos.</li></ul>',
        )

        create_section(
            'Informações Gerais',
            '<ul>'
            '<li>Turma: UFPB - Aprendizagem Supervisionada</li>'
            '<li>Professor: <a href="https://www.linkedin.com/in/alessio-almeida-24b25282/" target="_blank" style="color: #FF5000; text-decoration: none;">Alessio Tony</a></li>'
            '<li>Alunos: '
            '<a href="https://www.linkedin.com/in/gabriel-pontes-2152a9276/" target="_blank" style="color: #FF5000; text-decoration: none;">Gabriel Pontes</a> e '
            '<a href="https://www.linkedin.com/in/nercino-neto/" target="_blank" style="color: #FF5000; text-decoration: none;">Nercino Neto</a>'
            '</li>'
            '<li><a href="https://github.com/gabrielbpontes/POFAT-PB" target="_blank" style="color: #FF5000; text-decoration: none;">Repositório do Projeto</a></li>'
            '</ul>',
        )

        footer()

    except Exception as e:
        logger.error(f'Erro ao exibir a página inicial: {str(e)}')
        st.error(
            'Ocorreu um erro ao carregar a página inicial. Por favor, tente novamente.'
        )
