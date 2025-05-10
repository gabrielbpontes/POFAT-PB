import pickle

import pandas as pd
import streamlit as st
from utils import footer

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
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 1.5rem;
        }

        /* Título */
        .title-container {
            text-align: center;
            margin-bottom: 2rem;
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
            font-size: 2.5rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-bottom: 0.5rem;
        }

        /* Seções */
        .section {
            background: rgba(30, 30, 30, 0.3);
            border: 1px solid rgba(255, 80, 0, 0.1);
            border-radius: 6px;
            padding: 1.25rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
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
            margin-bottom: 1rem;
            letter-spacing: 0.5px;
        }

        /* Filtros */
        .filter-container {
            background: rgba(30, 30, 30, 0.3);
            border: 1px solid rgba(255, 80, 0, 0.1);
            border-radius: 6px;
            padding: 1.25rem;
            margin-bottom: 2rem;
            backdrop-filter: blur(5px);
        }

        /* Métricas */
        .metric-container {
            background: rgba(30, 30, 30, 0.3);
            border: 1px solid rgba(255, 80, 0, 0.1);
            border-radius: 6px;
            padding: 1.25rem;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(5px);
        }
        .metric-title {
            color: #FF5000;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1rem;
            text-align: center;
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
        .stMetric {
            background: rgba(30, 30, 30, 0.3) !important;
            border: 1px solid rgba(255, 80, 0, 0.1) !important;
            border-radius: 6px !important;
            padding: 1rem !important;
        }
        </style>
    """
}

@st.cache_resource
def carregar_modelo(nome_modelo):
    try:
        with open(f'modelos/{nome_modelo}', 'rb') as f:
            modelo = pickle.load(f)
        return modelo
    except Exception as e:
        st.error(f'Erro ao carregar o modelo: {str(e)}')
        return None


def criar_dados_entrada(
    dia_semana, br, fase_dia, condicao_metereologica, pessoas, veiculos
):
    # Ordem exata das colunas baseada no modelo treinado
    colunas = [
        'pessoas',
        'veiculos',
        'dia_semana_quarta-feira',
        'dia_semana_quinta-feira',
        'dia_semana_segunda-feira',
        'dia_semana_sexta-feira',
        'dia_semana_sábado',
        'dia_semana_terça-feira',
        'br_101',
        'br_104',
        'br_110',
        'br_116',
        'br_230',
        'br_361',
        'br_405',
        'br_412',
        'br_426',
        'br_427',
        'br_434',
        'fase_dia_Anoitecer',
        'fase_dia_Plena Noite',
        'fase_dia_Pleno dia',
        'condicao_metereologica_Céu Claro',
        'condicao_metereologica_Garoa/Chuvisco',
        'condicao_metereologica_Ignorado',
        'condicao_metereologica_Nevoeiro/Neblina',
        'condicao_metereologica_Nublado',
        'condicao_metereologica_Sol',
        'condicao_metereologica_Vento',
    ]

    df = pd.DataFrame(0, index=[0], columns=colunas)

    df['pessoas'] = pessoas
    df['veiculos'] = veiculos
    df[f'dia_semana_{dia_semana}'] = 1
    df[f'br_{br}'] = 1
    df[f'fase_dia_{fase_dia}'] = 1
    df[f'condicao_metereologica_{condicao_metereologica}'] = 1

    # Retirar colunas que foram omitidas no modelo
    # (drop_first=True, Exemplo: dia_semana_domingo)
    df = df[colunas]

    return df


def exibir():
    st.markdown(STYLES['main'], unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="title-container">
            <div class="title">Simulador de Risco de Acidente</div>
            <p style='color: #808495; font-size: 1.1rem; letter-spacing: 0.5px;'>
                Simule o risco de acidente com vítimas com base em diferentes fatores
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Informações do Acidente')

            modelo_selecionado = st.selectbox(
                'Modelo',
                ['Forest', 'KNN', 'Logit'],
                key='modelo_select',
            )

            br = st.selectbox(
                'BR',
                [
                    '101',
                    '104',
                    '110',
                    '116',
                    '230',
                    '361',
                    '405',
                    '412',
                    '426',
                    '427',
                    '434',
                ],
                key='br_select',
            )

            dia_semana = st.selectbox(
                'Dia da Semana',
                [
                    'domingo',
                    'segunda-feira',
                    'terça-feira',
                    'quarta-feira',
                    'quinta-feira',
                    'sexta-feira',
                    'sábado',
                ],
                key='dia_select',
            )

            fase_dia = st.selectbox(
                'Fase do Dia',
                ['Pleno dia', 'Anoitecer', 'Plena Noite', 'Amanhecer'],
                key='fase_select',
            )

            condicao_metereologica = st.selectbox(
                'Condição Meteorológica',
                [
                    'Céu Claro',
                    'Nublado',
                    'Sol',
                    'Nevoeiro/Neblina',
                    'Garoa/Chuvisco',
                    'Vento',
                    'Ignorado',
                    'Chuva',
                ],
                key='condicao_select',
            )

        with col2:
            st.subheader('Quantidades')
            pessoas = st.slider(
                'Número de Pessoas',
                min_value=1,
                max_value=50,
                value=1,
                key='pessoas_slider',
            )

            veiculos = st.slider(
                'Número de Veículos',
                min_value=1,
                max_value=22,
                value=1,
                key='veiculos_slider',
            )

            dados_entrada = criar_dados_entrada(
                dia_semana,
                br,
                fase_dia,
                condicao_metereologica,
                pessoas,
                veiculos,
            )

            try:
                modelo = carregar_modelo(f'modelo_{modelo_selecionado}.pkl')
                if modelo is None:
                    raise Exception(
                        'Erro ao carregar o modelo, verifique se o arquivo do modelo está presente no diretório modelos.'
                    )

                probabilidades = modelo.predict_proba(dados_entrada)

                with st.popover(
                    'Resultado da Previsão', use_container_width=True
                ):
                    st.subheader('Modelo Utilizado')
                    modelo_info = {
                        'Forest': 'Random Forest - Modelo baseado em árvores de decisão que combina múltiplas árvores para melhor precisão',
                        'KNN': 'K-Nearest Neighbors - Modelo que classifica baseado nos k exemplos mais próximos',
                        'Logit': 'Regressão Logística - Modelo linear para classificação binária',
                    }
                    st.info(modelo_info[modelo_selecionado])

                    st.subheader('Probabilidades')

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            'Probabilidade de Ter Vítimas',
                            f'{probabilidades[0][1]*100:.2f}%',
                        )

                    with col2:
                        st.metric(
                            'Probabilidade de Não Ter Vítimas',
                            f'{probabilidades[0][0]*100:.2f}%',
                        )

                    st.subheader('Interpretação')
                    if probabilidades[0][1] > 0.7:
                        st.error('Alto risco de acidente com vítimas')
                    elif probabilidades[0][1] > 0.4:
                        st.warning('Risco moderado de acidente com vítimas')
                    else:
                        st.success('Baixo risco de acidente com vítimas')

                    st.subheader('Informações Adicionais')
                    st.info(
                        'Este simulador utiliza dados históricos para fazer previsões. Consulte sempre as autoridades de trânsito para informações oficiais.'
                    )

            except Exception as e:
                st.error(f'Erro ao fazer previsão: {str(e)}')
                st.info(
                    'Verifique se todos os campos foram preenchidos corretamente.'
                )

            footer()
