select
distinct concat_ws(" - ", ht.hero_one, ht.hero_two, ht.hero_three, ht.hero_four, ht.hero_five)
as  team, count(*) as count
from gameDetails
inner join heroTeams as ht on ht.id_hash = gameDetails.hero_team
where  entry_is_valid
group by team
order by count desc
limit 10
