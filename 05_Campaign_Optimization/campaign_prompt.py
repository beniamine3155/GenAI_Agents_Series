from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

campaign_prompt = PromptTemplate.from_template(
    """
You are a digital marketing analyst.

Analyze the following campaign performance data:
{campaign_table}

Identify:
1. Campaigns with low performance (based on CTR, CPC, ROAS)
2. Suggested changes (budget reallocation, creative type, A/B testing)
3. Optimized strategy for next month

Format the response as a bulleted report.
"""
)