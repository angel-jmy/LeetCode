# Write your MySQL query statement below
with combined as (
    select customer_number, count(order_number) as orders
    from Orders
    group by customer_number
)

select customer_number from combined
where orders = (select max(orders) from combined)