# ✍️ AI Content Generation Agent

An interactive Streamlit-based web application that uses advanced prompt engineering and language models (like OpenAI) to generate high-quality, customized content for different industries, audiences, and use cases.

## 🚀 Features

- Generate content in multiple formats: **Blog Post, LinkedIn Post, Email, Product Description, Whitepaper**
- Customize content by:
  - **Topic**
  - **Target Audience**
  - **Tone of Voice**
  - **Word Count**
  - **Industry or Niche**
  - **Content Goals** (Educate, Convert, Inform, etc.)
  - **SEO Keywords**
  - **Style Guide**
  - **References**
  - **Call to Action (CTA)**
  - **Publishing Platform** (Blog, LinkedIn, Website, etc.)
- Preview generated content in the app
- Download the content as a `.txt` file

## 🧠 How It Works

The app uses a structured prompt template to send detailed instructions to a language model, ensuring the generated content is relevant, engaging, and tailored to specific needs. It leverages **LangChain's `PromptTemplate`**, and integrates with `Streamlit` for the user interface.

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit** for building the UI
- **LangChain** for advanced prompt management
- **LLMs** (OpenAI GPT, HuggingFace Transformers, etc.) for generating content


## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/beniamine3155/GenAI_Agents_Series.git
cd GenAI_Agents_Series
cd 04_Content_Generation
streamlit run app.py
