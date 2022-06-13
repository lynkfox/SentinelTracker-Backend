import boto3
from common.models.character_enums import Character, AlternateTags
from common.models.enums import BoxSet, Default, Type
from typing import Union

"""

Functions found in here are for interaction with dynamodb. If they interact directly with the dynamo,
i.e. querying or insert/updating, they will expect to be passed a dynamodb resource


    Dynamodb Arrangement

    [name]#TYPE
        META#
            Character Information (BoxSet, Difficulty/Peril/Complexity, HP, Powers, ect)
        META#ALT#[alt_name]
            Character Information (BoxSet, Difficulty/Peril/Complexity, HP, Powers, ect)
        CACHE#[hash of previous requests]
            Total Victories for [name], Total Games, De-hashed values, TTL?
        CACHE#ALT#[alt_name]#[hash of previous requests]

    

"""

def build_pk(primary_name: Character, alternate_name: Union[Character, Default], box_set: BoxSet, type:Type) ->str:
    """
        builds the PK
    """

    type = type.value.upper()

    if alternate_name == AlternateTags.definitive or box_set == BoxSet.DEFINITIVE_EDITION:
        pk = f"{primary_name.value}_{AlternateTags.definitive.value}#{type}"
    else:
        pk = f"{primary_name.value}#{type}"

    return pk.replace("__", "_")

def build_meta_sk(alternate_name: Union[Character, None]) -> str:
    """
        Builds the SK
    """
    if alternate_name == AlternateTags.definitive or alternate_name is None:
        sk = f"META#"
    else:
        sk = f"META#ALT#{_deal_with_prefix_on_alt_names(alternate_name.value)}"

    return sk.replace("__", "_")

def _deal_with_prefix_on_alt_names(name:str):
    """
        removes some of the prefix's that end up on the various Enums to keep certain things distinctive in code, but clean in output

        removes:
            alt_ -- for the 1929 and 2199 alternates in Cauldron.
            definitive_ -- for the definitive alternates that have the same name as the original version.
    """
    keys = ["alt_", "definitive_"]
    for key in keys:
        name = name.replace(key, "")
    
    return name