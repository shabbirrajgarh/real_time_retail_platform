from kafka import KafkaProducer
from faker import Faker
import json
import random
import time

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    transaction = {
        "transaction_id": fake.uuid4(),
        "customer_id": random.randint(1000, 9999),
        "product": random.choice([
            "Laptop",
            "Phone",
            "Headphones",
            "Keyboard",
            "Mouse"
        ]),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(100, 2000), 2),
        "timestamp": fake.iso8601()
    }

    producer.send("retail-transactions", transaction)

    print(transaction)

    time.sleep(2)