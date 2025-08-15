import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="🪔 Diwali Sales BI", layout="wide")

# Load enhanced dataset
df = pd.read_csv("Enhanced_Diwali_Sales_Data.csv")

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

# KPIs
st.title("📊 Diwali Sales Dashboard")
st.metric("💰 Total Revenue", f"₹{filtered_df['Total_Spend'].sum():,}")
st.metric("🧾 Avg. Transaction", f"₹{filtered_df['Total_Spend'].mean():.2f}" if not filtered_df.empty else "₹0")
st.metric("👤 Unique Customers", filtered_df['User_ID'].nunique())

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

st.subheader("📈 Age Group Spending Trend")
age_group_sales = filtered_df.groupby("Age Group")["Total_Spend"].sum()
if not age_group_sales.empty:
    fig5, ax5 = plt.subplots()
    sns.barplot(x=age_group_sales.index, y=age_group_sales.values, palette="coolwarm", ax=ax5)
    st.pyplot(fig5)
else:
    st.warning("⚠️ No data to display for selected filters in Age Group Sales.")

st.caption("🔗 Built with Streamlit | Enhanced Dataset for Diwali Sales Intelligence")
