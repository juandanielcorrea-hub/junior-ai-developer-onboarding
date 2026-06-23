import os
from langchain.agents import create_agent

# 1. Pegar tu API Key aquí ANTES de inicializar el agente
os.environ["GOOGLE_API_KEY"] = "<YOUR_GOOGLE_API_KEY>"

# (Opcional: Si la de arriba falla por la versión de LangChain, usa esta en su lugar)
# os.environ["GEMINI_API_KEY"] = "TU_LLAVE_SECRET_DE_GEMINI"

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# 2. El agente se crea normal. Al detectar que es "google_genai", 
# LangChain tomará la llave que definiste arriba automáticamente.
agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco"}]}
)

print(result["messages"][-1].content_blocks)


