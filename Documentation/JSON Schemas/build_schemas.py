import json
from lambda_functions.statistics.models import StatisticsResponse
from common.models.schema_models import GameDetail

"""
Handy script for building schema files.
"""

if __name__ == "__main__":

    with open("Documentation\JSON Schemas\statistics_response.json", "w", encoding="utf-8") as f:
        json.dump(StatisticsResponse.schema(), f, ensure_ascii=False, indent=4)

    with open("Documentation\JSON Schemas\input_game_details.json", "w") as f:
        schema = GameDetail.schema()
        del schema["definitions"]["HeroTeam"]
        del schema["definitions"]["VillainOpponent"]
        del schema["definitions"]["User"]
        json.dump(schema, f, ensure_ascii=False, indent=4)
