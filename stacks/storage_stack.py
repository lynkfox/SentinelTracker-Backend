import aws_cdk as core
from aws_cdk import NestedStack
from aws_cdk import aws_rds as rds
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from constructs import Construct

from configurations import ResourceNames
from configurations.common import DeploymentProperties


class StorageStack(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, deployment_properties: DeploymentProperties, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        """
            Contains the Storage Resources such as S3, Dynamodb, Parameter/Secrets
        """
        props = deployment_properties

        self.statistics = rds.DatabaseInstance(
            self,
            ResourceNames.STATISTICS_RDS,
            allocated_storage=25,
            database_name="",
            delete_automated_backups=True,
            max_allocated_storage=50,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE4_GRAVITON, ec2.InstanceSize.SMALL),
            instance_identifier=props.prefix_name(ResourceNames.STATISTICS_RDS, lower=True),
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_28,
            ),
            vpc=props.vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT),
        )

        self.rds_proxy = rds.DatabaseProxy(
            self,
            f"{ResourceNames.STATISTICS_RDS}proxy",
            secrets=[self.statistics.secret],
            vpc=props.vpc,
            proxy_target=rds.ProxyTarget.from_instance(self.statistics),
            iam_auth=True,
        )
