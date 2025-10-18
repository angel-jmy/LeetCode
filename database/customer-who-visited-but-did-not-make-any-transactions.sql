# Write your MySQL query statement below
-- select customer_id, count(*) as count_no_trans
-- from Visits v 
-- left join Transactions t
-- where v.visit_id = t.visit_id and transaction_id is Null
-- group by customer_id

with combined as (
    select customer_id, v.visit_id, transaction_id
    from Visits v
    left join Transactions t
    on v.visit_id = t.visit_id
)

select customer_id, count(*) as count_no_trans
from combined
where transaction_id is Null
group by customer_id