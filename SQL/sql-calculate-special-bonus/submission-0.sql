-- Write your query below
select employee_id ,
CASE 
When employee_id % 2 != 0 and name not like 'M%' Then salary
else 0
end as bonus 
from employees
order by employee_id;