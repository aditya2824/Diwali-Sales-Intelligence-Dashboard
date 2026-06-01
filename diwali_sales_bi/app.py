import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Page config
st.set_page_config(page_title="🪔 Diwali Sales BI", layout="wide")

BASE_DIR = Path(__file__).resolve().parent

@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(BASE_DIR / "Enhanced_Diwali_Sales_Data.csv")


def format_currency(value: float) -> str:
    return f"₹{value:,.2f}"


# Load enhanced dataset
df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Data")
gender = st.sidebar.multiselect("Select Gender:", options=df['Gender'].unique(), default=df['Gender'].unique())
state = st.sidebar.multiselect("Select State:", options=df['State'].unique(), default=df['State'].unique())
zone = st.sidebar.multiselect("Select Zone:", options=df['Zone'].unique(), default=df['Zone'].unique())
age_group = st.sidebar.multiselect("Select Age Group:", options=df['Age Group'].unique(), default=df['Age Group'].unique())

# Filtered data
filtered_df = df[(df['Gender'].isin(gender)) &
                 (df['State'].isin(state)) &
                 (df['Zone'].isin(zone)) &
                 (df['Age Group'].isin(age_group))]

st.title("📊 Diwali Sales Dashboard")

# Export filtered data
st.sidebar.subheader("Export Data")
csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.sidebar.download_button(
    label="Download filtered data as CSV",
    data=csv_data,
    file_name="filtered_diwali_sales_data.csv",
    mime="text/csv",
)

# KPIs
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.metric("💰 Total Revenue", format_currency(filtered_df['Total_Spend'].sum()))
with kpi2:
    avg_transaction = filtered_df['Total_Spend'].mean() if not filtered_df.empty else 0
    st.metric("🧾 Avg. Transaction", format_currency(avg_transaction))
with kpi3:
    st.metric("👤 Unique Customers", f"{filtered_df['User_ID'].nunique():,}")

st.divider()

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Top Product Categories")
    top_categories = filtered_df['Product_Category'].value_counts().head(10)
    if not top_categories.empty:
        fig1, ax1 = plt.subplots()
        sns.barplot(x=top_categories.values, y=top_categories.index, palette="magma", ax=ax1)
        st.pyplot(fig1)
    else:
        st.warning("⚠️ No data to display for selected filters in Product Categories.")

with col2:
    st.subheader("🧭 Zone-wise Revenue")
    zone_sales = filtered_df.groupby('Zone')['Total_Spend'].sum().sort_values()
    if not zone_sales.empty:
        fig2, ax2 = plt.subplots()
        zone_sales.plot(kind="barh", color="teal", ax=ax2)
        st.pyplot(fig2)
    else:
        st.warning("⚠️ No data to display for selected filters in Zone-wise Revenue.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("👩 Gender-wise Sales")
    gender_sales = filtered_df.groupby("Gender")["Total_Spend"].sum()
    if not gender_sales.empty:
        fig3, ax3 = plt.subplots()
        ax3.pie(gender_sales, labels=gender_sales.index, autopct="%1.1f%%", startangle=90, colors=["#FFA07A", "#20B2AA"])
        st.pyplot(fig3)
    else:
        st.warning("⚠️ No data to display for selected filters in Gender-wise Sales.")

with col4:
    st.subheader("👔 Occupation-wise Revenue")
    occupation_sales = filtered_df.groupby("Occupation")["Total_Spend"].sum().sort_values(ascending=False).head(10)
    if not occupation_sales.empty:
        fig4, ax4 = plt.subplots()
        sns.barplot(x=occupation_sales.values, y=occupation_sales.index, palette="cool", ax=ax4)
        st.pyplot(fig4)
    else:
        st.warning("⚠️ No data to display for selected filters in Occupation-wise Revenue.")

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.subheader("🏆 Top Customers by Spend")
    customer_sales = (
        filtered_df.groupby(["User_ID", "Cust_name"], as_index=False)["Total_Spend"]
        .sum()
        .sort_values("Total_Spend", ascending=False)
        .head(10)
    )
    if not customer_sales.empty:
        customer_sales["Customer"] = customer_sales["Cust_name"].fillna("Customer") + " (" + customer_sales["User_ID"].astype(str) + ")"
        fig5, ax5 = plt.subplots()
        sns.barplot(data=customer_sales, x="Total_Spend", y="Customer", palette="viridis", ax=ax5)
        ax5.set_xlabel("Total Spend")
        ax5.set_ylabel("")
        st.pyplot(fig5)
        st.dataframe(customer_sales[["User_ID", "Cust_name", "Total_Spend"]], use_container_width=True)
    else:
        st.warning("⚠️ No data to display for selected filters in Top Customers.")

with col6:
    st.subheader("🗺️ State-wise Revenue Dashboard")
    state_sales = (
        filtered_df.groupby("State", as_index=False)["Total_Spend"]
        .sum()
        .sort_values("Total_Spend", ascending=False)
    )
    if not state_sales.empty:
        total_state_revenue = state_sales["Total_Spend"].sum()
        state_sales["Revenue_Contribution_%"] = (state_sales["Total_Spend"] / total_state_revenue * 100).round(2)
        fig6, ax6 = plt.subplots()
        sns.barplot(data=state_sales.head(10), x="Total_Spend", y="State", palette="crest", ax=ax6)
        ax6.set_xlabel("Total Revenue")
        ax6.set_ylabel("")
        st.pyplot(fig6)
        st.dataframe(state_sales.head(10), use_container_width=True)
    else:
        st.warning("⚠️ No data to display for selected filters in State-wise Revenue.")

st.divider()

st.subheader("📈 Age Group Spending Trend")
age_group_sales = filtered_df.groupby("Age Group")["Total_Spend"].sum()
if not age_group_sales.empty:
    fig7, ax7 = plt.subplots()
    sns.barplot(x=age_group_sales.index, y=age_group_sales.values, palette="coolwarm", ax=ax7)
    st.pyplot(fig7)
else:
    st.warning("⚠️ No data to display for selected filters in Age Group Sales.")

st.divider()

st.subheader("🔗 Correlation Heatmap")
numeric_columns = [col for col in ["Orders", "Amount", "Age", "Marital_Status", "Total_Spend"] if col in filtered_df.columns]
if len(numeric_columns) >= 2 and not filtered_df.empty:
    correlation_df = filtered_df[numeric_columns].corr(numeric_only=True)
    fig8, ax8 = plt.subplots(figsize=(8, 5))
    sns.heatmap(correlation_df, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax8)
    st.pyplot(fig8)
else:
    st.warning("⚠️ Not enough numeric data available to build the correlation heatmap.")

st.caption("🔗 Built with Streamlit | Enhanced Dataset for Diwali Sales Intelligence")
