from py_linq import Enumerable


def top_ten_teams(all_details: Enumerable) -> dict:
    results = all_details.select(lambda x: _get_hero_list(x)).distinct().to_list()

    results.sort()
    return results


def _get_hero_list(x) -> list:
    heroes = [x.hero_one, x.hero_two, x.hero_three, x.hero_four if x.hero_four else "zzz", x.hero_five if x.hero_five else "zzz"]

    heroes.sort()
    return heroes
