import pandas as pd
import plotly.express as px
import streamlit as st
from utils import footer

CORES = {
    'principal': '#FF5000',
    'secundaria': '#FF7B33',
    'terciaria': '#FFA366',
    'fundo': '#1A1D24',
    'texto': '#E0E0E0',
    'texto_secundario': '#808495',
}

PALETA_GRAFICOS = ['#FF5000', '#FF7B33', '#FFA366', '#FFC299']

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

        /* Gráficos */
        .graph-container {
            background: rgba(30, 30, 30, 0.3);
            border: 1px solid rgba(255, 80, 0, 0.1);
            border-radius: 6px;
            padding: 1.25rem;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(5px);
        }
        .graph-title {
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
        </style>
    """
}


def exibir():
    st.markdown(STYLES['main'], unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="title-container">
            <div class="title">Dashboard Analítico</div>
            <p style='color: #808495; font-size: 1.1rem; letter-spacing: 0.5px;'>
                Visualização interativa dos dados de acidentes na Paraíba
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    try:
        df = pd.read_csv('data/acidentes_pb.csv')
        df = df.rename(
            columns={
                'dia_semana': 'dia_semana',
                'br': 'br',
                'fase_dia': 'fase_dia',
                'condicao_metereologica': 'condicao_metereologica',
                'classificacao_acidente': 'classificacao_acidente',
            }
        )

        df = df.fillna(
            {
                'condicao_metereologica': 'Não Informado',
                'classificacao_acidente': 'Não Informado',
                'fase_dia': 'Não Informado',
            }
        )
    except Exception as e:
        st.error(f'Erro ao carregar dados: {str(e)}')
        st.stop()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        br_options = sorted(df['br'].unique())[1:]
        selected_br = st.multiselect(
            'Selecione a(s) BR(s):',
            options=br_options,
            default=br_options[1:4:],
            format_func=lambda x: f'BR-{x}',
        )
    with col2:
        fase_options = df['fase_dia'].unique()
        selected_fase = st.multiselect(
            'Fase do dia:', options=fase_options, default=fase_options
        )
    with col3:
        tipo_options = df['classificacao_acidente'].unique()
        selected_tipo = st.multiselect(
            'Tipo de acidente:', options=tipo_options, default=tipo_options
        )
    st.markdown('</div>', unsafe_allow_html=True)

    filtered_df = df[
        (df['br'].isin(selected_br))
        & (df['fase_dia'].isin(selected_fase))
        & (df['classificacao_acidente'].isin(selected_tipo))
    ]

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="metric-title">Estatísticas Descritivas</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Total de Registros', len(filtered_df))
        st.write(f'**Média diária:** {len(filtered_df)/30:.1f} acidentes')
    with col2:
        br_mais_acidentes = filtered_df['br'].value_counts().idxmax()
        st.metric('BR com mais acidentes', f'BR-{br_mais_acidentes}')
        st.write(
            f"**Total:** {filtered_df['br'].value_counts().max()} ocorrências"
        )
    with col3:
        dia_mais_acidentes = filtered_df['dia_semana'].value_counts().idxmax()
        st.metric('Dia com mais acidentes', dia_mais_acidentes)
        st.write(
            f"**Total:** {filtered_df['dia_semana'].value_counts().max()} ocorrências"
        )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="graph-title">Distribuição por Dia e Turno</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        heatmap_data = (
            filtered_df.groupby(['dia_semana', 'fase_dia'])
            .size()
            .unstack()
            .fillna(0)
        )
        dias_ordenados = [
            'segunda-feira',
            'terça-feira',
            'quarta-feira',
            'quinta-feira',
            'sexta-feira',
            'sábado',
            'domingo',
        ]
        heatmap_data = heatmap_data.reindex(dias_ordenados)

        fig1 = px.imshow(
            heatmap_data,
            labels=dict(x='', y='', color=''),
            color_continuous_scale=PALETA_GRAFICOS,
            aspect='auto',
            text_auto=True,
        )
        fig1.update_layout(
            plot_bgcolor=CORES['fundo'],
            paper_bgcolor=CORES['fundo'],
            font=dict(color=CORES['texto']),
            height=450,
            width=450,
            margin=dict(l=0, r=0, t=30, b=0),
            coloraxis_showscale=False,
            xaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        br_counts = filtered_df['br'].value_counts().reset_index()
        br_counts.columns = ['BR', 'Acidentes']
        br_counts['BR'] = 'BR-' + br_counts['BR'].astype(str)

        fig2 = px.bar(
            br_counts,
            x='BR',
            y='Acidentes',
            color='Acidentes',
            color_continuous_scale=PALETA_GRAFICOS,
            text='Acidentes',
        )
        fig2.update_layout(
            plot_bgcolor=CORES['fundo'],
            paper_bgcolor=CORES['fundo'],
            font=dict(color=CORES['texto']),
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False,
            xaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickangle=-45,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            height=450,
            width=450,
        )
        fig2.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            marker_line_color=CORES['principal'],
            marker_line_width=1,
        )
        st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="graph-title">Análise de Condições e Gravidade</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        condicao_counts = (
            filtered_df['condicao_metereologica'].value_counts().reset_index()
        )
        condicao_counts.columns = ['Condicao', 'Acidentes']

        fig3 = px.bar(
            condicao_counts,
            y='Condicao',
            x='Acidentes',
            color='Acidentes',
            color_continuous_scale=PALETA_GRAFICOS,
            text='Acidentes',
            orientation='h',
        )
        fig3.update_layout(
            plot_bgcolor=CORES['fundo'],
            paper_bgcolor=CORES['fundo'],
            font=dict(color=CORES['texto']),
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False,
            xaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            height=450,
            width=450,
        )
        fig3.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            marker_line_color=CORES['principal'],
            marker_line_width=1,
        )
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        classificacao_counts = (
            filtered_df['classificacao_acidente'].value_counts().reset_index()
        )
        classificacao_counts.columns = ['Classificacao', 'Acidentes']

        fig4 = px.bar(
            classificacao_counts,
            x='Classificacao',
            y='Acidentes',
            color='Acidentes',
            color_continuous_scale=PALETA_GRAFICOS,
            text='Acidentes',
        )
        fig4.update_layout(
            plot_bgcolor=CORES['fundo'],
            paper_bgcolor=CORES['fundo'],
            font=dict(color=CORES['texto']),
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False,
            xaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickangle=-45,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            height=450,
            width=450,
        )
        fig4.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            marker_line_color=CORES['principal'],
            marker_line_width=1,
        )
        st.plotly_chart(fig4, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="graph-title">Análise Temporal</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        fase_counts = filtered_df['fase_dia'].value_counts().reset_index()
        fase_counts.columns = ['Fase', 'Acidentes']

        fig5 = px.bar(
            fase_counts,
            y='Fase',
            x='Acidentes',
            color='Acidentes',
            color_continuous_scale=PALETA_GRAFICOS,
            text='Acidentes',
            orientation='h',
        )
        fig5.update_layout(
            plot_bgcolor=CORES['fundo'],
            paper_bgcolor=CORES['fundo'],
            font=dict(color=CORES['texto']),
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False,
            xaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            height=450,
            width=450,
        )
        fig5.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            marker_line_color=CORES['principal'],
            marker_line_width=1,
        )
        st.plotly_chart(fig5, use_container_width=True)

    with col2:
        dia_counts = filtered_df['dia_semana'].value_counts().reset_index()
        dia_counts.columns = ['Dia', 'Acidentes']
        dias_ordenados = [
            'segunda-feira',
            'terça-feira',
            'quarta-feira',
            'quinta-feira',
            'sexta-feira',
            'sábado',
            'domingo',
        ]
        dia_counts['Dia'] = pd.Categorical(
            dia_counts['Dia'], categories=dias_ordenados, ordered=True
        )
        dia_counts = dia_counts.sort_values('Dia')

        fig6 = px.bar(
            dia_counts,
            x='Dia',
            y='Acidentes',
            color='Acidentes',
            color_continuous_scale=PALETA_GRAFICOS,
            text='Acidentes',
        )
        fig6.update_layout(
            plot_bgcolor=CORES['fundo'],
            paper_bgcolor=CORES['fundo'],
            font=dict(color=CORES['texto']),
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False,
            xaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickangle=-45,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=True,
                tickfont=dict(size=10, color=CORES['texto']),
            ),
            height=450,
            width=450,
        )
        fig6.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            marker_line_color=CORES['principal'],
            marker_line_width=1,
        )
        st.plotly_chart(fig6, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    footer()

    st.markdown('</div>', unsafe_allow_html=True)
