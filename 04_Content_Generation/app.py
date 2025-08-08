import streamlit as st
from dotenv import load_dotenv
from content_agent import generate_content
load_dotenv()


st.set_page_config(page_title="AI Content Generator", layout="centered")
st.title("✍️ AI Content Generation Agent")

# Basic content fields
topic = st.text_input("Enter topic:", "AI in healthcare")
audience = st.text_input("Target audience:", "Healthcare executives")
content_format = st.selectbox("Content format:", ["Blog Post", "LinkedIn Post", "Email", "Product Description", "Whitepaper"])
tone = st.selectbox("Tone of voice:", ["Professional", "Conversational", "Witty", "Urgent", "Empathetic"])
length = st.slider("Word count target:", 50, 2000, 500)

# Extended prompt variables
industry = st.text_input("Industry or Niche:", "Healthcare")
goal = st.selectbox("Content Goal:", ["Educate", "Convert", "Inform", "Inspire", "Entertain"])
keywords = st.text_input("SEO Focus Keywords (comma-separated):", "AI in healthcare, patient outcomes, medical automation")
style_guide = st.text_area("Style Guide / Preferences:", "Use short paragraphs, avoid technical jargon, add real-world examples.")
references = st.text_input("References to mention (optional):", "WHO AI Guidelines 2024")
cta = st.text_input("Call to Action (CTA):", "Download our free AI in Healthcare whitepaper.")
platform = st.selectbox("Publishing Platform:", ["Blog", "LinkedIn", "Website", "Email Newsletter", "Medium"])

# Button to generate content
if st.button("Generate Content"):
    content = generate_content(
        topic=topic,
        audience=audience,
        format=content_format,
        tone=tone,
        length=length,
        industry=industry,
        goal=goal,
        keywords=keywords,
        style_guide=style_guide,
        references=references,
        cta=cta,
        platform=platform,
    )
    
    st.subheader("📝 Generated Content")
    st.text_area("Content", content, height=400)
    st.download_button("Download as .txt", content, file_name="content.txt")

