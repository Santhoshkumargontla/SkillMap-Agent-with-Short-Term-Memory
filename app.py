import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
# Load environment variables from .env file
load_dotenv()

# Step 1: Initialize the Model
google_api_key = os.getenv('GOOGLE_API_KEY')
model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=google_api_key
)

# Step 2: Create Skill Demand Search Tool (Tavily)
tavily_api_key = os.getenv('TAVILY_API_KEY')
skill_demand_tool = TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=tavily_api_key
)

# Step 3: Create Custom Job Search Tool
@tool
def search_jobs(skill: str, location: str) -> list:
    """Search for jobs requiring a specific skill using JSearch API from RapidAPI."""
    print(f"\nCalling search_jobs tool")
    print(f"Searching jobs for: {skill} in {location}")
    rapidapi_key = os.getenv('RAPIDAPI_KEY')
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    querystring = {
        "query": f"{skill} in {location}",
        "page": "1",
        "num_pages": "1"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    jobs = data.get("data", [])
    results = []
    for job in jobs[:5]:
        results.append({
            "title": job.get("job_title", "N/A"),
            "company": job.get("employer_name", "N/A"),
            "location": job.get("job_city", "N/A"),
            "type": job.get("job_employment_type", "N/A"),
            "apply_link": job.get("job_apply_link", "N/A")
        })
    return results

# Step 4: Define System Prompt
system_prompt = """You are a Skill-to-Career Mapping assistant that helps students understand skill demand and find matching job opportunities.
You have access to these tools:
- skill_demand_tool: Search for industry demand, salary insights, and career trends
- search_jobs: Find actual job listings requiring specific skills
Help the student by researching the skill they ask about and finding relevant opportunities. Present results in a clean, readable format with clear sections and proper spacing. 
Include all job details with apply links. Don't use markdown format."""

# write your code here
checkpointer = InMemorySaver()
# Step 5: Create and Run the Agent
agent = create_agent(
    model=model,
    tools=[skill_demand_tool, search_jobs],
    system_prompt=system_prompt,
    checkpointer=checkpointer,
    debug = True
)
config = {"configurable": {"thread_id": "1"}}
user_query = "What's the demand for generative ai in the industry and show me related job openings in India"
response = agent.invoke({
    "messages": [{"role": "user", "content": user_query}]
},config=config)

print(response["messages"][-1].content)



user_query = "Tell me more about the second job "
response = agent.invoke({
    "messages": [{"role": "user", "content": user_query}]
},config=config)

print(response["messages"][-1].content)