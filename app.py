import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Trader Performance vs Market Sentiment")

@st.cache_data
def load_data():
    sentiment = pd.read_csv("fear_greed_index.csv")
    trade = pd.read_csv("historical_data.csv")
    
    #clean columns
    sentiment.columns = sentiment.columns.str.strip().str.lower()
    trade.columns = trade.columns.str.strip().str.lower()

    # fix timestamps
    trade['timestamp'] = pd.to_datetime(trade['timestamp'], unit='ms')
    trade['date'] = trade['timestamp'].dt.date
    sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

    # merge
    merged = trade.merge(
        sentiment[['date', 'classification']],
        on='date',
        how='left'
    )
    return merged
merged = load_data()
st.subheader("PnL by Sentiment")
fig, ax = plt.subplots()
sns.boxplot(data=merged, x='classification', y='closed pnl', ax=ax)
st.pyplot(fig)
st.subheader("Trade Size Distribution")
fig2, ax2 = plt.subplots()
ax2.hist(merged['size usd'], bins=30)
st.pyplot(fig2)
st.caption(
    "Note: Trade size (USD) is used as proxy for risk exposure due to missing leverage field."
)