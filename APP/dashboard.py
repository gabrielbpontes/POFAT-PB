import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def exibir():
    st.markdown("""
    <style>
    /* Remove todas as barras indesejadas */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
    
    /* Remove a barra de ferramentas dos gráficos */
    .modebar-container {
        display: none !important;
    }
    .modebar {
        height: 0 !important;
    }
    
    /* Remove a linha divisória específica */
    .st-emotion-cache-1v0mbdj, .st-emotion-cache-1dp5vir {
        display: none !important;
    }
    
    /* Remove espaçamento entre colunas */
    .st-emotion-cache-1q7spjk {
        width: calc(50% - 0.5rem) !important;
    }
    
    /* Ajuste final para garantir a remoção */
    .st-emotion-cache-1wrcr25 {
        gap: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h1 style="color: #FF5000; border-bottom: 1px solid #FF5000; padding-bottom: 0.5rem;">
            📊 Dashboard Analítico
        </h1>
        <p style="color: #808495;">
            Visualização interativa dos dados de acidentes na Paraíba
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:
        df = pd.read_csv("data/acidentes_pb.csv")
        df = df.rename(columns={
            'dia_semana': 'dia_semana',
            'br': 'br',
            'fase_dia': 'fase_dia',
            'condicao_metereologica': 'condicao_metereologica',
            'classificacao_acidente': 'classificacao_acidente'
        })
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        st.stop()

    with st.container():
        st.markdown('<div class="filter-container">', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            br_options = sorted(df['br'].unique())
            selected_br = st.multiselect(
                'Selecione a(s) BR(s):',
                options=br_options,
                default=br_options[:3],
                format_func=lambda x: f'BR-{x}'
            )
        
        with col2:
            fase_options = df['fase_dia'].unique()
            selected_fase = st.multiselect(
                'Fase do dia:',
                options=fase_options,
                default=fase_options
            )
        
        with col3:
            tipo_options = df['classificacao_acidente'].unique()
            selected_tipo = st.multiselect(
                'Tipo de acidente:',
                options=tipo_options,
                default=tipo_options
            )
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Filtros
    filtered_df = df[
        (df['br'].isin(selected_br)) &
        (df['fase_dia'].isin(selected_fase)) &
        (df['classificacao_acidente'].isin(selected_tipo))
    ]

    # Estatísticas Descritivas
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h3 style="color: #FF5000; font-size: 20px; border-bottom: 1px solid #FF5000; padding-bottom: 0.5rem; text-align: center;">
            📋 Estatísticas Descritivas
        </h3>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="stats-container">', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total de Registros", len(filtered_df))
            st.write(f"**Média diária:** {len(filtered_df)/30:.1f} acidentes")
            
        with col2:
            br_mais_acidentes = filtered_df['br'].value_counts().idxmax()
            st.metric("BR com mais acidentes", f"BR-{br_mais_acidentes}")
            st.write(f"**Total:** {filtered_df['br'].value_counts().max()} ocorrências")
            
        with col3:
            dia_mais_acidentes = filtered_df['dia_semana'].value_counts().idxmax()
            st.metric("Dia com mais acidentes", dia_mais_acidentes)
            st.write(f"**Total:** {filtered_df['dia_semana'].value_counts().max()} ocorrências")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Métricas
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h2 style="color: #FF5000; font-size: 20px; border-bottom: 1px solid #FF5000; padding-bottom: 0.5rem; text-align: center;">
            📈 Métricas Principais
        </h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Acidentes", len(filtered_df))
    with col2:
        st.metric("Com Vítimas Feridas", 
                 len(filtered_df[filtered_df['classificacao_acidente'].str.contains("Feridas")]))
    with col3:
        st.metric("Com Vítimas Fatais", 
                 len(filtered_df[filtered_df['classificacao_acidente'].str.contains("Fatais")]))

    # Gráficos
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico 1: Heatmap - Dia da Semana x Fase do Dia
        st.markdown("""
        <div style="margin: 1rem 0;">
            <h2 style="color: #FF5000; font-size: 1.2rem;">
                🔥 Distribuição por Dia e Turno
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        heatmap_data = filtered_df.groupby(['dia_semana', 'fase_dia']).size().unstack().fillna(0)
        dias_ordenados = ['segunda-feira', 'terça-feira', 'quarta-feira', 
                         'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        heatmap_data = heatmap_data.reindex(dias_ordenados)
        
        fig1 = px.imshow(
            heatmap_data,
            labels=dict(x=" ", y=" ", color="Acidentes"),
            color_continuous_scale='OrRd',
            aspect="auto"
        )
        fig1.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Gráfico 2: Distribuição por Rodovia (Versão Corrigida)
        st.markdown("""
        <div style="margin: 1rem 0;">
            <h2 style="color: #FF5000; font-size: 1.2rem;">
                🛣️ Acidentes por Rodovia (BR)
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        br_counts = filtered_df['br'].value_counts().reset_index()
        br_counts.columns = ['BR', 'Acidentes']
        br_counts['BR'] = 'BR-' + br_counts['BR'].astype(str)
        
        fig2 = px.bar(
            br_counts,
            x='BR',
            y='Acidentes',
            color='Acidentes',
            color_continuous_scale='OrRd',
            labels={'Acidentes': 'Número de Acidentes'},
            text='Acidentes'
        )
        fig2.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis_title=' ',
            yaxis_title='Nº de Acidentes',
            coloraxis_showscale=False,
            xaxis=dict(tickangle=-45),
            height=400
        )
        fig2.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            marker_line_color='rgba(255,80,0,0.8)',
            marker_line_width=1
        )
        max_value = br_counts['Acidentes'].max()
        fig2.update_yaxes(range=[0, max_value * 1.15])
        st.plotly_chart(fig2, use_container_width=True)

    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico 3: Condições Meteorológicas 
        st.markdown("""
        <div style="margin: 1rem 0;">
            <h2 style="color: #FF5000; font-size: 1.2rem;">
                ⛅ Condições Meteorológicas
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        condicao_counts = filtered_df['condicao_metereologica'].value_counts(normalize=True).reset_index()
        condicao_counts.columns = ['Condicao', 'Percentual']
        condicao_counts['Percentual'] = condicao_counts['Percentual'] * 100
        
        ordem_condicoes = ['Sol', 'Céu Claro', 'Chuva', 'Garoa/Chuvisco', 
                          'Nevoeiro/Neblina', 'Vento', 'Ignorado']
        condicao_counts['Condicao'] = pd.Categorical(condicao_counts['Condicao'], 
                                                   categories=ordem_condicoes, 
                                                   ordered=True)
        condicao_counts = condicao_counts.sort_values('Condicao')
        
        fig3 = px.pie(
            condicao_counts,
            names='Condicao',
            values='Percentual',
            hole=0.35,
            color_discrete_sequence=px.colors.sequential.OrRd,
            labels={'Percentual': 'Percentual (%)'},
            custom_data=['Percentual']
        )
        fig3.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title=None
            ),
            height=450
        )
        fig3.update_traces(
            hovertemplate="<b>%{label}</b><br>%{customdata[0]:.1f}%",
            textinfo='percent',
            texttemplate='%{percent:.1%}',
            textposition='inside',
            insidetextorientation='radial',
            marker=dict(line=dict(color='rgba(0,0,0,0.5)', width=0.5))
        )
        fig3.add_annotation(
            text=f"Total: {len(filtered_df)} acidentes",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=12, color='white')
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        # Gráfico 4: Gravidade dos Acidentes
        st.markdown("""
        <div style="margin: 1rem 0;">
            <h2 style="color: #FF5000; font-size: 1.2rem;">
                🚨 Gravidade dos Acidentes
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        classificacao_counts = filtered_df['classificacao_acidente'].value_counts().reset_index()
        classificacao_counts.columns = ['Classificacao', 'Acidentes']
        
        fig4 = px.bar(
            classificacao_counts,
            x='Classificacao',
            y='Acidentes',
            color='Acidentes',
            color_continuous_scale='OrRd',
            text='Acidentes'
        )
        fig4.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis_title=' ',
            yaxis_title='Nº de Acidentes',
            coloraxis_showscale=False,
            height=400
        )
        fig4.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            marker_line_color='rgba(255,80,0,0.8)',
            marker_line_width=1
        )
        st.plotly_chart(fig4, use_container_width=True)

    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico 5: Acidentes por Período do Dia
        st.markdown("""
        <div style="margin: 1rem 0;">
            <h2 style="color: #FF5000; font-size: 1.2rem;">
                🌇 Acidentes por Período do Dia
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        fase_counts = filtered_df['fase_dia'].value_counts().reset_index()
        fase_counts.columns = ['Fase', 'Acidentes']
        
        fig5 = px.pie(
            fase_counts,
            names='Fase',
            values='Acidentes',
            hole=0.3,
            color_discrete_sequence=px.colors.sequential.OrRd
        )
        fig5.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=400,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5
            )
        )
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        # Gráfico 6: Distribuição por Dia da Semana
        if 'data' in df.columns:
            st.markdown("""
            <div style="margin: 1rem 0;">
                <h2 style="color: #FF5000; font-size: 1.2rem;">
                    📅 Evolução Temporal
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            try:
                df['data'] = pd.to_datetime(df['data'])
                time_series = filtered_df.resample('M', on='data').size()
                
                fig6 = px.line(
                    time_series.reset_index(),
                    x='data',
                    y=0,
                    markers=True,
                    color_discrete_sequence=['#FF5000'],
                    labels={'0': 'Número de Acidentes', 'data': 'Data'}
                )
                fig6.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white'),
                    height=400
                )
                st.plotly_chart(fig6, use_container_width=True)
            except:
                st.warning("Não foi possível gerar a série temporal.")
        else:
            st.markdown("""
            <div style="margin: 1rem 0;">
                <h2 style="color: #FF5000; font-size: 1.2rem;">
                    📊 Distribuição por Dia da Semana
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            dia_counts = filtered_df['dia_semana'].value_counts().reset_index()
            dia_counts.columns = ['Dia', 'Acidentes']
            dias_ordenados = ['segunda-feira', 'terça-feira', 'quarta-feira', 
                             'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
            dia_counts['Dia'] = pd.Categorical(dia_counts['Dia'], 
                                             categories=dias_ordenados, 
                                             ordered=True)
            dia_counts = dia_counts.sort_values('Dia')
            
            fig6 = px.bar(
                dia_counts,
                x='Dia',
                y='Acidentes',
                color='Acidentes',
                color_continuous_scale='OrRd',
                text='Acidentes'
            )
            fig6.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                xaxis_title=' ',
                yaxis_title='Nº de Acidentes',
                coloraxis_showscale=False,
                height=400
            )
            fig6.update_traces(
                texttemplate='%{text:,}',
                textposition='outside',
                marker_line_color='rgba(255,80,0,0.8)',
                marker_line_width=1
            )
            st.plotly_chart(fig6, use_container_width=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #808495; font-size: 0.8rem; margin-top: 2rem;">
        Dados atualizados em: {}
    </div>
    """.format(pd.Timestamp.now().strftime('%d/%m/%Y %H:%M')), unsafe_allow_html=True)