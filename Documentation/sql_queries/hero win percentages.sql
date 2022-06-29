select pos1.name,
    pos1.wins+pos2.wins+pos3.wins+pos4.wins+pos5.wins as total_wins,
    pos1.total_games+pos2.total_games+pos3.total_games+pos4.total_games+pos5.total_games as total,
    ((pos1.wins+pos2.wins+pos3.wins+pos4.wins+pos5.wins )/( pos1.total_games+pos2.total_games+pos3.total_games+pos4.total_games+pos5.total_games))*100 as perc
FROM
(
    select total.name as name,
        wins.cnt as wins,
       total.cnt as total_games,
       total.cnt-wins.cnt as losses

    from
    (
        select h.full_name as name, count(gmd.hero_one) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_one
        group by h.full_name
    ) as total,

    (
        select h.full_name as name_win, count(gmd.hero_one) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_one
        where gmd.win
        group by h.full_name
    ) as wins

    where total.name=wins.name_win
) as pos1,

(
    select total.name as name,
        wins.cnt as wins,
       total.cnt as total_games,
       total.cnt-wins.cnt as losses

    from
    (
        select h.full_name as name, count(gmd.hero_two) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_two
        group by h.full_name
    ) as total,

    (
        select h.full_name as name_win, count(gmd.hero_two) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_two
        where gmd.win
        group by h.full_name
    ) as wins

    where total.name=wins.name_win
) as pos2,

(
    select total.name as name,
        wins.cnt as wins,
       total.cnt as total_games,
       total.cnt-wins.cnt as losses

    from
    (
        select h.full_name as name, count(gmd.hero_three) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_three
        group by h.full_name
    ) as total,

    (
        select h.full_name as name_win, count(gmd.hero_three) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_three
        where gmd.win
        group by h.full_name
    ) as wins

    where total.name=wins.name_win
) as pos3,

(
    select total.name as name,
        wins.cnt as wins,
       total.cnt as total_games,
       total.cnt-wins.cnt as losses

    from
    (
        select h.full_name as name, count(gmd.hero_four) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_four
        group by h.full_name
    ) as total,

    (
        select h.full_name as name_win, count(gmd.hero_four) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_four
        where gmd.win
        group by h.full_name
    ) as wins

    where total.name=wins.name_win
) as pos4,

(
    select total.name as name,
        wins.cnt as wins,
       total.cnt as total_games,
       total.cnt-wins.cnt as losses

    from
    (
        select h.full_name as name, count(gmd.hero_five) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_five
        group by h.full_name
    ) as total,

    (
        select h.full_name as name_win, count(gmd.hero_five) as cnt
        from heroes h
        left join gameDetails gmd on h.full_name = gmd.hero_five
        where gmd.win
        group by h.full_name
    ) as wins

    where total.name=wins.name_win
) as pos5

where pos1.name=pos2.name
and pos2.name=pos3.name
and pos3.name=pos4.name
and pos4.name=pos5.name

order by perc desc limit 10
