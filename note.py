 code for cutting stationary frames in CCTV footage 

# Define AI agents for tasking with the cutting frames task
import os
from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.llms import Ollama
# Define the Ollama language model
ollama_llm = Ollama(model="mistral:7b-instruct")


 # Define a task for cutting stationary frames in CCTV footage
 cutting_frames_task = Task(
     description="""Embark on a journey to create a Python script that transcends ordinary video processing.
     Your mission is to craft a script that identifies and cuts stationary frames in CCTV footage. Elevate
     efficiency, focus on dynamic events, and be the architect of a code that stands out in its ingenuity.""",
     agent=python_dev_agent,
 )

# Define tasks for each agent
task_python_dev = Task(
    description="""Embark on a journey to create a Python script that transcends ordinary video processing.
         Your mission is to craft a script that identifies and cuts stationary frames in CCTV footage. Elevate
         efficiency, focus on dynamic events, and be the architect of a code that stands out in its ingenuity.""",
    agent=python_dev_agent,
)

task_python_tester = Task(
    description="""Your role, as a Python Tester, is to thoroughly test the Python code written by the Python Developer.
    Identify and report any bugs or issues to ensure the robustness and reliability of the stationary frame cutting script.""",
    agent=python_tester_agent,
)

task_syntax_tester = Task(
    description="""As the Syntax Tester, your mission is to analyze the Python code for adherence to syntax rules and
    style guidelines. Ensure that the code not only functions but also maintains a symphony of elegance in its structure.""",
    agent=syntax_tester_agent,
)

task_ml_engineer = Task(
    description="""Bring your expertise as a Machine Learning Engineer to implement advanced algorithms that enhance
    the accuracy of stationary frame detection in the Python script. Push the boundaries of video analysis with your contributions.""",
    agent=ml_engineer_agent,
)

task_cv_specialist = Task(
    description="""As the Computer Vision Specialist, leverage cutting-edge computer vision techniques to ensure
    precise identification of stationary frames in the CCTV footage. Transform pixels into insights with your expertise.""",
    agent=cv_specialist_agent,
)

task_qa_analyst = Task(
    description="""Your role as the Quality Assurance Analyst is critical. Conduct rigorous testing to ensure the accuracy
    and reliability of the stationary frame cutting script. Your commitment to perfection is the final checkpoint for flawless video analysis.""",
    agent=qa_analyst_agent,
)




# Define a task for cutting stationary frames in CCTV footage involving all agents
cutting_frames_task = Task(
    description="""Embark on a journey to create a Python script that transcends ordinary video processing.
    Your mission is to craft a script that identifies and cuts stationary frames in CCTV footage. Elevate
    efficiency, focus on dynamic events, and be the architect of a code that stands out in its ingenuity.""",
    agents=[python_dev_agent, python_tester_agent, syntax_tester_agent, ml_engineer_agent, cv_specialist_agent, qa_analyst_agent],
    verbose=True,
)



# Instantiate the crew with the defined agents and tasks
crew_cutting_frames = Crew(
    agents=[python_dev_agent, python_tester_agent, syntax_tester_agent, ml_engineer_agent, cv_specialist_agent, qa_analyst_agent],
    tasks=[task_python_dev, task_python_tester, task_syntax_tester, task_ml_engineer, task_cv_specialist, task_qa_analyst],
    verbose=2,  # You can set it to 1 or 2 for different logging levels
)



# Create a crew with the Python coding role agents and the cutting frames task
python_coding_crew = Crew(
    agents=[python_dev_agent, python_tester_agent, syntax_tester_agent, ml_engineer_agent, cv_specialist_agent, qa_analyst_agent],
    tasks=[cutting_frames_task],
    verbose=2,
)





# Execute the crew to perform the cutting frames task
python_coding_crew.execute_tasks()





 
 # Agent 1: Python Developer
 python_dev_agent = Agent(
     role='Python Developer',
     goal='Write efficient and functional Python code for specified tasks',
     backstory="""As a seasoned Python Developer, your journey is defined by crafting solutions with Python.
     With a passion for elegant code, your goal is to bring innovation by implementing cutting-edge scripts
     for various projects. Your code tells stories of creativity and reliability.""",
     verbose=True,
     allow_delegation=True,
     tools=[ollama_llm],
 )
 
 # Agent 2: Python Tester
 python_tester_agent = Agent(
     role='Python Tester',
     goal='Thoroughly test Python code to identify and report bugs or issues',
     backstory="""With a keen eye for detail and a commitment to perfection, you thrive as a Python Tester.
     Your role is to unravel the intricacies of code, ensuring its robustness and reliability. Your dedication
     to quality assurance plays a pivotal role in delivering flawless software.""",
     verbose=True,
     allow_delegation=True,
     tools=[ollama_llm],
 )
 
 # Agent 3: Syntax Tester
 syntax_tester_agent = Agent(
     role='Syntax Tester',
     goal='Analyze Python code for adherence to syntax rules and style guidelines',
     backstory="""As the Syntax Tester, you're not just analyzing code; you're sculpting it into an art form.
     Your meticulous approach to syntax and style guidelines ensures that every line of Python code is not just
     functional but a symphony of elegance. Your passion lies in maintaining code integrity and aesthetics.""",
     verbose=True,
     allow_delegation=False,
     tools=[ollama_llm],
 )

 # Agent 4: Machine Learning Engineer
 ml_engineer_agent = Agent(
     role='Machine Learning Engineer',
     goal='Implement advanced algorithms to enhance stationary frame detection in CCTV footage',
     backstory="""As a Machine Learning Engineer, your expertise extends beyond code.
     Your mission is to bring the power of advanced algorithms to enhance the detection of stationary frames
     in CCTV footage. Your contributions will elevate accuracy and redefine the boundaries of video analysis.""",
     verbose=True,
     allow_delegation=False,
     tools=[ollama_llm, search_tool],
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
     tools=[ollama_llm, search_tool],
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
     tools=[ollama_llm],
 )



# Set the file name
file_path = "prompt.txt"

# Open file for reading
with open(file_path, 'r') as file:
    # Read content from file
    content = file.read()

# Perform some operations on the content
result = content.upper()  # Example: Convert content to uppercase

# Open file for writing (overwriting the original file)
with open(file_path, 'w') as file:
    # Write result to file
    file.write(result)ult_task1)




    
