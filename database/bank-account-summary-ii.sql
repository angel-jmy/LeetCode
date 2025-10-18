# Write your MySQL query statement below
select u.name as name, sum(amount) as balance
from Users u join Transactions t
on u.account = t.account
group by t.account, u.name
having sum(amount) > 10000