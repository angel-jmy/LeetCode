# Write your MySQL query statement below
select p.product_id, 
round(coalesce(sum(price * units), 0) / coalesce(sum(units), 1), 2) as average_price
from UnitsSold s
right join Prices p
on s.product_id = p.product_id
and purchase_date between start_date and end_date
group by p.product_id