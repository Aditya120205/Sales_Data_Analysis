import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    """Loads your sales_data.csv and performs cleaning."""
    try:
        df = pd.read_csv("sales_data.csv")
    except FileNotFoundError:
        st.error("❌ 'sales_data.csv' not found. Keep it in the same folder as this script.")
        return None

    # Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Convert date column
    df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

    # --- Feature Engineering ---
    # Create Profit = Sales_Amount – (Unit_Cost * Quantity_Sold)
    df["Total_Cost"] = df["Unit_Cost"] * df["Quantity_Sold"]
    df["Profit"] = df["Sales_Amount"] - df["Total_Cost"]

    # Create Revenue = Quantity_Sold * Unit_Price
    df["Revenue"] = df["Quantity_Sold"] * df["Unit_Price"]

    # Extract Month for trend analysis
    df["Month"] = df["Sale_Date"].dt.to_period("M").dt.to_timestamp()

    return df


def main():
    st.set_page_config(page_title="Sales Dashboard", layout="wide")
    st.title("📊 Sales Data Analysis Dashboard")

    df = load_data()
    if df is None:
        return

    # ---------------- Sidebar Filters ----------------
    st.sidebar.header("Filters")

    selected_region = st.sidebar.multiselect(
        "Select Region",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )

    selected_category = st.sidebar.multiselect(
        "Select Product Category",
        options=df["Product_Category"].unique(),
        default=df["Product_Category"].unique()
    )

    df_filtered = df[
        (df["Region"].isin(selected_region)) &
        (df["Product_Category"].isin(selected_category))
    ]

    if df_filtered.empty:
        st.warning("⚠ No data available for selected filters.")
        return

    # ---------------- KPIs ----------------
    total_sales = df_filtered["Sales_Amount"].sum()
    total_profit = df_filtered["Profit"].sum()
    total_qty = df_filtered["Quantity_Sold"].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.0f}")
    # col2.metric("Total Profit", f"${total_profit:,.0f}")
    col3.metric("Total Quantity Sold", f"{total_qty:,}")

    st.markdown("---")

    # ---------------- Monthly Trend ----------------
    st.subheader("📈 Monthly Sales & Profit Trend")

    monthly = df_filtered.groupby("Month").agg({
        "Sales_Amount": "sum",
        "Profit": "sum"
    }).reset_index()

    fig_month = px.line(
        monthly,
        x="Month",
        y=["Sales_Amount", "Profit"],
        title="Monthly Trend"
    )
    st.plotly_chart(fig_month, use_container_width=True)

    # ---------------- Category & Region Analysis ----------------
    colA, colB = st.columns(2)

    with colA:
        st.subheader("💰 Revenue by Product Category")
        cat_rev = df_filtered.groupby("Product_Category")["Revenue"].sum().sort_values()
        fig_cat = px.bar(cat_rev, x=cat_rev.index, y="Revenue")
        st.plotly_chart(fig_cat, use_container_width=True)

    with colB:
        st.subheader("🌍 Region-wise Sales Share")
        region_rev = df_filtered.groupby("Region")["Revenue"].sum()
        fig_region = px.pie(region_rev, values="Revenue", names=region_rev.index, hole=0.3)
        st.plotly_chart(fig_region, use_container_width=True)

    # ---------------- Top Products ----------------
    st.subheader("🏆 Top 5 Products by Revenue")
    top_products = df_filtered.groupby("Product_ID")["Revenue"].sum().nlargest(5)
    fig_top = px.bar(top_products, x=top_products.index, y="Revenue")
    st.plotly_chart(fig_top, use_container_width=True)

    # ---------------- Correlation Heatmap ----------------
    st.subheader("📉 Correlation Matrix")

    numeric_cols = ["Quantity_Sold", "Unit_Cost", "Unit_Price", "Sales_Amount", "Profit", "Revenue"]
    corr = df_filtered[numeric_cols].corr()

    fig_corr = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Heatmap"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    # --- Histogram: Revenue Distribution ---
    st.subheader("Revenue Distribution (Histogram)")
    fig_hist = px.histogram(df_filtered, x="Revenue", nbins=40, title="Revenue Distribution")
    st.plotly_chart(fig_hist, use_container_width=True)

    # --- Scatter Plot: Units Sold vs Revenue ---
    st.subheader("Units Sold vs Revenue (Scatter Plot)")
    fig_scatter = px.scatter(
        df_filtered,
        x="Quantity_Sold",
        y="Revenue",
        title="Scatter Plot of Units Sold vs Revenue",
        trendline="ols"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # --- Additional Line Chart: Daily Revenue Trend ---
    st.subheader("Daily Revenue Trend")
    daily_revenue = df_filtered.groupby(df_filtered['Sale_Date'].dt.date)['Revenue'].sum().reset_index()
    daily_revenue.rename(columns={'Sale_Date': 'Date'}, inplace=True)
    fig_daily_line = px.line(daily_revenue, x='Date', y='Revenue', title="Daily Revenue Trend")
    st.plotly_chart(fig_daily_line, use_container_width=True)


if __name__ == "__main__":
    main()
