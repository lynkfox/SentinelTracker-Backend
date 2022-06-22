OPPONENTS_CHOSEN = """
select c1.villain1,
       c1.cnt as pos1,
       c2.cnt as pos2,
       c3.cnt as pos3,
       c4.cnt as pos4,
       c5.cnt as pos5,
       c1.cnt+c2.cnt+c3.cnt+c4.cnt+c5.cnt as total
from
(
select h.full_name as villain1, count(ht.villain_one) as cnt
from villains h
left join gameDetails ht on h.full_name = ht.villain_one
group by h.full_name
) as c1,

(
select h2.full_name as villain2, count(ht2.villain_two) as cnt
from villains h2
left join gameDetails ht2 on h2.full_name = ht2.villain_two
group by h2.full_name
) as c2,

(
select h3.full_name as villain3, count(ht3.villain_three) as cnt
from villains h3
left join gameDetails ht3 on h3.full_name = ht3.villain_three
group by h3.full_name
) as c3,

(
select h4.full_name as villain4, count(ht4.villain_four) as cnt
from villains h4
left join gameDetails ht4 on h4.full_name = ht4.villain_four
group by h4.full_name
) as c4,

(
select h5.full_name as villain5, count(ht5.villain_five) as cnt
from villains h5
left join gameDetails ht5 on h5.full_name = ht5.villain_five
group by h5.full_name
) as c5

where c1.villain1 = c2.villain2
and   c2.villain2 = c3.villain3
and   c3.villain3 = c4.villain4
and   c4.villain4 = c5.villain5
and (c1.cnt+c2.cnt+c3.cnt+c4.cnt+c5.cnt) != 0
and c2.cnt = 0

order by total desc
"""

HEROES_CHOSEN = """
select c1.hero1,
       c1.cnt as pos1,
       c2.cnt as pos2,
       c3.cnt as pos3,
       c4.cnt as pos4,
       c5.cnt as pos5,
       c1.cnt+c2.cnt+c3.cnt+c4.cnt+c5.cnt as total
from
(
select h.full_name as hero1, count(ht.hero_one) as cnt
from heroes h
left join gameDetails ht on h.full_name = ht.hero_one
group by h.full_name
) as c1,

(
select h2.full_name as hero2, count(ht2.hero_two) as cnt
from heroes h2
left join gameDetails ht2 on h2.full_name = ht2.hero_two
group by h2.full_name
) as c2,

(
select h3.full_name as hero3, count(ht3.hero_three) as cnt
from heroes h3
left join gameDetails ht3 on h3.full_name = ht3.hero_three
group by h3.full_name
) as c3,

(
select h4.full_name as hero4, count(ht4.hero_four) as cnt
from heroes h4
left join gameDetails ht4 on h4.full_name = ht4.hero_four
group by h4.full_name
) as c4,

(
select h5.full_name as hero5, count(ht5.hero_five) as cnt
from heroes h5
left join gameDetails ht5 on h5.full_name = ht5.hero_five
group by h5.full_name
) as c5

where c1.hero1 = c2.hero2
and   c2.hero2 = c3.hero3
and   c3.hero3 = c4.hero4
and   c4.hero4 = c5.hero5
and (c1.cnt+c2.cnt+c3.cnt+c4.cnt+c5.cnt) != 0

order by total

"""

LOCATIONS_CHOSEN = """
select h.full_name as environment, count(ht.environment) as total
from environments h
left join gameDetails ht on h.full_name = ht.environment
group by h.full_name
order by total desc

"""

TEAMS_CHOSEN = """
select
distinct concat_ws(" - ", ht.hero_one, ht.hero_two, ht.hero_three, ht.hero_four, ht.hero_five)
as  team, count(*) as count
from gameDetails
inner join heroTeams as ht on ht.id_hash = gameDetails.hero_team
where  entry_is_valid
group by team
order by count desc
"""
