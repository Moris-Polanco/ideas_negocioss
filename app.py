import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_business_idea(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

st.title("Generador de ideas de negocios")

st.markdown("Escribe una breve descripción de tus intereses y te sugeriremos algunas ideas de negocios que podrías explorar.")

prompt = st.text_input("Descripción de tus intereses y del negocio")

if st.button("Generar idea de negocio"):
    business_idea = generate_business_idea(prompt)
    st.success(business_idea)
