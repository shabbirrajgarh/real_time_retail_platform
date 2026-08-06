from kafka import KafkaProducer
from faker import Faker
from datetime import datetime
import json
import random
import time

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

PRODUCTS = [
    "Laptop",
    "Phone",
    "Headphones",
    "Keyboard",
    "Mouse"
]

print("🚀 Retail Producer Started...")

while True:
    transaction = {
        "transaction_id": fake.uuid4(),
        "customer_id": random.randint(1000, 9999),
        "product": random.choice(PRODUCTS),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(100, 2000), 2),

        # REAL CURRENT TIMESTAMP
        "timestamp": datetime.now().isoformat()
    }

    producer.send("retail-transactions", transaction)
    producer.flush()

    print(transaction)

    time.sleep(2)