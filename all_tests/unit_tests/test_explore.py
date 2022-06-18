import json

from models import StatsIncoming, StatisticsResponse
from results import calculate
from common.rds.queries import query
from common.rds import get_mysql_client


def test_explore():
    event = {"httpMethod": "GET", "pathParameters": {"proxy": "/villain/baron_blade"}}
    MY_SQL_CLIENT = get_mysql_client()

    _event = StatsIncoming(event)
    results = query(_event.look_up_data.operations, MY_SQL_CLIENT)
    body = calculate(_event.look_up_data, results).json()

    print(body)
