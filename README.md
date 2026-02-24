# Trader Performance vs Market Sentiment

## Overview

This project investigates how market sentiment (Fear vs Greed) relates to trader behavior and performance on the Hyperliquid platform. The objective was to determine whether market mood influences how traders take risk, trade, and generate profit.

To achieve this, the **Fear & Greed Index** was combined with real **Hyperliquid trade-level data**, enabling analysis of profitability patterns, behavioral shifts, and trader archetypes across different sentiment regimes.

---

## 🎯 Objectives

* Examine whether trader performance differs during Fear vs Greed periods
* Analyze how trader behavior changes with market sentiment
* Segment traders into meaningful behavioral groups
* Build a simple model to predict trade profitability
* Provide actionable, risk-aware trading insights

---

## 📂 Datasets Used

### 1️⃣ Fear & Greed Index

This dataset provides daily market sentiment.

**Key fields used:**

* `date`
* `classification` (Fear / Extreme Fear / Greed / Extreme Greed)

The dataset also contains a Unix `timestamp` and `value`, which were not required for the merge.

---

### 2️⃣ Hyperliquid Historical Trader Data

This dataset contains detailed trade-level activity from the Hyperliquid platform.

**Key fields used:**

* `account`
* `side`
* `size usd`
* `closed pnl`
* `timestamp ist` (used as the actual trade time)

**Important note:**
The numeric `timestamp` column in the dataset is an internal identifier, not the actual execution time. Therefore, **Timestamp IST** was used to derive the daily trading date.

---

## 🧹 Data Preparation

The following preprocessing steps were performed:

* Standardized column names across both datasets
* Converted `timestamp ist` to datetime and extracted daily dates
* Converted sentiment `date` to consistent format
* Merged Hyperliquid trades with Fear & Greed data at daily granularity
* Verified missing values and duplicates
* Engineered trader behavioral metrics

**Data limitation:**
The Hyperliquid dataset did not include an explicit leverage field. Trade size (USD) was used as a practical proxy for risk exposure.

---

## 📊 Key Metrics Engineered

To evaluate trader behavior and performance:

* Daily PnL per trader
* Trader win rate
* Average trade size (USD)
* Number of trades per day
* Long vs Short distribution
* Trader consistency indicators

---

## 🔍 Analysis Highlights

### 📈 Performance vs Sentiment

* Trader profitability varies across sentiment regimes
* Fear periods show wider PnL dispersion, indicating higher uncertainty
* Market sentiment appears to influence trading outcomes

---

### 🔄 Behavioral Shifts

* Traders adjust average position size depending on market mood
* Trade activity patterns differ between Fear and Greed environments
* Evidence suggests traders dynamically manage risk

---

### 👥 Trader Segmentation

Three meaningful trader groups were identified:

* **High vs Low trade size traders**
* **Frequent vs Infrequent traders**
* **Consistent vs Inconsistent performers**

Interestingly, inconsistent traders showed slightly higher average PnL (~48.95 vs ~45.80), suggesting a higher-risk, higher-reward trading style.

---

## 🤖 Predictive Modeling (Bonus)

A logistic regression model was built to predict trade profitability using:

* Market sentiment
* Trade size
* Trader historical behavior

**Result:**
The model achieved ~57% accuracy.

Given the inherent noise in short-term trading outcomes and limited feature availability, this performance is realistic and indicates modest predictive signal.

---

## 🧠 Trader Archetypes (Clustering)

KMeans clustering was applied at the trader level to identify behavioral archetypes such as:

* High-risk, high-return traders
* Conservative steady traders
* Low-activity participants

This segmentation can support personalized risk controls and trader scoring systems.

---

## 💡 Strategy Recommendations

### Strategy 1 — Dynamic Risk Adjustment

* Reduce position size during Fear regimes
* Allow controlled scaling during Greed periods

**Expected impact:** Improved downside protection during uncertain markets.

---

### Strategy 2 — Risk Controls for High-Variance Traders

* Apply stricter risk management to inconsistent traders
* Avoid optimizing purely for win rate

**Expected impact:** Preserve upside while limiting large drawdowns.

---

## 🖥️ Interactive Dashboard

A lightweight Streamlit dashboard was developed to visualize:

* PnL distribution by sentiment
* Trade size distribution
* Interactive filtering

### ▶️ Run locally

```bash
streamlit run app.py
```

## ⚙️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit

## 📁 Project Structure

project/
│
├── app.py
├── analysis.ipynb
├── requirements.txt
├── fear_greed_index.csv
├── historical_data.csv
└── README.md


