# 🤖 Development Agents: Financial Analyst, Travel Planner & Orchestrator

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![ADK Mastery](https://img.shields.io/badge/Certification-ADK_Mastery-gold?style=for-the-badge&logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/Python_Development-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_2.0_Flash-8E44AD?style=for-the-badge&logo=google-gemini&logoColor=white)

Multi-Agent system (travel planner, financial analyst, and root agent) built with **Google ADK** and **Gemini 2.0**, featuring a sophisticated orchestration layer for autonomous task delegation.

## 🎯 Project Goal

The primary objective of this project is to implement a high-level hierarchical orchestration architecture. A centralized **Root Agent** serves as the intelligent interface that processes natural language user requests and dynamically delegates them to specialized expert agents in finance or travel planning, ensuring accurate and context-aware responses.

## 💡 Key Skills Demonstrated

* **Multi-Agent Orchestration:** Designing and deploying an agent hierarchy for intelligent task delegation and session state management.
* **ADK Mastery:** Advanced implementation of the **Google Agent Development Kit (ADK)** framework for building production-ready AI agents.
* **Gemini 2.0 Implementation:** Seamless integration of Google's latest generative model for reasoning and tool-calling.
* **Modern Python Tooling:** Efficient dependency management and virtual environment orchestration using **`uv`**.
* **Robust Error Handling:** Resolved complex technical challenges related to object serialization (Pydantic) and identifier validation in distributed systems.

## 📁 Files Info:

* **`multi_agents/agent.py`** — The core engine containing the orchestrator logic and sub-agent definitions.
* **`pyproject.toml`** — Configuration manifest ensuring environment reproducibility.
* **`.env.example`** — Security configuration template for API Keys (AI Studio and Google Search).

---

## ⚙️ How to run

1.  **Clone and Sync:**
    ```powershell
    git clone https://github.com/JairMoz/development-agents--financial-analyst-travel-planner-and-orchestrator-adk-antigravity.git
    cd development-agents...
    uv sync
    ```

2.  **API Configuration:**
    Create a `.env` file and add your `GEMINI_API_KEY`.

3.  **Launch the System:**
    ```powershell
    uv run adk web
    ```