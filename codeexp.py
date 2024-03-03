import os
from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
from langchain.agents import load_tools
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.tools import DuckDuckGoSearchRun


search = DuckDuckGoSearchRun()

# Load the tools for the agents
ollama_llm = Ollama(model="mistral:7b-instruct")

# Loading Human Tools
human_tools = load_tools(["human"])



# Create new agents
syntax_checker = Agent(
    role='Syntax Checker',
    goal='Check the syntax of given code snippets which is present in code.txt',
    backstory="""You are a Syntax Checker, specialized in verifying
    the syntax of code snippets. Your goal is to ensure that code follows
    correct syntax rules.""",
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

language_expert = Agent(
    role='Language Expert',
    goal='Provide insights on programming language concepts',
    backstory="""You are a Language Expert, knowledgeable in various
    programming languages. Your expertise is valuable in explaining language-specific
    features and concepts in code.""",
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

with open('crewai/code.txt', 'r') as file:
    code_snippet = file.read()

# Create tasks for the new agents
# task1 = Task(
#     description="Check the syntax of the given code snippet on 'code.txt'",
#     agent=syntax_checker,
   
# )


with open("crewai/code.txt", "r") as file:
    code_content = file.read()

task1 = Task(
    description=f"Analyze the code in this file:\n{code_content}",
    agent=syntax_checker,
)

task2 = Task(
    description="Provide insights on programming language concepts in the given code snippet",
    agent=language_expert,
   
)

# Create a crew with the new agents and tasks
crew = Crew(
    agents=[syntax_checker, language_expert],
    tasks=[task1, task2],
    verbose=2,  # You can set it to 1 or 2 for different logging levels
)


# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
