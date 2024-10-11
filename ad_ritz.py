import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Título
st.title("Avaliação de Desempenho")

# Legenda
st.subheader("Legenda das Notas:")
st.text("""
1 - Mostrou melhora no trabalho em equipe
2 - Apresenta ética e comprometimento nas atividades
3 - Comunicação e relações sociais melhoradas
4 - Apresentou bom relacionamento interpessoal
5 - Mostra boa disciplina e tendência a cumprir regras determinadas
""")

# Campo para o nome
nome = st.text_input("Nome completo:")

# Critérios comportamentais
st.header("Critérios Comportamentais")
trabalho_em_equipe = st.radio("Trabalho em Equipe", [1, 2, 3, 4, 5])
etica = st.radio("Ética", [1, 2, 3, 4, 5])
comunicacao = st.radio("Comunicação", [1, 2, 3, 4, 5])
relacionamento = st.radio("Relacionamento Interpessoal", [1, 2, 3, 4, 5])
disciplina = st.radio("Disciplina", [1, 2, 3, 4, 5])

# Critérios técnicos
st.header("Critérios Técnicos")
habilidade = st.radio("Habilidade", [1, 2, 3, 4, 5])
produtividade = st.radio("Produtividade", [1, 2, 3, 4, 5])
criatividade = st.radio("Criatividade", [1, 2, 3, 4, 5])
organizacao = st.radio("Organização", [1, 2, 3, 4, 5])
conhecimento = st.radio("Conhecimento Específico", [1, 2, 3, 4, 5])

# Dados para o gráfico de radar
categorias_comportamentais = ['Trabalho em Equipe', 'Ética', 'Comunicação', 'Relacionamento Interpessoal', 'Disciplina']
categorias_tecnicas = ['Habilidade', 'Produtividade', 'Criatividade', 'Organização', 'Conhecimento Específico']

valores_comportamentais = [trabalho_em_equipe, etica, comunicacao, relacionamento, disciplina]
valores_tecnicos = [habilidade, produtividade, criatividade, organizacao, conhecimento]

# Função para criar gráfico de radar
def radar_chart(categorias, valores, title, color):
    N = len(categorias)
    valores += valores[:1]  # Loop no gráfico
    angulos = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angulos += angulos[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angulos, valores, color=color, alpha=0.25)
    ax.plot(angulos, valores, color=color, linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(categorias)
    ax.set_title(title, size=20, color=color, y=1.1)
    
    return fig

# Exibir gráfico ao enviar
if st.button("Gerar Avaliação"):
    st.write(f"Avaliação de: {nome}")
    
    # Gráfico comportamental
    fig_comportamental = radar_chart(categorias_comportamentais, valores_comportamentais, "Mapa Comportamental", 'blue')
    st.pyplot(fig_comportamental)
    
    # Gráfico técnico
    fig_tecnico = radar_chart(categorias_tecnicas, valores_tecnicos, "Mapa Técnico", 'orange')
    st.pyplot(fig_tecnico)
