SELECT g.end_result, Count(g.end_result) as amount, count(*)/derived.total*100 as percentage, derived.total
from gameDetails as g,  ( select count(*) as total from gameDetails as g Where "Absolute Zero" in(g.hero_one, g.hero_two, g.hero_three, g.hero_four, g.hero_five) and g.entry_is_valid is True ) as derived
Where "Absolute Zero" in(g.hero_one, g.hero_two, g.hero_three, g.hero_four, g.hero_five)
	and g.entry_is_valid is True
group by g.end_result;
