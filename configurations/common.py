from dataclasses import dataclass, field
from aws_cdk import aws_ec2 as ec2
from typing import Optional


@dataclass
class DeploymentProperties:
    PREFIX: str = field(default="Sentinels")
    ENVIRONMENT: str = field(default="DEMO")
    vpc: Optional[ec2.IVpc] = field(default=None)

    def prefix_name(self, name: str, lower: bool = False) -> str:
        """
        Returns the name-tag ready to be prefixed on a resource

        Parameters:
            name(str): Name of the resource.
            lower(bool) [Optional]: Defaults False, set true for resources like S3.

        Returns:
            (str): Name prefixed with Prefix and Environment with dashes between.
        """
        full_name = f"{self.PREFIX}-{self.ENVIRONMENT}-{name}"
        return full_name.lower() if lower else full_name
