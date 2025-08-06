# MongoDB Natural Language Query Agent

This project demonstrates an intelligent AI agent that translates natural language questions into executable MongoDB queries and returns human-readable answers. It uses LangGraph to orchestrate the multi-step workflow, LangChain for prompt engineering and LLM interaction, and PyMongo to connect to MongoDB.

## Purpose

- Allow users to interact with a MongoDB collection using plain English
- Automatically generate and run `.find()` or `.aggregate()` queries
- Return accurate and human-readable answers using an LLM
- Log query parsing, execution, and response formatting in one pipeline

## Features

- Translates user questions into MongoDB queries using an LLM
- Supports both filter and aggregation-style queries
- Parses JSON-like strings into valid Python MongoDB syntax
- Displays total document count and matched document count
- Shows top 3 result previews in logs
- Formats output with names, CGPA, department, graduation year

## Agent Workflow

1. **generate_pipeline**: Uses prompt + LLM to generate a query
2. **execute_query**: Detects query type, executes against MongoDB
3. **format_answer**: Sends results to LLM for readable summary
4. Returns complete final answer with full matching records

## Tech Stack

- Python 3.10+
- LangGraph
- LangChain
- OpenAI or compatible LLM
- PyMongo (MongoDB Python client)
- JSON, datetime, regex

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/beniamine3155/GenAI_Agents_Series.git
   cd GenAI_Agents_Series


