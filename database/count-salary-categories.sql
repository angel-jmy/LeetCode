# Write your MySQL query statement below
with labels as (
    select account_id, 
    (case when income < 20000 then "Low Salary"
    when income >= 20000 and income <= 50000 then "Average Salary"
    else "High Salary" end) as category
    from Accounts

    union

    select null as account_id, "Low Salary" as category

    union 

    select null as account_id, "Average Salary" as category

    union

    select null as account_id, "High Salary" as category
)

select category, count(account_id) as accounts_count
from labels
group by category;