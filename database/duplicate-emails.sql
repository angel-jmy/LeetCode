# Write your MySQL query statement below
-- with Counts as (select email, count(email) as counts
-- from Person
-- group by email
-- )

-- select email as Email from 
-- Counts
-- where counts > 1

select email as Email
from Person
group by Email
having count(*) > 1