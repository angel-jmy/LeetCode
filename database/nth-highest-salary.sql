CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      with ranked as 
        (select salary, dense_rank() over (order by salary DESC) as rnk
        from Employee
        )

        select distinct salary from ranked
        where 
        rnk = N
  );
END