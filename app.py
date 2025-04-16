import streamlit as st

st.set_page_config(page_title="Cassol - Configurador de Peças", page_icon='favicon.ico')

with open('assets/styles.css', 'r') as f:
    css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.image("assets/logo.png", width=192)

opcoes_dd1 = {
    "Nenhum": 0, 
    "0 a 2": 1.5, 
    "3 a 4": 2, 
    "5 a 8": 2.6, 
    "9 a 12": 3.4, 
    "13 a 20": 4.8
}
dd1 = st.selectbox("1. Quantidade de Consolos", list(opcoes_dd1.keys()))

opcoes_dd2 = {
    "Nenhum": 0,
    "1": 0,
    "2": 1.3,
    "3": 1.7
}
dd2 = st.selectbox("2. Quantidade de Chumbadores", list(opcoes_dd2.keys()))

opcoes_dd3 = {
    "Nenhum": 0,
    "1": 0,
    "2": 1.3,
    "3": 1.7
}
dd3 = st.selectbox("3. Quantidade de Pluviais", list(opcoes_dd3.keys()))

opcoes_dd4 = {
    "Nenhum": 0, 
    "1 a 2": 0, 
    "3 a 4": 1.3, 
    "5 a 20": 1.7
}
dd4 = st.selectbox("4. Quantidade de Insertos", list(opcoes_dd4.keys()))

opcoes_dd5 = {
    "Nenhum": 0, 
    "1": 0, 
    "2": 1.3, 
    "3": 1.7
}
dd5 = st.selectbox("5. Quantidade de Canaletas", list(opcoes_dd5.keys()))

opcoes_dd6 = {
    "Nenhum": 0, 
    "1 a 4": 0, 
    "5 a 10": 1.3, 
    "11 ou mais": 1.7
}
dd6 = st.selectbox("6. Quantidade de Luvas", list(opcoes_dd6.keys()))

opcoes_dd7 = {
    "Nenhum": 0, 
    "1": 0, 
    "2": 1.3, 
    "3 ou mais": 1.7
}
dd7 = st.selectbox("7. Quantidade de Aterrinserts", list(opcoes_dd7.keys()))

pontos_peca = (
    opcoes_dd1[dd1] +
    opcoes_dd2[dd2] +
    opcoes_dd3[dd3] +
    opcoes_dd4[dd4] +
    opcoes_dd5[dd5] +
    opcoes_dd6[dd6] +
    opcoes_dd7[dd7]
)

dificuldade=''
tempo=''

if(pontos_peca < 6):
    dificuldade='Fácil'
    tempo='0,5 a 1 Dia'

elif(pontos_peca >= 6 and pontos_peca < 8):
    dificuldade='Médio'
    tempo='1,5 a 2 Dias'

elif(pontos_peca >= 8 and pontos_peca < 12):
    dificuldade='Difícil'
    tempo='2,5 a 3,5 Dias'

elif(pontos_peca >= 12):
    dificuldade='Complexo'
    tempo='4 Dias ou mais'

st.markdown("-")
st.markdown(f"### Pontuação da Peça: {pontos_peca}")
st.markdown(f"### Nível de Complexidade: {dificuldade}")
st.markdown(f"### Tempo de Fabricação: {tempo}")