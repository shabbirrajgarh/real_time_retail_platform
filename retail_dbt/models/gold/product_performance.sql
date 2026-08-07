select
    product,
    avg(price) as avg_price,
    max(price) as max_price,
    min(price) as min_price,
    count(*) as transaction_count
from {{ ref('stg_transactions') }}
group by product