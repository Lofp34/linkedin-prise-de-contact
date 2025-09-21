from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import MCPServerAdapter
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from mcp import StdioServerParameters
import os

@CrewBase
class hdwcrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    mcp_server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@horizondatawave/mcp"],
        env={
            "HDW_ACCESS_TOKEN": os.environ.get("HDW_ACCESS_TOKEN"),
            "HDW_ACCOUNT_ID": os.environ.get("HDW_ACCOUNT_ID"),
        },
    )

    # Ajoutez votre knowledge source ici
    knowledge_source_1 = TextFileKnowledgeSource(file_paths=["report.md"])
    knowledge_source_2 = TextFileKnowledgeSource(file_paths=["report_laurent.md"])

    @agent
    def my_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['my_agent'],
            tools=self.get_mcp_tools(),
            knowledge_sources_1=[self.knowledge_source_1],  # Ajout de la knowledge source
            verbose=True
        )
    
    @agent
    def my_copywriter(self) -> Agent:
        return Agent(
            config=self.agents_config['my_copywriter'],
            tools=self.get_mcp_tools(),
            knowledge_sources_2=[self.knowledge_source_2],
            verbose=True
        )
    @task
    def my_task(self) -> Task:
        return Task(
            config=self.tasks_config['my_task']
        )

    @task
    def Strategie_task(self) -> Task:
        return Task(
            config=self.tasks_config['Strategie_task']
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )