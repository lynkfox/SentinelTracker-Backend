# Sentinels Track Backend

Repo containing the sentinels tracker back end setup, including AWS CDK deployment, lambdas, api gateway, and dynamodb setups.


This backend controls all the analysis, loading, and retrieval of statistics data through an API.

In general, users should never need to use this repo - this is around for developer access and backup.

# Assumptions Made about data:

The following assumptions are made when data is inputted into the dataset.

1. Definitive Edition Heroes and Villains *can* mix in a game entry, but unless otherwise specified a given name is **always** considered to be Enhanced Edition
    * i.e. Baron Blade is Enhanced. Baron Blade, Definitive is Definitive. Baron Blade, Mad Bomber is Enhanced. Baron Blade, Definitive Mad Bomber is Definitive.
    * Removing GameMode.MIXED from the results will remove these mixed rule-set games.
2. Advanced and/or Challenge mode applies to the entire Villain Team - not individually
3. Adamant Sentinels are always considered "As a group" - Not tracking individually if a given Southwest Sentinel is Adamant or not.
4. While the Scions, Shield, and Rewards are all recorded for OblivAeon games, only Shield is used as a sorting factor for statistics at this time
    * likewise the order of environments destroyed, additional heroes played by player slot are recorded, but not taken into account (beyond the starting team of Heroes and starting Environment)


# Querying the Data through the API

The api end point is queried with the following structure:

[type]/[name]/[alternate_tag]/[keyword]/[name]/[alternate_tag] ... ect

## Type
The `Type` in the first field sets the nature for the following keywords. It can be:
* **hero/**
* **villain/**
* **environment/**

## Name
The `name` field is just the base character name - `absolute_zero` or `baron_blade` or `insula_primalis`

## Alternate Tag
The `alternate_tag` is how to focus in on a single alt version. If left blank, the Enhanced Edition base character is used.
* like: `freedom_six` or `mad_bomber`
* `definitive` will select the characters base definitive version
* if a character has an alternate that has the same name in both EE and Definitive, the prefixing the name with definitive will indicate it should be used: `baron_blade/definitive_mad_bomber`

## Keywords:
* **in/** - The name immediately following this must be an environment name.
    * you can follow this with `/definitive` for the definitive version.
* **with/** - Pairs the name following it with the first proceeding it. All characters of the same type (hero or villain) need to be chained together.
    * `absolute_zero/with/legacy`
    * `absolute_zero/freedom_six/with/tachyon/freedom_six`
* **versus/** - This keyword switches types and the name that follows it must be the opposite type of the ones before it.
    * `absolute_zero/versus/baron_blade`
    * *with/* can be on both sides of the `versus` tag at the same time, for use with team villains.
    * `absolute_zero/with/legacy/versus/baron_blade/team_villain/plague_rat/team_villain.
* **from/** this keyword narrows the results down to a single (case sensitive) user name.

These can all be combined in any order as long as the rules of all the heroes and all the villains are on opposite sides of the versus. *note: currently environment cannot start a chain - you can do just `environment/insula_primalis` but cannot chain any further than that - further needs of refinement need to use the `in` keyword*

`hero/absolute_zero/with_legacy/in/insula_primalus/versus/baron_blade/from/Lynkfox`

# TO DO:

**Enable All keyword**
* `hero/absolute_zero/all` - gets all versions of Absolute Zero not just his base form

**Enable OR keyword**
* `hero/absolute_zero/or/legacy/in/insula_primalis` - gets all the games with *either* AZ and Legacy in Insula Primalis

**Enable BETWEEN/BEFORE/AFTER keywords**
* `hero/absolute_zero/after/2022-01-01` - only looks at the stats with a given dateframe.

**Enable sending pseudo query language in body as part of a json structure**
* Similar in idea to JSON-Logic but with less ambiguity and more sugar for friendliness
    * something like - for a generic query
    ```
    {
        "hero": {
            "name": "absolute_zero"
            "with": [("legacy", "americas_greatest")]
        }
    }
    ```

    or for something far more specific

    ```
    {
        "hero": {
            "name": "absolute_zero",
            "where": {
                "incapped": "yes",
                "number_of_players": {
                    "greater_than": 2
                }
            }
        }
    }
    ```

    basically, each Key in a given object is either a Keyword (Hero, Where, In, Greater Than, With) or an attribute in the table to compare the keyword with.
    *note for self: if key != dict, recursive parse as an instruction, else is a value*

# Setup for Development:
See `/Documentation/Setup and Organization.md` for more details.
