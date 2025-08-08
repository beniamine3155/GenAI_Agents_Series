from langchain_openai import ChatOpenAI
from content_prompt import content_prompt
from dotenv import load_dotenv
load_dotenv()


## Content generation method

def generate_content(format, topic, audience, tone, length, industry, goal, keywords, style_guide, references,cta, platform):
    prompt = content_prompt.format(
        format=format,
        topic=topic,
        audience=audience,
        tone=tone,
        length=length,
        industry=industry,
        goal=goal,
        keywords=keywords,
        style_guide=style_guide,
        references=references,
        cta=cta,
        platform=platform
    )

    llm = ChatOpenAI()
    return llm.predict(prompt)


