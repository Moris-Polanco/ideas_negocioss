import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Crear una interfaz de usuario con streamlit
st.title("Generador de planes de negocios")

# Solicitar al usuario que ingrese su idea de negocio
wish = st.text_input("¿Qué idea tienes? O deja en blanco y espera.")

# Utilizar GPT-3 para generar un plan de negocios para la idea del usuario
model_engine = "text-davinci-003"
prompt = (f"Generar una idea de negocio basada en '{wish}'. Incluir nombre de la idea, una línea corta, persona objetivo del usuario, puntos de dolor del usuario a resolver, principales propuestas de valor, descripción detallada de la idea, canales de ventas y marketing, fuentes de ingresos por ventas, estructuras de costos, actividades clave, recursos clave, socios clave, pasos de validación de la idea, costo estimado del primer año de operación y desafíos comerciales potenciales a considerar. ")

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=2024,
    n=1,
    stop=None,
    temperature=0.7,
)

# Obtén el texto del resultado del plan de negocios
business_plan = completions.choices[0].text

# Crea una tabla en formato markdown con dos columnas
table = "| Columna 1 | Columna 2 |\n| --- | --- |\n"

# Separa el texto en líneas
lines = business_plan.split("\n")

# Recorre cada línea del texto
for line in lines:
  # Dividir la línea en dos partes en base al carácter ":"
  parts = line.split(":", 1)
  # Agregar cada parte a una columna de la tabla
  if len(parts) == 2:
    table += f"| {parts[0]} | {parts[1]} |\n"
  else:
    table += f"| {parts[0]} | |\n"

# Muestra la tabla en la aplicación
st.markdown(table)
