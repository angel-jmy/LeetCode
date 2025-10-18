# Write your MySQL query statement below
with single as (
    select num, count(*) as counts
    from MyNumbers
    group by num
    having counts = 1
    order by num desc
)

select num from single

union

select Null as num
limit 1