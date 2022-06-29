select pos1.name,
    pos1.wins as total_wins_against,
    pos1.total_games as total,
    (pos1.wins /pos1.total_games)*100 as perc
FROM
(
    select total.name as name,
        wins.cnt as wins,
       total.cnt as total_games,
       total.cnt-wins.cnt as losses

    from
    (
        select h.full_name as name, count(gmd.villain_one) as cnt
        from villains h
        left join gameDetails gmd on h.full_name = gmd.villain_one
        where gmd.game_mode="Normal"
        group by h.full_name
    ) as total,

    (
        select h.full_name as name_win, count(gmd.villain_one) as cnt
        from villains h
        left join gameDetails gmd on h.full_name = gmd.villain_one
        where gmd.win
        and gmd.game_mode="Normal"
        group by h.full_name
    ) as wins

    where total.name=wins.name_win
) as pos1

order by perc
