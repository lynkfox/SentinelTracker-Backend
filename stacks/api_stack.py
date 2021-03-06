from typing import Dict

import aws_cdk as core
from aws_cdk import NestedStack
from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda
from constructs import Construct

from configurations import ResourceNames
from configurations.common import DeploymentProperties


class ApiStack(NestedStack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        deployment_properties: DeploymentProperties,
        lambda_mapping: Dict[str, aws_lambda.IFunction],
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        props = deployment_properties

        self.backend_api = apigateway.RestApi(
            self,
            ResourceNames.BACKEND_API,
            rest_api_name=props.prefix_name(ResourceNames.BACKEND_API),
            retain_deployments=True,
            deploy_options=apigateway.StageOptions(
                stage_name=props.ENVIRONMENT,
            ),
            policy=None,  # api_policy_document if self.props.IS_PRODUCTION else None
        )

        self.backend_api.apply_removal_policy(core.RemovalPolicy.DESTROY)

        lambda_mapping[ResourceNames.STATISTICS].grant_invoke(iam.ServicePrincipal("apigateway.amazonaws.com"))

        # Not paying for a domain name on this free account :)
        #
        # certificate_arn = "arn for the cert"
        # domain_name = "some.domain.name"
        # domain = apigateway.DomainName(
        #     self, 'Domain',
        #     certificate=certmanager.Certificate.from_certificate_arn(self, "API Cert", certificate_arn=certificate_arn),
        #     domain_name=domain_name,
        # )

        # domain.add_base_path_mapping(
        #     target_api=self.backend_api,
        #     stage=self.backend_api.deployment_stage
        # )

        # route53_host_zone = route53.HostedZone.from_hosted_zone_attributes(
        #     self, "Route53HostZone",
        #     hosted_zone_id=props.HOST_ZONE_ID,
        #     zone_name=props.HOST_ZONE_NAME
        # )

        # route53.ARecord(
        #     self, "DomainAliasRecord",
        #     zone=route53_host_zone,
        #     target=route53.RecordTarget.from_alias(r53_targets.ApiGatewayDomain(domain)),
        #     record_name=domain_name
        # )

        version_one = apigateway.Resource(self, "version_one", parent=self.backend_api.root, path_part="v1")

        statistics = apigateway.Resource(self, "statistics", parent=version_one, path_part="statistics")

        add_entry = apigateway.Resource(self, "add_entry", parent=version_one, path_part="add")

        user = apigateway.Resource(self, "user", parent=version_one, path_part="user")

        response_template = {
            "application/json": """$input.path('$.body')\n"""
            """#if($input.path('$.statusCode').toString().contains("503"))\n"""
            """    #set($context.responseOverride.status = 503)\n"""
            """#end\n"""
            """#if($input.path('$.statusCode').toString().contains("400"))\n"""
            """    #set($context.responseOverride.status = 400)\n"""
            """#end"""
        }

        json_200_method_response = apigateway.MethodResponse(
            status_code="200",
            response_models={"application/json": apigateway.Model.EMPTY_MODEL},
        )
        json_200_integration_response = apigateway.IntegrationResponse(
            status_code="200",
            content_handling=apigateway.ContentHandling.CONVERT_TO_TEXT,
            response_templates=response_template,
        )

        standard_method = apigateway.MethodOptions(api_key_required=False, method_responses=[json_200_method_response])

        statistics.add_proxy(
            default_integration=apigateway.LambdaIntegration(
                handler=lambda_mapping[ResourceNames.STATISTICS],
                proxy=True,
                integration_responses=[json_200_integration_response],
            ),
            default_method_options=standard_method,
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_credentials=True,
            ),
            any_method=True,
        )

        add_entry.add_method(
            "ANY",
            integration=apigateway.LambdaIntegration(
                handler=lambda_mapping[ResourceNames.POST_ENTRY],
                proxy=True,
                integration_responses=[json_200_integration_response],
            ),
            method_responses=[json_200_method_response],
        )

        # add_entry.add_proxy(
        #     default_integration=apigateway.LambdaIntegration(
        #         handler=lambda_mapping[ResourceNames.POST_ENTRY],
        #         proxy=True,
        #         integration_responses=[json_200_integration_response],
        #     ),
        #     default_method_options=standard_method,
        #     default_cors_preflight_options=apigateway.CorsOptions(
        #         allow_origins=apigateway.Cors.ALL_ORIGINS,
        #         allow_credentials=True,
        #     ),
        #     any_method=True,
        # )
