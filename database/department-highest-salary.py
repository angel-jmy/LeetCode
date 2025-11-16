import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salaries = employee.groupby('departmentId').max()['salary'].reset_index()
    max_salaries = max_salaries[['departmentId', 'salary']].rename(columns = {'salary':'Salary'})

    max_salaries = max_salaries.merge(department, left_on = 'departmentId', right_on = 'id').rename(columns = {'name':'Department'})
    
    max_salaries = max_salaries.merge(employee[['name', 'salary', 'departmentId']], left_on = ['id', 'Salary'], right_on = ['departmentId', 'salary']).rename(columns = {'name':'Employee'})

    return max_salaries[['Department','Employee', 'Salary']]