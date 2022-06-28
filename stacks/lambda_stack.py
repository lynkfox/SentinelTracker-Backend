import aws_cdk as core
from aws_cdk import NestedStack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_lambda
from aws_cdk import aws_rds as rds
from constructs import Construct
import os
from pathlib import Path

from configurations import ResourceNames, DirectoryLocations
from configurations.common import DeploymentProperties
from configurations.environment_variables import LambdaEnvironmentVariables

root_directory = Path(__file__).parents[1]


class LambdaStack(NestedStack):
    def __init__(
        self, scope: Construct, construct_id: str, deployment_properties: DeploymentProperties, rds_table: rds.DatabaseProxy, **kwargs
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
            environment=LambdaEnvironmentVariables({}, ResourceNames.STATISTICS, rds_table.endpoint).as_dict(),
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            timeout=core.Duration.seconds(29),
            layers=[layer],
            memory_size=512,
            vpc=props.vpc,
            security_groups=props.security_groups,
            allow_public_subnet=True,
        )

        self.lambda_mapping[ResourceNames.STATISTICS] = statistics
        rds_table.grant_connect(statistics)
        rds_table.connections.allow_from(statistics.connections, port_range=ec2.Port.tcp(3306))

        add_entry = aws_lambda.Function(
            self,
            ResourceNames.POST_ENTRY,
            function_name=props.prefix_name(ResourceNames.POST_ENTRY),
            code=aws_lambda.Code.from_asset(os.path.join(root_directory, DirectoryLocations.POST_ENTRY)),
            environment=LambdaEnvironmentVariables({}, ResourceNames.POST_ENTRY, rds_table.endpoint).as_dict(),
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            timeout=core.Duration.seconds(29),
            layers=[layer],
            memory_size=512,
            vpc=props.vpc,
            security_groups=props.security_groups,
            allow_public_subnet=True,
        )

        self.lambda_mapping[ResourceNames.POST_ENTRY] = add_entry
        rds_table.grant_connect(add_entry)
        rds_table.connections.allow_from(add_entry.connections, port_range=ec2.Port.tcp(3306))
