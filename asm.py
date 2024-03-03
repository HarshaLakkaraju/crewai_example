# Define AI agents for tasking with the cutting frames task
import os
from crewai import Agent, Task, Crew,Process
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import load_tools
from langchain.tools import tool
from crewai.tasks.task_output import TaskOutput
import google.generativeai as genai 
from langchain.llms import Ollama
from crewai.process import Process


# Define the Gemini API
#pip install google-generativeai langchain-google-genai streamlit for the google.generativeai


# Set gemini pro as llm
ollama_llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose = True,
                             temperature = 0.5,
                             google_api_key="AIzaSyCSoLtDo3bTrxwUKDjq3IfvHRncQiZ7lEI")



# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# from langchain_community.llms import HuggingFaceHub
# repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
# ollama_llm = HuggingFaceHub(
#     repo_id=repo_id, model_kwargs={"temperature": 2, "max_tokens":4096}
# )

# Define the Ollama language model
#ollama_llm = Ollama(model="codellama:13b-python")


# Define the DuckDuckGoSearchRun tool
search_tool = DuckDuckGoSearchRun()
# Loading Human Tools
human_tools = load_tools(["human"])

def callback_function(output: TaskOutput):
    # Do something after the task is completed
    # Example: Send an email to the manager
    print(f"""
        Task completed!
        Task: {output.description}
        Output: {output.result}
    """)
    
# Define the manager agent 
manager_agent = Agent(
    role='Project Manager',
    goal='Oversee the development of a Python script for identifying and cutting stationary frames in CCTV footage',
    backstory="""As the Project Manager,your main role is to check work form every developer rerun if needed , your role is to oversee the development of a Python script that can identify and cut stationary frames in CCTV footage.
    Your goal is to ensure that the project is executed efficiently and that the final script meets the specified requirements and identify requirements for the project and assign the task to the respective developer and tester and syntax tester and machine learning engineer and computer vision specialist and quality assurance analyst and install the code in the system and check the code and re run the code if needed""",
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm,
    tools=[search_tool]
)
 
 # Agent 1: Python Developer
python_dev_agent = Agent(
     role='Python Developer',
     goal='Write efficient and functional Python code for specified tasks',
     backstory="""As a seasoned Python Developer, your journey is defined by crafting solutions with Python.
     With a passion for elegant code, your goal is to bring innovation by implementing cutting-edge scripts
     for various projects. Your code tells stories of creativity and reliability.""",
     verbose=True,
     allow_delegation=False,
     llm=ollama_llm,
     #tools=[search_tool]
  )
 
 # Agent 2: Python Tester
python_tester_agent = Agent(
     role='Python Tester',
     goal='Thoroughly test Python code to identify and report bugs or issues',
     backstory="""With a keen eye for detail and a commitment to perfection, you thrive as a Python Tester.
     Your role is to unravel the intricacies of code, ensuring its robustness and reliability. Your dedication
     to quality assurance plays a pivotal role in delivering flawless software.""",
     verbose=True,
     allow_delegation=False,
     llm=ollama_llm,
    #tools=[search_tool]
 )
 
 # Agent 3: Syntax Tester
syntax_tester_agent = Agent(
     role='Syntax Tester',
     goal='Analyze Python code for adherence to syntax rules and style guidelines',
     backstory="""As the Syntax Tester, you're not just analyzing code; you're sculpting it into an art form.
     Your meticulous approach to syntax and style guidelines ensures that every line of Python code is not just
     functional but a symphony of elegance. Your passion lies in maintaining code integrity and aesthetics,if code is not efficient the code should be sent back to the developer for rework.""",
     verbose=True,
     aallow_delegation=False,
     llm=ollama_llm,
    #tools=[search_tool]
 )

 # Agent 4: Machine Learning Engineer
ml_engineer_agent = Agent(
     role='Machine Learning Engineer',
     goal='Implement advanced algorithms to enhance stationary frame detection in CCTV footage',
     backstory="""As a Machine Learning Engineer, your expertise extends beyond code.
     Your mission is to bring the power of advanced algorithms to enhance the detection of stationary frames
     in CCTV footage. Your contributions will elevate accuracy and redefine the boundaries of video analysis,if code is not efficient the code should be sent back to the developer for rework.""",
     verbose=True,
     allow_delegation=False,
     tools=[search_tool],
     llm=ollama_llm
     
 )
 
 # Agent 5: Computer Vision Specialist
cv_specialist_agent = Agent(
     role='Computer Vision Specialist',
     goal='Leverage computer vision techniques for precise identification of stationary frames in videos',
     backstory="""With a focus on the visual realm, you are the Computer Vision Specialist.
     Your task is to apply cutting-edge computer vision techniques, ensuring precise identification of
     stationary frames in CCTV footage. Your vision transforms pixels into insights.""",
     verbose=True,
     allow_delegation=False,
     tools=[search_tool],
     llm=ollama_llm
     
 )
 
 # Agent 6: Quality Assurance Analyst
qa_analyst_agent = Agent(
     role='Quality Assurance Analyst',
     goal='Conduct rigorous testing to ensure the accuracy and reliability of the stationary frame cutting script',
     backstory="""As the guardian of quality, you are the Quality Assurance Analyst.
     Your role is to conduct relentless testing, ensuring the accuracy and reliability of the stationary frame
     cutting script. Your commitment to perfection is the final checkpoint for flawless video analysis.""",
     verbose=True,
     allow_delegation=False,
     llm=ollama_llm
     
 )

# # Define tasks for each agent
task1 = Task(
    description="for writting  a code to create a Python script  that can identify motion and also store the time interval for cutting stationary frames in CCTV footage will give work to python developer and check every task by python tester and syntax tester and machine learning engineer and computer vision specialist and quality assurance analyst and install the code in the system and check the code and re run the code if needed",  
    agent=manager_agent,
)

task_python_dev = Task(
    description=" using use insight from prompt and write a code to create a Python script that can identify and cut stationary frames in CCTV footage Your mission is to craft a script Elevate efficiency, by using open cv ,focus on dynamic events, and be the architect of a code that stands out in its ingenuity. ",
    agent=python_dev_agent,
)

task_python_tester = Task(
    description="Your role, use insight from prompt and a Python Tester, is to thoroughly test the Python code written by the Python Developer. Identify and report any bugs or issues to ensure the robustness and reliability of the stationary frame cutting script, if code is not efficient the code should be sent back to the developer for rework.",
    agent=python_tester_agent,
)

task_syntax_tester = Task(
    description="As the Syntax Tester,use insight from prompt and  your mission is to analyze the Python code for adherence to syntax rules and style guidelines. Ensure that the code not only functions but also maintains a symphony of elegance in its structure , write in {file_path},again if code is not efficient the code should be sent back to the developer for rework.",
    agent=syntax_tester_agent,
)

task_ml_engineer = Task(
    description="""use insight from prompt and Bring your expertise as a Machine Learning Engineer to implement advanced algorithms that enhance
    the accuracy of stationary frame detection in the Python code. Push the boundaries of video analysis with your contributions,again if code is not efficient the code should be sent back to the developer for rework.""",
    agent=ml_engineer_agent,
)

task_cv_specialist = Task(
    description="""use insight from prompt and As the Computer Vision Specialist, leverage cutting-edge computer vision techniques to ensure
    precise identification of stationary frames in the CCTV footage. Transform pixels into insights with your expertise and install tool in the system and check the code and re run the code if needed""",
    agent=cv_specialist_agent,
)

task_qa_analyst = Task(
    description="""Your role as the Quality Assurance Analyst is critical use insight from prompt and Conduct rigorous testing to ensure the accuracy
    and reliability of the stationary frame cutting script. Your commitment to perfection is the final checkpoint for flawless video analysis and install tool in the system and check the code and re run the code if needed""",
    agent=qa_analyst_agent,
)
task_reboot = Task(
    description="""use insight from prompt and if any of the code is not efficient the code should be sent back to the developer for rework and all task for the code should be re run""",
    agent=manager_agent,
)
# # Define the main task of cutting frames
# cutting_frames_task = Task(
#     description="""The main task is to create a Python script that can identify and cut stationary frames in CCTV footage.
#     The script should be thoroughly tested, adhere to syntax rules and style guidelines, leverage advanced algorithms for
#     enhanced accuracy, apply computer vision techniques for precise identification, and undergo rigorous quality assurance testing.""",
#     subtasks=[task_python_dev, task_python_tester, task_syntax_tester, task_ml_engineer, task_cv_specialist, task_qa_analyst],
# )


# # Instantiate the crew with the defined agents and tasks
# crew_cutting_frames = Crew(
#     agents=[python_dev_agent, python_tester_agent, syntax_tester_agent, ml_engineer_agent, cv_specialist_agent, qa_analyst_agent],
#     tasks=[cutting_frames_task],
#     verbose=2,  # You can set it to 1 or 2 for different logging levels
# )

# Instantiate the crew with the defined agents and tasks
crew_cutting_frames = Crew(
    agents=[python_dev_agent, python_tester_agent, syntax_tester_agent, ml_engineer_agent, cv_specialist_agent, qa_analyst_agent],
    tasks=[task1,task_cv_specialist, task_qa_analyst,task_python_dev, task_python_tester, task_syntax_tester, task_ml_engineer,task_reboot ],
    verbose=2,
    #process=Process.hierarchical,
     # You can set it to 1 or 2 for different logging levels
)




# Get the security crew to work!
result = crew_cutting_frames.kickoff()

print("######################")
print(result)

# Open file for writing 
with open('result.txt', 'w') as f:

    # Write result to file
    f.write(result) 

print('Result saved to result.txt')

