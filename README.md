# Diwali-Sales-Intelligence-Dashboard
# 🪔 Diwali Sales Intelligence Dashboard – Streamlit BI Project

## 📊 Overview

This project presents a **fully interactive Business Intelligence dashboard** that explores and visualizes key sales trends during the Indian festival of **Diwali**, using real-world retail transaction data.  
Built with **Streamlit, Pandas, Seaborn, and Matplotlib**, this web-based dashboard allows users to interactively filter customer demographics, geographic zones, product categories, and more—offering granular insights into consumer behavior and retail performance.

The dashboard empowers retailers, analysts, and decision-makers with **data-driven insights** to optimize marketing, product strategies, and resource allocation during festive campaigns.

## 🎯 Project Goals

- Analyze sales performance across different regions, age groups, product categories, and customer segments.
- Enable **real-time, filterable analysis** through an interactive web dashboard.
- Visualize **revenue distribution, demographic trends**, and **purchase behaviors** using intuitive charts.
- Help businesses uncover **hidden patterns** for better Diwali campaign planning.

## 🛠️ Tech Stack

| Tool        | Purpose                                  |
|-------------|-------------------------------------------|
| **Python**  | Core logic and data preprocessing         |
| **Pandas**  | Data wrangling and aggregation            |
| **Seaborn** | Visual aesthetics and styling of charts   |
| **Matplotlib** | Custom plotting and layout control     |
| **Streamlit** | Web framework for interactive dashboard |
| **CSV File** | Source data for transactions             |

## 📂 Dataset: `Enhanced_Diwali_Sales_Data.csv`

This dataset contains enriched retail transaction data collected during the Diwali sales period. Key fields include:

- `User_ID`, `Gender`, `Age Group`, `State`, `Zone`
- `Product_Category`, `Occupation`
- `Orders`, `Amount`, `Total_Spend`

👉 The field `Total_Spend` is derived from:  
```python
Total_Spend = Orders × Amount
```

## ⚙️ Dashboard Features

### ✅ Filter Options (via Sidebar)
- Gender  
- State  
- Zone (e.g., North, South, East, West)  
- Age Group  

### 📊 Visual Insights

| Visualization              | Insight Provided                                          |
|----------------------------|-----------------------------------------------------------|
| **Top Product Categories** | Displays best-selling categories during Diwali            |
| **Zone-wise Revenue**      | Highlights revenue performance across geographic zones     |
| **Gender-wise Sales**      | Reveals purchase distribution between male and female users|
| **Occupation-wise Revenue**| Identifies which professions contribute the most revenue  |
| **Age Group Spending**     | Shows which age groups are spending the most              |
| **KPIs (Top Cards)**       | Total Revenue, Avg. Transaction Value, Unique Customers   |

Each visualization updates **dynamically** based on sidebar filters for live exploratory analysis.

## 📈 Sample KPIs

- **Total Revenue:** ₹12,43,250+  
- **Avg. Transaction Value:** ₹2,145  
- **Top Performing Zone:** West  
- **Most Engaged Age Group:** 26–35 years  

## 🧠 Problem Solved

Retailers often face challenges such as:

- Inability to segment sales across demographics.  
- Lack of interactive tools for deep sales insight.  
- Underutilization of rich transaction data.  

### ✅ This project solves that by providing:
- Real-time, visual segmentation.  
- Granular filtering and KPI updates.  
- A flexible, open-source, and easy-to-use dashboard for any retailer.  

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/diwali-sales-bi-dashboard.git
cd diwali-sales-bi-dashboard
```

### 2. Install Required Libraries
```bash
pip install streamlit pandas matplotlib seaborn
```

### 3. Run the App
```bash
streamlit run app.py
```

## 🔮 Future Enhancements

- Add **time-based filters** (e.g., week-by-week analysis).
- Integrate **predictive models** for demand forecasting.
- Embed dashboard into a **company intranet or BI platform**.
- Export filtered reports as **PDF or Excel**.

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and share it.

## 🙏 Acknowledgements

- [data.gov.in](https://data.gov.in) – For open retail datasets  
- [Streamlit](https://streamlit.io) – For simplifying web-based data apps  
- Python Community – For continuous support and open libraries

📌 It demonstrates the power of **data visualization and real-time interactivity** in transforming raw data into actionable retail insights.
