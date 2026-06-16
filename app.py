import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Viagem ✈️",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Contagem Regressiva da Viagem")
st.write("Destino: 16/07/2026")

# Música opcional. Você pode trocar este link por outro arquivo de áudio.
musica_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

if "play" not in st.session_state:
    st.session_state.play = False

if st.button("🔊 Ativar música"):
    st.session_state.play = True

if st.session_state.play:
    st.audio(musica_url, autoplay=True)

# Data fixa da viagem
data_viagem = datetime(2026, 7, 16, 0, 0, 0)
agora = datetime.now()
diferenca = data_viagem - agora

st.markdown("---")

if diferenca.total_seconds() <= 0:
    st.success("🎉 Hoje é o dia da viagem! ✈️")
else:
    dias = diferenca.days
    horas, resto = divmod(diferenca.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Dias", dias)
    col2.metric("Horas", horas)
    col3.metric("Minutos", minutos)
    col4.metric("Segundos", segundos)

    st.info("Atualize a página para ver a contagem atualizada 🔄")
