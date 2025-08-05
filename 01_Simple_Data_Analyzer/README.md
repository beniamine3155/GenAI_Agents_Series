# Project 1: Simple Data Analyzer
## Online Retail Customer Behavior

This project demonstrates a powerful GenAI-based agent designed to analyze a synthetic e-commerce dataset and uncover insights through advanced data analysis, statistical operations, feature engineering, and correlation metrics. Built using LangChain and OpenAI, the agent interacts with a structured pandas DataFrame to simulate real-world retail data analysis tasks.

## 💡 Purpose

The goal of this project is to explore how GenAI agents can be used to automate and enhance the data analysis workflow — especially in contexts where real-world data is difficult to collect. By generating synthetic but realistic online retail data, this agent can:

- Perform exploratory data analysis (EDA)
- Execute advanced statistical computations
- Handle feature engineering (missing values, encoding, scaling, etc.)
- Uncover relationships and correlations between features

## 📊 Dataset Overview

The dataset mimics customer behavior on an online shopping platform and includes fields such as:

- Date, CustomerID, Gender, Age, Region, MembershipStatus, DeviceType
- TimeOnSite, PagesViewed, CartValue, Purchase (binary), SatisfactionScore

It is randomly generated using NumPy and pandas to simulate realistic patterns across 1000 records.

## 🧠 Agent Capabilities

The agent is powered by OpenAI’s GPT-4o and LangChain’s `create_pandas_dataframe_agent`, customized with a detailed system prompt. It can:

- Summarize dataset structure and metadata
- Perform descriptive stats (mean, median, mode, quartiles, IQR, skewness, etc.)
- Conduct univariate and bivariate analysis
- Handle missing values and outliers
- Encode categorical variables using one-hot, label, and ordinal encoding
- Build and analyze correlation matrices (Pearson, Spearman, etc.)
- Recommend actions or insights based on data findings

## ⚙️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/beniamine3155/GenAI_Agents_Series.git
   cd GenAI_Agents_Series
   ```

2. **Set up a virtual environment:**

   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key:**

   Create a `.env` file:

   ```
   OPENAI_API_KEY=your_openai_key_here
   ```

## 🚀 How to Use

Run the agent script and interact with the assistant:

```bash
python agent.py
```

Then ask questions like:

- "What is the average CartValue by membership tier?"
- "Detect and handle outliers in TimeOnSite."
- "Perform correlation analysis on numerical columns."
- "Encode all categorical columns using one-hot encoding."

## 📂 Project Structure

```
GenAI_Agents_Series/01_Simple_Data_Analyzer
│
├── data_analyzer.ipynb
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 📌 Dependencies

- Python 3.11+
- pandas
- numpy
- langchain
- openai
- python-dotenv


