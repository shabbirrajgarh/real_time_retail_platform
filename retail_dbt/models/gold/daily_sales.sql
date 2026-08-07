select
    date(transaction_time) as sales_date,
    count(*) as total_orders,
    sum(quantity) as total_quantity,
    round(cast(sum(revenue) as numeric), 2) as total_revenue
from {{ ref('stg_transactions') }}
group by 1