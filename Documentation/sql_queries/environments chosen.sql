select h.full_name as environment, count(ht.environment) as total
from environments h
left join gameDetails ht on h.full_name = ht.environment
group by h.full_name
order by total desc limit 10
