from py_linq import Enumerable
from common.rds.queries import map_row_to_GameDetails


def get_all_GameDetails_as_enumerable(sql_client) -> Enumerable:
    """
    Returns all entries as a single very large Enumerable for py_linq syntax
    """
    cursor = sql_client.cursor()
    cursor.execute(
        "SELECT * FROM gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE gameDetails.entry_is_valid"
    )
    response_rows = cursor.fetchall()
    return Enumerable([map_row_to_GameDetails(row) for row in response_rows])
