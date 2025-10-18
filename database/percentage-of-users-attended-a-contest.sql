# Write your MySQL query statement below
-- with combined as (
    -- select contest_id, u.user_id
    -- from Users u
    -- left join Register r 
    -- on u.user_id = r.user_id
-- )

select contest_id, 
round(count(*) / 
(
    select count(*) from Users
)
 * 100, 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id asc