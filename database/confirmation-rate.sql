# Write your MySQL query statement below

select user_id, 
round(sum(case when action = 'confirmed' then 1 else 0 end) / count(action), 2)     as confirmation_rate
from Confirmations
group by user_id

union

select user_id, round(0, 2) as confirmation_rate
from Signups
where user_id not in (
    select distinct user_id from Confirmations
)