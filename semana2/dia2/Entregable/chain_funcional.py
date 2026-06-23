import os
from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# ==========================================
# 0. CONFIGURACIÓN DE CREDENCIALES
# ==========================================

os.environ["GOOGLE_API_KEY"] = "<YOUR_GOOGLE_API_KEY>"

# ==========================================
# 1. OUTPUT ESTRUCTURADO 
# ==========================================

class ResumenTecnologia(BaseModel):
    nombre: str = Field(description="Nombre de la tecnología o lenguaje de programación")
    anio_creacion: int = Field(description="Año en que fue lanzado oficialmente o creado")
    caracteristicas_clave: List[str] = Field(description="Lista con exactamente 3 características principales")
    caso_uso_ideal: str = Field(description="El mejor escenario o tipo de proyecto para usarlo")

# ==========================================
# 2. COMPONENTES DE LA CADENA
# ==========================================

parser = JsonOutputParser(pydantic_object=ResumenTecnologia)

# Creamos el Prompt Template inyectando dinámicamente las instrucciones del parseador
prompt = ChatPromptTemplate.from_template(
    "Eres un ingeniero de software experto. Analiza la siguiente tecnología: {tecnologia}.\n\n{instrucciones_formato}",
    partial_variables={"instrucciones_formato": parser.get_format_instructions()}
)

# Inicializamos el LLM con la versión exacta que soporta la API
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.1)

# ==========================================
# 3. CONSTRUCCIÓN DE LA CHAIN (Sintaxis LCEL)
# ==========================================

chain = prompt | llm | parser

# ==========================================
# 4. EJECUCIÓN (Prueba de concepto)
# ==========================================

if __name__ == "__main__":
    # Definimos nuestro Input
    variable_entrada = {"tecnologia": "Python"}
    
    print(f"🚀 Ejecutando la cadena para el input: {variable_entrada['tecnologia']}...\n")
    
    try:
        # Invocamos la cadena completa
        resultado_final = chain.invoke(variable_entrada)
        
        # Imprimimos los resultados obtenidos
        print("✅ ¡Cadena ejecutada con éxito!\n")
        print("📊 Datos Estructurados Recibidos:")
        print(f"Tipo de objeto: {type(resultado_final)}")  # Comprobamos que es un dict de Python
        print(resultado_final)
        
        print("\nAccediendo a campos individuales:")
        print(f" - Nombre: {resultado_final['nombre']}")
        print(f" - Año: {resultado_final['anio_creacion']}")
        print(f" - Caso de uso: {resultado_final['caso_uso_ideal']}")
        
    except Exception as e:
        print(f"❌ Ocurrió un error al ejecutar la cadena: {e}")