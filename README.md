# GenAI_Agents_Series

This repository is dedicated to exploring and building advanced GenAI (Generative AI) Agent-based projects. The core objective is to deeply understand GenAI concepts and apply them to solve real-world problems using agent-based architecture.

## Purpose

- Gain in-depth knowledge of Generative AI fundamentals and modern frameworks.
- Design and develop intelligent agents that can reason, plan, and act autonomously.
- Identify significant global challenges and propose AI-driven solutions.
- Implement multiple real-world projects using GenAI core concepts and agent frameworks.

## Features

- Agent-based design pattern applied to each use case.
- Integration of LLMs (Large Language Models) through APIs and open-source frameworks.
- Structured environment setup using virtual environments and secure configuration practices.
- Modular folder-wise project breakdown for scalability and organization.

## Environment Setup

The following steps have been completed for the initial setup:

- Created a virtual environment using `venv` to isolate dependencies.
- Added a `.env` file to securely store API keys and other environment variables.
- Prepared a `requirements.txt` file listing all necessary libraries for easy installation.
- Configured `.gitignore` to exclude sensitive and unnecessary files like `.env` and `venv/`.

## 📁 Project Structure

Each subfolder corresponds to an individual agent-based GenAI project.

```
GenAI_Agents_Series/
│
├── 01_Simple_Data_Analyzer/
├── 02_Multi_Agent_Math_Solver/
├── 03_Mongodb_Agent/
├── 04_Content_Generation/
├── 05_Campaign_Optimization/
├── 06_AI_Search_Agent/
├── 
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── agent_venv/
```

## How to Use

1. Clone this repository:
   ```
   git clone https://github.com/beniamine3155/GenAI_Agents_Series.git
   ```

2. Navigate to the project directory and activate the virtual environment:
   ```
   cd GenAI_Agents_Series
   source venv/bin/activate  # For Unix or Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Add your API keys and configuration values to the `.env` file.

5. Explore and run any project from the structured folders.

## Contribution

This is a personal learning journey, but ideas, feedback, and collaboration are welcome. Feel free to open issues or suggest improvements.


