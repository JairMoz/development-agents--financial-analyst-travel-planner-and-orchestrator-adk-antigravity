from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.models.lite_llm import LiteLlm

AGENT_MODEL = LiteLlm(model="gemini/gemini-2.5-flash")


FINANCIAL_ANALYST_AGENT = Agent(
    name="financial_analyst_agent",
    model=AGENT_MODEL,
    description="Un agente especializado en analizar mercados, reportes corporativos y métricas financieras.",
    instruction="""Eres un analista financiero experto. 
    Tu trabajo es evaluar datos económicos, explicar conceptos complejos de inversión de forma clara, 
    analizar balances generales y evaluar tendencias del mercado. 
    Asegúrate de estructurar tus respuestas de forma profesional. 
    Nota: Siempre incluye un descargo de responsabilidad indicando que no proporcionas asesoría financiera formal."""
)

TRAVEL_PLANNER_AGENT = Agent(
    name="travel_planner_agent",
    model=AGENT_MODEL,
    description="Un experto en crear itinerarios de viaje detallados y optimizados.",
    instruction="Eres un asistente de planificación de viajes. Tu trabajo es crear itinerarios.",
)

ROOT_AGENT = Agent(
    name="root_agent",
    model=AGENT_MODEL,
    description="Agente principal que coordina las peticiones del usuario.",
    instruction="""Eres el orquestador principal. 
    Tu función es analizar la petición del usuario y delegar la tarea al agente especializado correspondiente.
    Si el usuario quiere planear un viaje, usa al travel_planner_agent.""",
    sub_agents=[TRAVEL_PLANNER_AGENT, FINANCIAL_ANALYST_AGENT]
)

root_agent = ROOT_AGENT