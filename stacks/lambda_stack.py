from logging import root
from typing import Dict

import aws_cdk as core
from aws_cdk import NestedStack
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda
from aws_cdk import aws_dynamodb as dynamodb
from constructs import Construct
import os
from pathlib import Path

from configurations import ResourceNames, DirectoryLocations
from configurations.common import DeploymentProperties
from configurations.environment_variables import LambdaEnvironmentVariables

root_directory = Path(__file__).parents[1]


class LambdaStack(NestedStack):
    def __init__(
        self, scope: Construct, construct_id: str, deployment_properties: DeploymentProperties, dynamo_table: dynamodb.ITable, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        props = deployment_properties

        layer = aws_lambda.LayerVersion(
            self,
            ResourceNames.COMMON_LAYER,
            code=aws_lambda.Code.from_asset(os.path.join(root_directory, DirectoryLocations.COMMON_LAYER)),
            layer_version_name=props.prefix_name(ResourceNames.COMMON_LAYER),
        )

        self.lambda_mapping = {}

        statistics = aws_lambda.Function(
            self,
            ResourceNames.STATISTICS,
            function_name=props.prefix_name(ResourceNames.STATISTICS),
            code=aws_lambda.Code.from_asset(os.path.join(root_directory, DirectoryLocations.STATISTICS)),
            environment=LambdaEnvironmentVariables({}, ResourceNames.STATISTICS, dynamo_table.table_name).as_dict(),
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            layers=[layer],
            vpc=props.vpc,
        )

        self.lambda_mapping[ResourceNames.STATISTICS] = statistics
        dynamo_table.grant_full_access(statistics)
