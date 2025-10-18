# Write your MySQL query statement below
with firstorders as (

    select customer_id, min(order_date) as mindate
    from Delivery 
    group by customer_id

),
immediates as (
    select d.customer_id, mindate, customer_pref_delivery_date 
    from firstorders f
    join Delivery d
    on f.customer_id = d.customer_id
    and mindate = order_date
    where mindate = customer_pref_delivery_date
    
)

select round((select count(*) from immediates) / (select count(*) from firstorders) * 100, 2)
as immediate_percentage 