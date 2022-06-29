import json

from models import StatsIncoming, StatisticsResponse
from results import calculate
from common.rds.queries import query
from common.rds import get_mysql_client
from common.models.schema_models import HeroTeam

from lambda_functions.periodic_stats.periodic_utilities import get_all_GameDetails_as_enumerable
from lambda_functions.periodic_stats.team_based_results import top_ten_teams
from lambda_functions.game_detail_entry.entry_models import GameDetailIncoming

null = None
false = False
true = True


def test_explore():
    event = {"httpMethod": "GET", "pathParameters": {"proxy": "hero/legacy/americas_greatest"}}
    MY_SQL_CLIENT = get_mysql_client()

    _event = StatsIncoming(event)
    results = query(_event.look_up_data.operations, MY_SQL_CLIENT)
    body = calculate(_event.look_up_data, results).json(exclude_none=True)
    body = json.loads(body)
    print("")


def test_explore2():
    # MY_SQL_CLIENT = get_mysql_client()

    entry = {
        "resource": "/v1/add",
        "path": "/v1/add",
        "httpMethod": "POST",
        "body": '{\n    "username": "Lynkfox",\n    "game_mode": "Normal",\n    "selection_method": "Random",\n    "platform": "Physical",\n    "end_result": "The Hero\'s Triumph (Villain(s) Incapacitated)",\n    "estimated_time": "Not Known / Not Recorded",\n    "number_of_players": 1,\n    "number_of_heroes": 3,\n    "perceived_difficulty": 2,\n    "environment": "Insula Primalis",\n    "hero_one": "Absolute Zero",\n    "hero_one_incapped": false,\n    "hero_two": "Legacy",\n    "hero_two_incapped": false,\n    "hero_three": "Tachyon, Super Scientific",\n    "hero_three_incapped": false,\n    "villain_one": "Baron Blade",\n    "villain_one_incapped": true,\n    "advanced": true,\n    "comment": "Test Entry"\n}',
    }
    value = GameDetailIncoming(entry)

    new_value = value.entry_data.get_insert_statement()

    print("")
