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

Enable All keyword
* `hero/absolute_zero/all` - gets all versions of Absolute Zero not just his base form

Enable OR keyword
* `hero/absolute_zero/or/legacy/in/insula_primalis` - gets all the games with *either* AZ and Legacy in Insula Primalis




# First time Setup:

## Requirements:

* python > 3.9.5
* node > 16
* aws cli v2
* aws cdk > 2.0.0

* see requirements.txt for more dev related installs.

# Directories:

## Common

Common functionality that will be used between multiple lambda's. Also will be the basis for the SDK


## google_docs

Scripts and helpers for loading the RDS on first initialization, and pulling data from the old Google Sheets

Nothing in here is Unit Tested. **use at your own risk.** Requires access to Google through Authentication (it wont work without notifying @lynkfox first), an aws account, and the CDK stacks deployed. **Use at your own risk.** Many of the files in here require some custom python pathing in order to get to work.

At the time of this writing, the script was the following stats:

31297 entries retrieved in 2.5484685999999996 seconds, and parsed in 18.090468 seconds

## lambda_functions

Individual directories for each lambda deployed in the CDK for the backend.

## stacks

The cdk stack files defining the deployment of resources to AWS

# pre-commit-config.yaml

activate with `pre-commit-install` inside your python venv after installing requirements.

# app.py

entry point for the CDK stacks

# makefile
Need to run this make file (or do the exact same commands manually) to create the layer zip for CDK deployment.
