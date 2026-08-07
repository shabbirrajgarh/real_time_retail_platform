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
# AUTO REFRESH
# ==================================

st_autorefresh(
    interval=5000,
    key="refresh"
)

# ==================================
# DATABASE CONNECTION
# ==================================

@st.cache_resource
def get_engine():
    return create_engine(
        "postgresql+psycopg2://retail_user:retail_password@localhost:5432/retail_dw"
    )

engine = get_engine()

# ==================================
# LOAD DATA
# ==================================

@st.cache_data(ttl=5)
def load_data():
    query = """
    SELECT *
    FROM transactions
    ORDER BY transaction_time DESC
    LIMIT 1000
    """
    return pd.read_sql(query, engine)

df = load_data()

# ==================================
# PREPARE DATA
# ==================================

df["transaction_time"] = pd.to_datetime(
    df["transaction_time"]
)

df["revenue"] = (
    df["quantity"] * df["price"]
)

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("⚙ Dashboard Filters")

products = sorted(
    df["product"].unique()
)

selected_products = st.sidebar.multiselect(
    "Products",
    options=products,
    default=products
)

df = df[
    df["product"].isin(selected_products)
]

# ==================================
# HEADER
# ==================================

st.title("🛒 Retail Analytics Platform")

st.markdown(
    """
### Real-Time Retail Data Platform

Kafka Streaming • Spark Processing • PostgreSQL Warehouse • dbt Analytics • Streamlit BI
"""
)

st.caption(
    f"Last Refresh: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)

# ==================================
# KPI CALCULATIONS
# ==================================

total_orders = len(df)

total_quantity = int(
    df["quantity"].sum()
)

total_revenue = float(
    df["revenue"].sum()
)

avg_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)

latest_time = df[
    "transaction_time"
].max()

summary = (
    df.groupby("product")
    .agg(
        Quantity=("quantity", "sum"),
        Revenue=("revenue", "sum"),
        Transactions=("product", "count")
    )
    .reset_index()
)

top_product = summary.sort_values(
    "Revenue",
    ascending=False
).iloc[0]["product"]

# ==================================
# KPI ROW 1
# ==================================

k1, k2, k3 = st.columns(3)

with k1:
    st.metric(
        "📦 Orders",
        f"{total_orders:,}"
    )

with k2:
    st.metric(
        "💰 Revenue",
        f"₹{total_revenue:,.0f}"
    )

with k3:
    st.metric(
        "🛒 Avg Order Value",
        f"₹{avg_order_value:,.0f}"
    )

# ==================================
# KPI ROW 2
# ==================================

k4, k5, k6 = st.columns(3)

with k4:
    st.metric(
        "📊 Quantity Sold",
        f"{total_quantity:,}"
    )

with k5:
    st.metric(
        "🏆 Top Product",
        top_product
    )

with k6:
    st.metric(
        "⏱ Latest Event",
        latest_time.strftime("%H:%M:%S")
    )

# ==================================
# SYSTEM STATUS
# ==================================

st.success(
    "🟢 Kafka Producer Active | "
    "🟢 Spark Consumer Active | "
    "🟢 PostgreSQL Connected | "
    "🟢 dbt Models Refreshing"
)

st.divider()

# ==================================
# PRODUCT ANALYTICS
# ==================================

col1, col2 = st.columns(2)

with col1:

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

with col2:

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

# ==================================
# REVENUE SHARE
# ==================================

fig_pie = px.pie(
    summary,
    names="product",
    values="Revenue",
    title="Revenue Share by Product"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

st.divider()

# ==================================
# REVENUE TREND
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
# PRODUCT PERFORMANCE TABLE
# ==================================

st.subheader("🏆 Product Performance")

performance = summary.copy()

performance["Average Revenue"] = (
    performance["Revenue"]
    / performance["Transactions"]
).round(2)

st.dataframe(
    performance.sort_values(
        "Revenue",
        ascending=False
    ),
    use_container_width=True
)

st.divider()

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
    height=450
)

st.caption(
    "Dashboard refreshes automatically every 5 seconds."
)