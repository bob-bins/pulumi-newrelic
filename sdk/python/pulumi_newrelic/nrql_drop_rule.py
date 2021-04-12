# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = ['NrqlDropRuleArgs', 'NrqlDropRule']

@pulumi.input_type
class NrqlDropRuleArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 nrql: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NrqlDropRule resource.
        :param pulumi.Input[str] action: An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).
        :param pulumi.Input[str] nrql: A NRQL string that specifies what data types to drop.
        :param pulumi.Input[int] account_id: Account where the drop rule will be put. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] description: The description of the drop rule.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "nrql", nrql)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def nrql(self) -> pulumi.Input[str]:
        """
        A NRQL string that specifies what data types to drop.
        """
        return pulumi.get(self, "nrql")

    @nrql.setter
    def nrql(self, value: pulumi.Input[str]):
        pulumi.set(self, "nrql", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        Account where the drop rule will be put. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the drop rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class NrqlDropRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 nrql: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        New Relic NRQL drop rules can be imported using a concatenated string of the format

        `<account_id>:<rule_id>`, e.g. bash

        ```sh
         $ pulumi import newrelic:index/nrqlDropRule:NrqlDropRule foo 12345:34567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Account where the drop rule will be put. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] action: An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).
        :param pulumi.Input[str] description: The description of the drop rule.
        :param pulumi.Input[str] nrql: A NRQL string that specifies what data types to drop.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NrqlDropRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        New Relic NRQL drop rules can be imported using a concatenated string of the format

        `<account_id>:<rule_id>`, e.g. bash

        ```sh
         $ pulumi import newrelic:index/nrqlDropRule:NrqlDropRule foo 12345:34567
        ```

        :param str resource_name: The name of the resource.
        :param NrqlDropRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NrqlDropRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 nrql: Optional[pulumi.Input[str]] = None,
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
            __props__ = dict()

            __props__['account_id'] = account_id
            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__['action'] = action
            __props__['description'] = description
            if nrql is None and not opts.urn:
                raise TypeError("Missing required property 'nrql'")
            __props__['nrql'] = nrql
            __props__['rule_id'] = None
        super(NrqlDropRule, __self__).__init__(
            'newrelic:index/nrqlDropRule:NrqlDropRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            action: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            nrql: Optional[pulumi.Input[str]] = None,
            rule_id: Optional[pulumi.Input[str]] = None) -> 'NrqlDropRule':
        """
        Get an existing NrqlDropRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Account where the drop rule will be put. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] action: An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).
        :param pulumi.Input[str] description: The description of the drop rule.
        :param pulumi.Input[str] nrql: A NRQL string that specifies what data types to drop.
        :param pulumi.Input[str] rule_id: The id, uniquely identifying the rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["action"] = action
        __props__["description"] = description
        __props__["nrql"] = nrql
        __props__["rule_id"] = rule_id
        return NrqlDropRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        Account where the drop rule will be put. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the drop rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def nrql(self) -> pulumi.Output[str]:
        """
        A NRQL string that specifies what data types to drop.
        """
        return pulumi.get(self, "nrql")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Output[str]:
        """
        The id, uniquely identifying the rule.
        """
        return pulumi.get(self, "rule_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

