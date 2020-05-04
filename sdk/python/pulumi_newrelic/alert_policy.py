# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class AlertPolicy(pulumi.CustomResource):
    channel_ids: pulumi.Output[list]
    """
    An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result
    in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs cannot be
    imported via terraform import.
    """
    created_at: pulumi.Output[str]
    """
    **DEPRECATED:** The time the policy was created.
    """
    incident_preference: pulumi.Output[str]
    """
    The rollup strategy for the policy.  Options include: `PER_POLICY`, `PER_CONDITION`, or `PER_CONDITION_AND_TARGET`.  The default is `PER_POLICY`.
    """
    name: pulumi.Output[str]
    """
    The name of the policy.
    """
    updated_at: pulumi.Output[str]
    """
    **DEPRECATED:** The time the policy was last updated.
    """
    def __init__(__self__, resource_name, opts=None, channel_ids=None, incident_preference=None, name=None, __props__=None, __name__=None, __opts__=None):
        """
        Use this resource to create and manage New Relic alert policies.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] channel_ids: An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result
               in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs cannot be
               imported via terraform import.
        :param pulumi.Input[str] incident_preference: The rollup strategy for the policy.  Options include: `PER_POLICY`, `PER_CONDITION`, or `PER_CONDITION_AND_TARGET`.  The default is `PER_POLICY`.
        :param pulumi.Input[str] name: The name of the policy.
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

            __props__['channel_ids'] = channel_ids
            __props__['incident_preference'] = incident_preference
            __props__['name'] = name
            __props__['created_at'] = None
            __props__['updated_at'] = None
        super(AlertPolicy, __self__).__init__(
            'newrelic:index/alertPolicy:AlertPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, channel_ids=None, created_at=None, incident_preference=None, name=None, updated_at=None):
        """
        Get an existing AlertPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] channel_ids: An array of channel IDs (integers) to assign to the policy. Adding or removing channel IDs from this array will result
               in a new alert policy resource being created and the old one being destroyed. Also note that channel IDs cannot be
               imported via terraform import.
        :param pulumi.Input[str] created_at: **DEPRECATED:** The time the policy was created.
        :param pulumi.Input[str] incident_preference: The rollup strategy for the policy.  Options include: `PER_POLICY`, `PER_CONDITION`, or `PER_CONDITION_AND_TARGET`.  The default is `PER_POLICY`.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] updated_at: **DEPRECATED:** The time the policy was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["channel_ids"] = channel_ids
        __props__["created_at"] = created_at
        __props__["incident_preference"] = incident_preference
        __props__["name"] = name
        __props__["updated_at"] = updated_at
        return AlertPolicy(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

