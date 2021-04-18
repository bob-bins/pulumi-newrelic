# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AlertChannelArgs', 'AlertChannel']

@pulumi.input_type
class AlertChannelArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 config: Optional[pulumi.Input['AlertChannelConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AlertChannel resource.
        :param pulumi.Input[str] type: The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
        :param pulumi.Input['AlertChannelConfigArgs'] config: A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
        :param pulumi.Input[str] name: The name of the channel.
        """
        pulumi.set(__self__, "type", type)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['AlertChannelConfigArgs']]:
        """
        A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['AlertChannelConfigArgs']]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AlertChannelState:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input['AlertChannelConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AlertChannel resources.
        :param pulumi.Input['AlertChannelConfigArgs'] config: A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
        :param pulumi.Input[str] name: The name of the channel.
        :param pulumi.Input[str] type: The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
        """
        if config is not None:
            pulumi.set(__self__, "config", config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['AlertChannelConfigArgs']]:
        """
        A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['AlertChannelConfigArgs']]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class AlertChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['AlertChannelConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Use this resource to create and manage New Relic alert channels.

        ## Example Usage
        ### Email
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                include_json_attachment="true",
                recipients="foo@example.com",
            ),
            type="email")
        ```
        ### Slack
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                channel="example-alerts-channel",
                url="https://hooks.slack.com/services/XXXXXXX/XXXXXXX/XXXXXXXXXX",
            ),
            type="slack")
        ```
        ### OpsGenie
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                api_key="abc123",
                recipients="user1@domain.com, user2@domain.com",
                tags="tag1, tag2",
                teams="team1, team2",
            ),
            type="opsgenie")
        ```
        ### PagerDuty
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                service_key="abc123",
            ),
            type="pagerduty")
        ```
        ### VictorOps
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                key="abc123",
                route_key="/example",
            ),
            type="victorops")
        ```
        ### Webhook
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            type="webhook",
            config=newrelic.AlertChannelConfigArgs(
                base_url="http://www.test.com",
                payload_type="application/json",
                payload={
                    "condition_name": "$CONDITION_NAME",
                    "policy_name": "$POLICY_NAME",
                },
                headers={
                    "header1": value1,
                    "header2": value2,
                },
            ))
        ```
        ### Webhook with complex payload
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                base_url="http://www.test.com",
                payload_string=\"\"\"{
          "my_custom_values": {
            "condition_name": "$CONDITION_NAME",
            "policy_name": "$POLICY_NAME"
          }
        }

        \"\"\",
                payload_type="application/json",
            ),
            type="webhook")
        ```

        ## Import

        Alert channels can be imported using the `id`, e.g. bash

        ```sh
         $ pulumi import newrelic:index/alertChannel:AlertChannel main <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AlertChannelConfigArgs']] config: A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
        :param pulumi.Input[str] name: The name of the channel.
        :param pulumi.Input[str] type: The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to create and manage New Relic alert channels.

        ## Example Usage
        ### Email
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                include_json_attachment="true",
                recipients="foo@example.com",
            ),
            type="email")
        ```
        ### Slack
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                channel="example-alerts-channel",
                url="https://hooks.slack.com/services/XXXXXXX/XXXXXXX/XXXXXXXXXX",
            ),
            type="slack")
        ```
        ### OpsGenie
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                api_key="abc123",
                recipients="user1@domain.com, user2@domain.com",
                tags="tag1, tag2",
                teams="team1, team2",
            ),
            type="opsgenie")
        ```
        ### PagerDuty
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                service_key="abc123",
            ),
            type="pagerduty")
        ```
        ### VictorOps
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                key="abc123",
                route_key="/example",
            ),
            type="victorops")
        ```
        ### Webhook
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            type="webhook",
            config=newrelic.AlertChannelConfigArgs(
                base_url="http://www.test.com",
                payload_type="application/json",
                payload={
                    "condition_name": "$CONDITION_NAME",
                    "policy_name": "$POLICY_NAME",
                },
                headers={
                    "header1": value1,
                    "header2": value2,
                },
            ))
        ```
        ### Webhook with complex payload
        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.AlertChannel("foo",
            config=newrelic.AlertChannelConfigArgs(
                base_url="http://www.test.com",
                payload_string=\"\"\"{
          "my_custom_values": {
            "condition_name": "$CONDITION_NAME",
            "policy_name": "$POLICY_NAME"
          }
        }

        \"\"\",
                payload_type="application/json",
            ),
            type="webhook")
        ```

        ## Import

        Alert channels can be imported using the `id`, e.g. bash

        ```sh
         $ pulumi import newrelic:index/alertChannel:AlertChannel main <id>
        ```

        :param str resource_name: The name of the resource.
        :param AlertChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['AlertChannelConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
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
            __props__ = AlertChannelArgs.__new__(AlertChannelArgs)

            __props__.__dict__["config"] = config
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(AlertChannel, __self__).__init__(
            'newrelic:index/alertChannel:AlertChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[pulumi.InputType['AlertChannelConfigArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'AlertChannel':
        """
        Get an existing AlertChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AlertChannelConfigArgs']] config: A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
        :param pulumi.Input[str] name: The name of the channel.
        :param pulumi.Input[str] type: The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AlertChannelState.__new__(_AlertChannelState)

        __props__.__dict__["config"] = config
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        return AlertChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional['outputs.AlertChannelConfig']]:
        """
        A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the channel.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
        """
        return pulumi.get(self, "type")

