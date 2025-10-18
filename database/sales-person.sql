# Write your MySQL query statement below
with allorders as (
    select o.order_date, o.com_id as ocom, o.sales_id as osale, s.name as person, c.name as company
    from Orders o, SalesPerson s, Company c
    where o.com_id = c.com_id
    and o.sales_id = s.sales_id
)

select name from SalesPerson
where name not in 
(
    select person from allorders
    where company = 'RED'
)