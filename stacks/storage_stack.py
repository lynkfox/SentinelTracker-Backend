import aws_cdk as core
from aws_cdk import NestedStack
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_s3 as s3
from constructs import Construct

from configurations import ResourceNames
from configurations.common import DeploymentProperties
from common.attributes import DynamoAttributes


class StorageStack(NestedStack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        deployment_properties: DeploymentProperties,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        """
            Contains the Storage Resources such as S3, Dynamodb, Parameter/Secrets
        """
        props = deployment_properties

        self.sentinels_dynamo = dynamodb.Table(
            self,
            ResourceNames.ITEM_DYNAMODB,
            table_name=props.prefix_name(ResourceNames.ITEM_DYNAMODB),
            partition_key=dynamodb.Attribute(
                name=DynamoAttributes.PARTITION_KEY, type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name=DynamoAttributes.SORT_KEY, type=dynamodb.AttributeType.STRING
            ),
            removal_policy=core.RemovalPolicy.DESTROY,
        )
