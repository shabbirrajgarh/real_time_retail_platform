select
    transaction_id,
    customer_id,
    product,
    quantity,
    price,
    transaction_time,
    quantity * price as revenue
from transactions