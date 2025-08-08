from campaign_data import get_campaign_data
from campaign_prompt import campaign_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

## generate campaing insights
def generate_campaing_insights():
    df = get_campaign_data()
    formatted_table = df.to_stata(index=False)
    llm = ChatOpenAI()
    prompt = campaign_prompt.format(campaign_table = formatted_table)
    insights = llm.predict(prompt)

    return df, insights