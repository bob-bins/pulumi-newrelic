# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['MonitorScript']


class MonitorScript(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 monitor_id: Optional[pulumi.Input[str]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Use this resource to update a synthetics monitor script in New Relic.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] monitor_id: The ID of the monitor to attach the script to.
        :param pulumi.Input[str] text: The plaintext representing the monitor script.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if monitor_id is None:
                raise TypeError("Missing required property 'monitor_id'")
            __props__['monitor_id'] = monitor_id
            if text is None:
                raise TypeError("Missing required property 'text'")
            __props__['text'] = text
        super(MonitorScript, __self__).__init__(
            'newrelic:synthetics/monitorScript:MonitorScript',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            monitor_id: Optional[pulumi.Input[str]] = None,
            text: Optional[pulumi.Input[str]] = None) -> 'MonitorScript':
        """
        Get an existing MonitorScript resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] monitor_id: The ID of the monitor to attach the script to.
        :param pulumi.Input[str] text: The plaintext representing the monitor script.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["monitor_id"] = monitor_id
        __props__["text"] = text
        return MonitorScript(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="monitorId")
    def monitor_id(self) -> pulumi.Output[str]:
        """
        The ID of the monitor to attach the script to.
        """
        return pulumi.get(self, "monitor_id")

    @property
    @pulumi.getter
    def text(self) -> pulumi.Output[str]:
        """
        The plaintext representing the monitor script.
        """
        return pulumi.get(self, "text")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

