import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from campaign_agent import generate_campaing_insights

st.set_page_config(page_title="Campaign Optimization Agent", layout="wide")
st.title("📈 Campaign Optimization Agent")

if st.button("Analyze Campaigns"):
    df, insights = generate_campaing_insights()

    st.subheader("📊 Performance Metrics")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(df, x="Campaign", y="ROAS", color="Channel", title="ROAS by Campaign")
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.scatter(df, x="CTR", y="CPC", color="Channel", size="Spend",
                          title="CTR vs CPC (Bubble Size = Spend)", hover_name="Campaign")
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig3 = px.line(df, x="Campaign", y="ROAS", markers=True, title="ROAS Trend by Campaign")
        st.plotly_chart(fig3, use_container_width=True)

        fig4 = px.pie(df, values="Spend", names="Campaign", title="Spend Distribution by Campaign")
        st.plotly_chart(fig4, use_container_width=True)

    col1, col2 = st.columns(2)
    # Channel-wise average ROAS
    with col1:
        avg_roas = df.groupby("Channel")["ROAS"].mean().reset_index()
        fig5 = px.bar(avg_roas, x="Channel", y="ROAS", title="Average ROAS by Channel", color="Channel")
        st.plotly_chart(fig5, use_container_width=True)

    # Correlation heatmap
    with col2:
        st.subheader("📌 Correlation Between Metrics")
        corr = df[["CTR", "CPC", "ROAS", "Spend"]].corr()
        fig6, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig6)

    # GPT Insights
    st.subheader("🧠 GPT Optimization Suggestions")
    st.text_area("AI Recommendations", insights, height=350)
