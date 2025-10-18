# Write your MySQL query statement below
with grouped as (
    select customer_id, count(distinct product_key) as products
    from Customer
    group by customer_id
)

select customer_id from grouped
where products = (
    select count(distinct product_key) from Product
)