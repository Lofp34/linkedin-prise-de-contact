from crewai import Agent
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters  # For Stdio Server
import os

# Charger les variables depuis ton .env (si tu utilises python-dotenv, sinon os.environ suffit si ton venv a les variables)
HDW_ACCESS_TOKEN = os.environ.get("HDW_ACCESS_TOKEN")
HDW_ACCOUNT_ID = os.environ.get("HDW_ACCOUNT_ID")

# Définir les paramètres du serveur
server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@horizondatawave/mcp"],
    env={
        "HDW_ACCESS_TOKEN": HDW_ACCESS_TOKEN,
        "HDW_ACCOUNT_ID": HDW_ACCOUNT_ID,
    },
)

# Exemple d'utilisation
with MCPServerAdapter(server_params, connect_timeout=60) as mcp_tools:
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")


agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from an MCP server pour telecharger le profil linkedin de laurentserre34 .",
        backstory="I can connect to hdw MCP server and use their tools.",
        tools=[mcp_tools["get_linkedin_profile"]], # Pass the loaded tools to your agent
        reasoning=True,
        verbose=True
    )

task = Task(
    description="Télécharger et analyser le profil LinkedIn de laurentserre34 en utilisant les outils MCP disponibles",
    expected_output="Un rapport détaillé du profil LinkedIn avec les informations principales",
    agent=agent  # Ici vous utilisez le nom de votre variable agent
)