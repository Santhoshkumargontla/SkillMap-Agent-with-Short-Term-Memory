# SkillMap Agent with Short-Term Memory

An AI-powered Skill-to-Career Mapping Agent built using LangChain, LangGraph, Gemini 2.5 Flash, Tavily Search, and RapidAPI JSearch.

The agent helps students and professionals:
- Understand industry demand for specific skills
- Explore career trends and salary insights
- Discover real-time job opportunities
- Continue conversations using short-term conversational memory

---

# Features

- AI Career Guidance Assistant
- Industry Skill Demand Analysis
- Real-Time Job Search
- Conversational Memory using LangGraph
- Multi-tool Agent Architecture
- Gemini 2.5 Flash Integration
- Tavily Web Search Integration
- RapidAPI JSearch Integration

---

# Tech Stack

- Python
- LangChain
- LangGraph
- Gemini 2.5 Flash
- Tavily Search API
- RapidAPI JSearch API
- dotenv

---

# Project Architecture

User Query
   ↓
AI Agent (LangChain + Gemini)
   ↓
Tool Calling System
   ├── Tavily Search Tool
   └── JSearch Job API Tool
   ↓
Memory Checkpointer (LangGraph)
   ↓
Final Career + Job Recommendations

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Santhoshkumargontla/SkillMap-Agent-with-Short-Term-Memory.git

cd SkillMap-Agent-with-Short-Term-Memory
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key

TAVILY_API_KEY=your_tavily_api_key

RAPIDAPI_KEY=your_rapidapi_key
```

---

# APIs Used

## 1. Gemini API

Used for:
- Reasoning
- Tool calling
- Conversational responses

Get API Key:
https://aistudio.google.com/

---

## 2. Tavily Search API

Used for:
- Industry demand analysis
- Career trends
- Skill research

Get API Key:
https://app.tavily.com/

---

## 3. RapidAPI JSearch API

Used for:
- Real-time job listings
- Company details
- Job application links

Get API Key:
https://rapidapi.com/

---

# Running the Project

```bash
python app.py
```

---

# Example Queries

```text
What's the demand for generative AI in the industry?
```

```text
Show me machine learning jobs in India
```

```text
Tell me more about the second job
```

---

# Example Output

Industry Demand for Generative AI:
- High demand across AI startups and enterprise companies
- Strong hiring growth in India and globally
- Popular roles:
  - AI Engineer
  - Prompt Engineer
  - ML Engineer
  - LLM Application Developer

Job Openings:
1. Generative AI Engineer - Bangalore
2. AI Research Intern - Hyderabad
3. ML Engineer - Remote

---

# Memory Support

This project uses LangGraph's `InMemorySaver` to maintain short-term conversational memory.

Example:

User:
```text
Show me AI jobs in India
```

Follow-up:
```text
Tell me more about the second job
```

The agent remembers previous conversation context.

---

# Core Components

## 1. Skill Demand Tool

Uses Tavily Search to analyze:
- Industry demand
- Salary trends
- Future scope
- Career opportunities

---

## 2. Job Search Tool

Custom LangChain tool using JSearch API.

Returns:
- Job title
- Company name
- Location
- Employment type
- Apply link

---

## 3. LangGraph Memory

Provides:
- Thread-based conversation tracking
- Short-term memory persistence
- Context-aware responses

---

# Future Improvements

- Long-term memory integration
- Resume analysis
- Skill gap analysis
- Career roadmap generation
- Streamlit web interface
- Vector database integration
- Multi-user session management
- Salary prediction system

---

# Folder Structure

```text
SkillMap-Agent-with-Short-Term-Memory/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── venv/
```

---

# Requirements

Example `requirements.txt`

```txt
langchain
langgraph
langchain-google-genai
langchain-community
langchain-tavily
python-dotenv
requests
```

---

# Author

Gontla Santhosh Kumar

GitHub:
https://github.com/Santhoshkumargontla

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

- LangChain
- LangGraph
- Google Gemini
- Tavily
- RapidAPI# SkillMap-Agent-with-Short-Term-Memory
