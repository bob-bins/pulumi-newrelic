# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Provider(pulumi.ProviderResource):
    def __init__(__self__, resource_name, opts=None, api_key=None, api_url=None, cacert_file=None, infra_api_url=None, insecure_skip_verify=None, insights_account_id=None, insights_insert_key=None, insights_insert_url=None, insights_query_key=None, insights_query_url=None, synthetics_api_url=None, __props__=None, __name__=None, __opts__=None):
        """
        The provider type for the newrelic package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/index.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if api_key is None:
                api_key = utilities.get_env('NEWRELIC_API_KEY')
            __props__['api_key'] = api_key
            if api_url is None:
                api_url = (utilities.get_env('NEWRELIC_API_URL') or 'https://api.newrelic.com/v2')
            __props__['api_url'] = api_url
            if cacert_file is None:
                cacert_file = utilities.get_env('NEWRELIC_API_CACERT')
            __props__['cacert_file'] = cacert_file
            if infra_api_url is None:
                infra_api_url = (utilities.get_env('NEWRELIC_INFRA_API_URL') or 'https://infra-api.newrelic.com/v2')
            __props__['infra_api_url'] = infra_api_url
            if insecure_skip_verify is None:
                insecure_skip_verify = utilities.get_env_bool('NEWRELIC_API_SKIP_VERIFY')
            __props__['insecure_skip_verify'] = pulumi.Output.from_input(insecure_skip_verify).apply(json.dumps) if insecure_skip_verify is not None else None
            if insights_account_id is None:
                insights_account_id = utilities.get_env('NEWRELIC_INSIGHTS_ACCOUNT_ID')
            __props__['insights_account_id'] = insights_account_id
            if insights_insert_key is None:
                insights_insert_key = utilities.get_env('NEWRELIC_INSIGHTS_INSERT_KEY')
            __props__['insights_insert_key'] = insights_insert_key
            if insights_insert_url is None:
                insights_insert_url = (utilities.get_env('NEWRELIC_INSIGHTS_INSERT_URL') or 'https://insights-collector.newrelic.com/v1/accounts')
            __props__['insights_insert_url'] = insights_insert_url
            if insights_query_key is None:
                insights_query_key = utilities.get_env('NEWRELIC_INSIGHTS_QUERY_KEY')
            __props__['insights_query_key'] = insights_query_key
            if insights_query_url is None:
                insights_query_url = (utilities.get_env('NEWRELIC_INSIGHTS_QUERY_URL') or 'https://insights-api.newrelic.com/v1/accounts')
            __props__['insights_query_url'] = insights_query_url
            if synthetics_api_url is None:
                synthetics_api_url = (utilities.get_env('NEWRELIC_SYNTHETICS_API_URL') or 'https://synthetics.newrelic.com/synthetics/api/v3')
            __props__['synthetics_api_url'] = synthetics_api_url
        super(Provider, __self__).__init__(
            'newrelic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get an existing Provider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/index.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        return Provider(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

