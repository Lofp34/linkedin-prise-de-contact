from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os

# Charger les variables d'environnement
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

# Utilisation avec MCPServerAdapter
with MCPServerAdapter(server_params, connect_timeout=60) as mcp_tools:
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")
    
    # Créer l'agent
    agent = Agent(
        role="MCP Tool User",
        goal="Utilize tools from an MCP server pour telecharger le profil linkedin de laurentserre34.",
        backstory="I can connect to hdw MCP server and use their tools.",
        tools=[mcp_tools["get_linkedin_profile"]],
        reasoning=True,
        verbose=True
    )
    
    # Créer la tâche
    task = Task(
        description="Télécharger le profil LinkedIn de laurentserre34 en utilisant l'outil get_linkedin_profile",
        expected_output="Les informations du profil LinkedIn de laurentserre34",
        agent=agent,  # Utiliser le nom de votre variable agent
        output_file="report.md",
        verbose=True

    )
    
    # Créer et exécuter le crew
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )
    
    result = crew.kickoff()