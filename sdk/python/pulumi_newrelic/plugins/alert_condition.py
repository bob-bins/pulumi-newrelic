# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class AlertCondition(pulumi.CustomResource):
    enabled: pulumi.Output[bool]
    entities: pulumi.Output[list]
    metric: pulumi.Output[str]
    """
    The metric field accepts parameters based on the `type` set.
    """
    metric_description: pulumi.Output[str]
    name: pulumi.Output[str]
    """
    The title of the condition. Must be between 1 and 64 characters, inclusive.
    """
    plugin_guid: pulumi.Output[str]
    """
    The GUID of the plugin which produces the metric.
    """
    plugin_id: pulumi.Output[str]
    """
    The ID of the installed plugin instance which produces the metric.
    """
    policy_id: pulumi.Output[float]
    """
    The ID of the policy where this condition should be used.
    """
    runbook_url: pulumi.Output[str]
    """
    Runbook URL to display in notifications.
    """
    terms: pulumi.Output[list]
    """
    A list of terms for this condition. See Terms below for details.
    
      * `duration` (`float`)
      * `operator` (`str`)
      * `priority` (`str`)
      * `threshold` (`float`)
      * `timeFunction` (`str`)
    """
    value_function: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, enabled=None, entities=None, metric=None, metric_description=None, name=None, plugin_guid=None, plugin_id=None, policy_id=None, runbook_url=None, terms=None, value_function=None, __props__=None, __name__=None, __opts__=None):
        """
        ## Terms
        
        The `term` mapping supports the following arguments:
        
          * `duration` - (Required) In minutes, must be in the range of `5` to `120`, inclusive.
          * `operator` - (Optional) `above`, `below`, or `equal`.  Defaults to `equal`.
          * `priority` - (Optional) `critical` or `warning`.  Defaults to `critical`.
          * `threshold` - (Required) Must be 0 or greater.
          * `time_function` - (Required) `all` or `any`.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] metric: The metric field accepts parameters based on the `type` set.
        :param pulumi.Input[str] name: The title of the condition. Must be between 1 and 64 characters, inclusive.
        :param pulumi.Input[str] plugin_guid: The GUID of the plugin which produces the metric.
        :param pulumi.Input[str] plugin_id: The ID of the installed plugin instance which produces the metric.
        :param pulumi.Input[float] policy_id: The ID of the policy where this condition should be used.
        :param pulumi.Input[str] runbook_url: Runbook URL to display in notifications.
        :param pulumi.Input[list] terms: A list of terms for this condition. See Terms below for details.
        
        The **terms** object supports the following:
        
          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `priority` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `timeFunction` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/plugins_alert_condition.html.markdown.
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

            __props__['enabled'] = enabled
            if entities is None:
                raise TypeError("Missing required property 'entities'")
            __props__['entities'] = entities
            if metric is None:
                raise TypeError("Missing required property 'metric'")
            __props__['metric'] = metric
            if metric_description is None:
                raise TypeError("Missing required property 'metric_description'")
            __props__['metric_description'] = metric_description
            __props__['name'] = name
            if plugin_guid is None:
                raise TypeError("Missing required property 'plugin_guid'")
            __props__['plugin_guid'] = plugin_guid
            if plugin_id is None:
                raise TypeError("Missing required property 'plugin_id'")
            __props__['plugin_id'] = plugin_id
            if policy_id is None:
                raise TypeError("Missing required property 'policy_id'")
            __props__['policy_id'] = policy_id
            __props__['runbook_url'] = runbook_url
            if terms is None:
                raise TypeError("Missing required property 'terms'")
            __props__['terms'] = terms
            if value_function is None:
                raise TypeError("Missing required property 'value_function'")
            __props__['value_function'] = value_function
        super(AlertCondition, __self__).__init__(
            'newrelic:plugins/alertCondition:AlertCondition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, enabled=None, entities=None, metric=None, metric_description=None, name=None, plugin_guid=None, plugin_id=None, policy_id=None, runbook_url=None, terms=None, value_function=None):
        """
        Get an existing AlertCondition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] metric: The metric field accepts parameters based on the `type` set.
        :param pulumi.Input[str] name: The title of the condition. Must be between 1 and 64 characters, inclusive.
        :param pulumi.Input[str] plugin_guid: The GUID of the plugin which produces the metric.
        :param pulumi.Input[str] plugin_id: The ID of the installed plugin instance which produces the metric.
        :param pulumi.Input[float] policy_id: The ID of the policy where this condition should be used.
        :param pulumi.Input[str] runbook_url: Runbook URL to display in notifications.
        :param pulumi.Input[list] terms: A list of terms for this condition. See Terms below for details.
        
        The **terms** object supports the following:
        
          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `priority` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `timeFunction` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/plugins_alert_condition.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["enabled"] = enabled
        __props__["entities"] = entities
        __props__["metric"] = metric
        __props__["metric_description"] = metric_description
        __props__["name"] = name
        __props__["plugin_guid"] = plugin_guid
        __props__["plugin_id"] = plugin_id
        __props__["policy_id"] = policy_id
        __props__["runbook_url"] = runbook_url
        __props__["terms"] = terms
        __props__["value_function"] = value_function
        return AlertCondition(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

