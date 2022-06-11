import boto3
from common.models.entity import Entity

"""

Functions found in here are for interaction with dynamodb. They all expect to be
passed a dynamodb client/resource or a Table

"""


def get_entity(partial_entity: Entity, table: boto3.Session.Table) -> Entity:
    """
    Returns an Entity representing a Character or Environment

    Parameters:
        entity_name (Entity): A partial entity. It must have at least have
            Entity.name and Entity.type set.
        table: (boto3.resource('dynamodb').Table). A boto3 Table Resource

    Returns:
        (Entity): with all data from the dynamo for that Entity.
    """

    if partial_entity.name is None:
        raise ValueError("Missing Name on Entity")
    if partial_entity.type is None:
        raise ValueError("Missing Type on Entity")
