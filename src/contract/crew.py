from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ContractReviewTeam:
    """Contract Review Team Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ----------- Agents -----------

    @agent
    def legal_compliance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['legal_compliance_agent'],
            verbose=True
        )

    @agent
    def finance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['finance_agent'],
            verbose=True
        )

    @agent
    def negotiator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['negotiator_agent'],
            verbose=True
        )

    @agent
    def summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summary_agent'],
            verbose=True
        )

    # ----------- Tasks -----------

    @task
    def contract_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['contract_analysis_task']
        )

    @task
    def financial_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_review_task']
        )

    @task
    def negotiation_suggestions_task(self) -> Task:
        return Task(
            config=self.tasks_config['negotiation_suggestions_task']
        )

    @task
    def contract_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['contract_summary_task']
        )

    # ----------- Crew -----------

    @crew
    def crew(self) -> Crew:
        """Creates the Contract Review Team Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
