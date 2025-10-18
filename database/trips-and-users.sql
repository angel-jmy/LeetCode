# Write your MySQL query statement below
-- select request_at as `Day`, 
--         round(sum(case when status like 'cancelled%' then 1 else 0 end) / count(*), 2) as `Cancellation Rate`
-- from Trips t
-- left join Users d
-- on t.driver_id = d.users_id
-- left join Users c
-- on t.client_id = c.users_id
-- where d.banned <> 'Yes' and c.banned <> 'Yes'
-- group by request_at
-- having request_at between '2013-10-01' and '2013-10-03'

select request_at as `Day`, round(sum(
    case when status like 'cancelled%' then 1 else 0 end
) / count(*), 2) as `Cancellation Rate`
from Trips t join Users c
on t.client_id = c.users_id
join Users d
on t.driver_id = d.users_id
where c.banned = 'No' and d.banned = 'No'
group by request_at
having request_at between '2013-10-01' and '2013-10-03'








