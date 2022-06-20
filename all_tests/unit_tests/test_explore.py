import json

from models import StatsIncoming, StatisticsResponse
from results import calculate
from common.rds.queries import query
from common.rds import get_mysql_client
from common.models.schema_models import HeroTeam

from lambda_functions.periodic_stats.periodic_utilities import get_all_GameDetails_as_enumerable
from lambda_functions.periodic_stats.team_based_results import top_ten_teams


def test_explore():
    event = {"httpMethod": "GET", "pathParameters": {"proxy": "hero/legacy/americas_greatest"}}
    MY_SQL_CLIENT = get_mysql_client()

    _event = StatsIncoming(event)
    results = query(_event.look_up_data.operations, MY_SQL_CLIENT)
    body = calculate(_event.look_up_data, results).json(exclude_none=True)
    body = json.loads(body)
    print("")


def test_explore2():
    MY_SQL_CLIENT = get_mysql_client()

    team = HeroTeam(hero_one="Absolute Zero", hero_two="Legacy", hero_three="Bunker")

    # results = get_all_GameDetails_as_enumerable(MY_SQL_CLIENT)

    # top_teams = top_ten_teams(results)

    print("")
