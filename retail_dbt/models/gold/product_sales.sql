select
    product,
    count(*) as total_transactions,
    sum(quantity) as total_quantity,
    round(cast(sum(revenue) as numeric), 2) as total_revenue
from {{ ref('stg_transactions') }}
group by product