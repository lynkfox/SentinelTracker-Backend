import os
from pathlib import Path

import aws_cdk as core
from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

from configurations import DirectoryLocations, ResourceNames
from configurations.common import DeploymentProperties
from stacks.storage_stack import StorageStack
from stacks.lambda_stack import LambdaStack
from stacks.api_stack import ApiStack

root_directory = Path(__file__).parents[1]


class MainStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        deployment_properties: DeploymentProperties,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.props = deployment_properties
        self.props.vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        storage = StorageStack(self, "StorageStack", self.props)

        functions = LambdaStack(self, "Lambdas", self.props, storage.sentinels_dynamo)

        api = ApiStack(self, "Api", self.props, functions.lambda_mapping)

        core.CfnOutput(
            self,
            "ApiEndpoint",
            value=api.backend_api.url,
            export_name="apiUrl",
        )
