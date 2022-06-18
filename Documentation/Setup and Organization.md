
# First time Setup:

## Requirements:

* python > 3.9.5
* node > 16
* aws cli v2
* aws cdk > 2.0.0

* see requirements.txt for more dev related installs.


## Development Installation setup:

* ensure the above requirements are set
* create a python virtual env: `python -m venv .venv`
* enter the virtual env:
    * `source .venv/bin/activate` for linux/mac
    * `& .venv/Scripts/Activate.ps1` for Powershell (windows)
* upgrade pip: `pip install -u pip`
* install requirements.txt: `pip install -r requirements.txt`
* install pre-commit: `pre-commit install`
* run makefile:
    * `make` for linux/mac
    * windows doesn't have make. You'll either need to create the common.zip file manually, or use WSL or a make equivalent for powershell.

* Begin development, making use of Unit Tests
    * i.e. run pytest after every few changes and continue to write more Unit Tests.
* Do note that Pre-Commit will run on every commit to your branch/fork. If anything 'fails' you have to `git add --a, git commit -m "same message"` again as the 'failures' are formatting.
* Open a PR when ready and request a merge.

## Setting up your own Database:

* See `Documentation\Sentinels Tracker RDS.sql` for the schema of the database
* Request a copy of the current data from Lynkfox.
* If using AWS you can deploy a copy to you your AWS account using `cdk deploy` assuming you have run `aws config` at least once
    * **Do note**, the current config of the RDS is _*NOT*_ free tier eligible and will start to gather charges (about $25 a month)
    * You can change this in `cdk/storage_stack.py`


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
