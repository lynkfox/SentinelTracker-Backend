#!/usr/bin/env python3
import os

import aws_cdk as cdk

from configurations.common import DeploymentProperties
from stacks.sentine_tracker_backend import MainStack

app = cdk.App()
default_environment = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
)
deployment_props = DeploymentProperties()
MainStack(
    app,
    "SentinelTrackerBackend",
    env=default_environment,
    deployment_properties=deployment_props,
)
app.synth()
