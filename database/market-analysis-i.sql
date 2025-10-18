# Write your MySQL query statement below
with in2019 as (
    select user_id, join_date, count(*) as orders_in_2019
    from Users join Orders
    on user_id = buyer_id
    where year(order_date) = 2019
    group by user_id
)

select user_id as buyer_id, join_date, orders_in_2019 from in2019

union

select user_id as buyer_id, join_date, 0 as orders_in_2019
from Users
where user_id not in (
    select user_id from in2019
)