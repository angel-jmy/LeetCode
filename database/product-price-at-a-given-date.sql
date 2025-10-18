# Write your MySQL query statement below
select product_id, new_price as price
from
(select product_id, new_price,
dense_rank() over (partition by product_id order by change_date desc) as rnk
from Products
where change_date <= '2019-08-16') as ranked
where rnk = 1

union

select distinct product_id, 10 as price
from Products
where product_id not in
(
    select distinct product_id from Products
    where change_date <= '2019-08-16'
) 