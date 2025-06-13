
import streamlit as st
import os
import hmac
from functions import generate_chat_prompt, query_bedrock, personalize_recommendations

st.set_page_config(
    page_title="Chatbot Ways",
    page_icon="logo.jpeg",
    layout="wide"
)

def check_password():
    def password_entered():
        if hmac.compare_digest(st.session_state["username"], "admin") and \
           hmac.compare_digest(st.session_state["password"], "admin123"):
            st.session_state["authenticated"] = True
            del st.session_state["password"]
        else:
            st.session_state["authenticated"] = False

    if "authenticated" not in st.session_state:
        st.text_input("Usuário", key="username")
        st.text_input("Senha", type="password", key="password", on_change=password_entered)
        return False
    elif not st.session_state["authenticated"]:
        st.text("Usuário ou senha incorretos.")
        return False
    else:
        return True

if check_password():
    st.title("Chatbot Ways 🤖")
    st.write("Bem-vindo! Este é seu assistente educacional para AWS.")

    user_input = st.text_area("Sua pergunta:", placeholder="Digite sua dúvida sobre AWS...")
    if st.button("Enviar"):
        prompt = generate_chat_prompt(user_input)
        response = query_bedrock(prompt)
        st.write("Resposta da IA:")
        st.write(response)

    if st.checkbox("Mostrar recomendações de trilhas personalizadas?"):
        user_id = st.session_state.get("username", "default_user")
        recommendations = personalize_recommendations(user_id)
        st.write("Trilhas recomendadas:")
        for rec in recommendations:
            st.write(f"- {rec}")
