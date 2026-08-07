import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://retail_user:retail_password@localhost:5432/retail_dw"
)

df = pd.read_sql(
    "SELECT * FROM transactions",
    engine
)

results = []

results.append({
    "check": "transaction_id_not_null",
    "passed": df["transaction_id"].notnull().all()
})

results.append({
    "check": "customer_id_not_null",
    "passed": df["customer_id"].notnull().all()
})

results.append({
    "check": "quantity_positive",
    "passed": (df["quantity"] > 0).all()
})

results.append({
    "check": "price_positive",
    "passed": (df["price"] > 0).all()
})

allowed_products = [
    "Laptop",
    "Phone",
    "Headphones",
    "Keyboard",
    "Mouse"
]

results.append({
    "check": "valid_products",
    "passed": df["product"].isin(
        allowed_products
    ).all()
})

report = pd.DataFrame(results)

print("\nDATA QUALITY REPORT\n")
print(report)

report.to_csv(
    "docs/deliverables/data_quality/data_quality_report.csv",
    index=False
)

print(
    "\nReport saved successfully."
)