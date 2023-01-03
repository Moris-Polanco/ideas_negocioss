import openai
import streamlit as st
import weasyprint
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Crear una interfaz de usuario con streamlit
st.title("Generador de ideas de negocios")

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

# Mostrar el resultado en una tabla en formato markdown
business_plan = completions.choices[0].text

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas

# Crea un archivo PDF
c = Canvas("business_plan.pdf", pagesize=letter)

# Dibuja el texto del plan de negocios en el archivo PDF
c.drawString(100, 750, business_plan)

# Guarda el archivo PDF
c.save()

# Muestra el PDF en la aplicación
st.markdown("Se ha creado un archivo PDF con el plan de negocios. Haga clic en el botón a continuación para descargar el archivo.")
st.markdown("[Descargar PDF](business_plan.pdf)")
