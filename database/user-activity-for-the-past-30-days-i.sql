# Write your MySQL query statement below
-- select a1.activity_date as `day`, count(distinct a2.user_id) as active_users
-- from Activity a1 join Activity a2
-- on a2.activity_date between a1.activity_date - interval 30 day and a1.activity_date
-- group by a1.activity_date
-- having a1.activity_date <= '2019-07-27'


select activity_date as `day`, count(distinct user_id) as active_users
from Activity
where activity_date between '2019-07-27' - interval 29 day and '2019-07-27'
group by activity_date
