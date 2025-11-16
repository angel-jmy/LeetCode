import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    joined = employee.merge(employee[['id', 'name', 'salary']], \
                    left_on = 'managerId', right_on = 'id',
                    suffixes = ('_e', '_m'))
    
    return joined[joined['salary_e'] > joined['salary_m']][['name_e']].rename(columns = {'name_e':'Employee'})