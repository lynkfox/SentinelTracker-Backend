from logging import root
from typing import Dict

import aws_cdk as core
from aws_cdk import NestedStack
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_lambda_python_alpha as python_lambda
from constructs import Construct
import os
from pathlib import Path

from configurations import ResourceNames, DirectoryLocations
from configurations.common import DeploymentProperties
from configurations.environment_variables import LambdaEnvironmentVariables

root_directory = Path(__file__).parents[1]


class LambdaStack(NestedStack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        deployment_properties: DeploymentProperties,
        dynamo_table: dynamodb.ITable,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        props = deployment_properties

        layer = aws_lambda.LayerVersion(
            self,
            ResourceNames.COMMON_LAYER,
            code=aws_lambda.Code.from_asset(
                os.path.join(root_directory, DirectoryLocations.COMMON_LAYER)
            ),
            layer_version_name=props.prefix_name(ResourceNames.COMMON_LAYER),
        )

        self.lambda_mapping = {}

        get_entity = aws_lambda.Function(
            self,
            ResourceNames.GET_ENTITY,
            function_name=props.prefix_name(ResourceNames.GET_ENTITY),
            code=aws_lambda.Code.from_asset(
                os.path.join(root_directory, DirectoryLocations.GET_ENTITY)
            ),
            environment=LambdaEnvironmentVariables(
                {}, ResourceNames.GET_ENTITY, dynamo_table.table_name
            ),
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="handler.lambda_handler",
            layers=[layer],
        )

        self.lambda_mapping[ResourceNames.GET_ENTITY] = get_entity
        dynamo_table.grant_full_access(get_entity)
