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
