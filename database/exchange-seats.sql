# Write your MySQL query statement below
-- with NewSeat as (
--     select id - 1 as newid, student
--     from Seat
--     where mod(id, 2) = 0

--     union

--     select id + 1 as newid, student
--     from Seat
--     where mod(id, 2) = 1 and id <> (select max(id) from Seat)

--     union

--     select id as newid, student
--     from Seat
--     where mod(id, 2) = 1 and id = (select max(id) from Seat)
-- )

-- select newid as id, student
-- from NewSeat
-- order by id


select (
    case 
        when mod(id, 2) = 0 then id - 1 
        when mod(id, 2) = 1 and id < (select max(id) from Seat) then id + 1
        else id end
) as id, student
from Seat
order by id






