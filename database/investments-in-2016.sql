# Write your MySQL query statement below
with in2015 as (
    select tiv_2015, count(*) as num2015
    from Insurance
    group by tiv_2015
    having num2015 > 1
),
lalon as (
    select concat(cast(lat as char), cast(lon as char)) as LatLon, 
        count(*) as numlatlon
    from Insurance
    group by LatLon
    having numlatlon > 1
)

select round(sum(tiv_2016), 2) as 'tiv_2016' 
from (
    select tiv_2016 from Insurance
    where tiv_2015 in (select tiv_2015 from in2015)
    and concat(cast(lat as char), cast(lon as char)) not in (select LatLon from lalon)
) as allpossible
