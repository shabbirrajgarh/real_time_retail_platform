import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Retail Analytics Platform",
    page_icon="🛒",
    layout="wide"
)

# ==================================
# AUTO REFRESH EVERY 5 SECONDS
# ==================================

st_autorefresh(interval=5000, key="refresh")

# ==================================
# DATABASE
# ==================================

engine = create_engine(
    "postgresql+psycopg2://retail_user:retail_password@localhost:5432/retail_dw"
)

# ==================================
# LOAD ONLY RECENT DATA
# ==================================

query = """
SELECT *
FROM transactions
ORDER BY transaction_time DESC
LIMIT 1000
"""

df = pd.read_sql(query, engine)

df["transaction_time"] = pd.to_datetime(df["transaction_time"])
df["revenue"] = df["quantity"] * df["price"]

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("⚙ Dashboard Filters")

selected_products = st.sidebar.multiselect(
    "Products",
    options=sorted(df["product"].unique()),
    default=sorted(df["product"].unique())
)

df = df[df["product"].isin(selected_products)]

# ==================================
# HEADER
# ==================================

st.title("🛒 Retail Analytics Platform")

st.markdown(
    """
### Live Retail Analytics Dashboard
Kafka • PostgreSQL • Spark • dbt • Streamlit
"""
)

st.caption(
    f"Last Refresh: {datetime.now().strftime('%H:%M:%S')}"
)

# ==================================
# KPIs
# ==================================

total_orders = len(df)
total_quantity = int(df["quantity"].sum())
total_revenue = float(df["revenue"].sum())
latest_time = df["transaction_time"].max()

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Orders",
    f"{total_orders:,}"
)

k2.metric(
    "Quantity",
    f"{total_quantity:,}"
)

k3.metric(
    "Revenue",
    f"₹{total_revenue:,.0f}"
)

k4.metric(
    "Latest Event",
    latest_time.strftime("%H:%M:%S")
)

st.divider()

# ==================================
# PRODUCT CHARTS
# ==================================

summary = (
    df.groupby("product")
    .agg(
        Quantity=("quantity", "sum"),
        Revenue=("revenue", "sum")
    )
    .reset_index()
)

c1, c2 = st.columns(2)

with c1:
    fig_qty = px.bar(
        summary,
        x="product",
        y="Quantity",
        title="Quantity Sold by Product"
    )

    st.plotly_chart(
        fig_qty,
        use_container_width=True
    )

with c2:
    fig_rev = px.bar(
        summary,
        x="product",
        y="Revenue",
        title="Revenue by Product"
    )

    st.plotly_chart(
        fig_rev,
        use_container_width=True
    )

st.divider()

# ==================================
# SALES TREND
# ==================================

trend = (
    df.groupby(
        pd.Grouper(
            key="transaction_time",
            freq="1min"
        )
    )
    .agg(
        Revenue=("revenue", "sum")
    )
    .reset_index()
)

fig_trend = px.line(
    trend,
    x="transaction_time",
    y="Revenue",
    title="Revenue Trend"
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)

st.divider()

# ==================================
# TOP PRODUCTS
# ==================================

st.subheader("🏆 Top Products")

top_products = summary.sort_values(
    "Revenue",
    ascending=False
)

st.dataframe(
    top_products,
    use_container_width=True
)

# ==================================
# LIVE TRANSACTION FEED
# ==================================

st.subheader("🔴 Latest Transactions")

latest_transactions = df[
    [
        "transaction_time",
        "transaction_id",
        "product",
        "quantity",
        "price",
        "revenue"
    ]
].head(50)

st.dataframe(
    latest_transactions,
    use_container_width=True,
    height=400
)

st.caption(
    "Auto refreshes every 5 seconds"
)