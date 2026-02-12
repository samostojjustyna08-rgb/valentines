import streamlit as st
import time

# Konfiguracja strony
st.set_page_config(page_title="Walentynka", page_icon="❤️")

# --- STYLE CSS (Animacje) ---
st.markdown("""
<style>
    @keyframes falling {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed;
        color: red;
        font-size: 24px;
        user-select: none;
        z-index: 1000;
        animation: falling 3s linear infinite;
    }
    @keyframes flash {
        0%, 100% { background-color: white; }
        50% { background-color: pink; }
    }
    .flash-effect {
        animation: flash 0.5s ease-in-out 3;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIKA APLIKACJI ---

if 'stage' not in st.session_state:
    st.session_state.stage = 'start'

def reset():
    st.session_state.stage = 'start'

# --- EKRAN STARTOWY ---
if st.session_state.stage == 'start':
    st.title("Hej Ty... ❤️")
    st.subheader("Mam do Ciebie bardzo ważne pytanie:")
    st.header("Czy zostaniesz moją walentynką?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("TAK! 😍", use_container_width=True):
            st.session_state.stage = 'yes'
            st.rerun()
            
    with col2:
        if st.button("Nie. 😐", use_container_width=True):
            st.session_state.stage = 'no'
            st.rerun()

# --- EKRAN "NIE" ---
elif st.session_state.stage == 'no':
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZpZzB4bmZ3bm9qZzB4bmZ3bm9qZzB4bmZ3bm9qZzB4bmZ3bm9qJnB0PWV2ZW50Jm49Z3VpZGVfcmVwbGFjZW1lbnQv/", width=400)
    # Używamy Giphy z wściekłym kotkiem
    st.error("Pojebało cię?")
    
    if st.button("Spróbuj jeszcze raz 🔄"):
        reset()
        st.rerun()

# --- EKRAN "TAK" ---
elif st.session_state.stage == 'yes':
    # Efekt błysku (klasa CSS)
    st.markdown('<div class="flash-effect"></div>', unsafe_allow_html=True)
    
    # Spadające serduszka (generowanie wielu divów)
    hearts_html = "".join([f'<div class="heart" style="left: {i*5}%; animation-delay: {i*0.2}s;">❤️</div>' for i in range(20)])
    st.markdown(hearts_html, unsafe_allow_html=True)
    
    st.balloons() # Dodatkowy efekt od Streamlit
    st.title("Wiedziałem! ❤️❤️❤️")
    st.header("To będą najlepsze Walentynki!")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGRiaW80Z3R4bmZ3bm9qZzB4bmZ3bm9qZzB4bmZ3bm9qZzB4bmZ3bm9qJnB0PWV2ZW50Jm49Z3VpZGVfcmVwbGFjZW1lbnQv/v4IsP6K18b-")

    if st.button("Zacznij od nowa"):
        reset()
        st.rerun()
