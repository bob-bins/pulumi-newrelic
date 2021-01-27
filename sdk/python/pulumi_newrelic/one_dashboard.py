# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['OneDashboard']


class OneDashboard(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        **NOTE:** This feature is currently in **CLOSED BETA**, and will **NOT WORK** for most New Relic customers and is subject to **BREAKING CHANGES**.

        Use this resource to create and manage New Relic One dashboards.

        ## Example Usage
        ## Additional Examples

        ## Import

        New Relic dashboards can be imported using their GUID, e.g.

        ```sh
         $ pulumi import newrelic:index/oneDashboard:OneDashboard my_dashboard <Dashboard GUID>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] description: Brief text describing the dashboard.
        :param pulumi.Input[str] name: The title of the dashboard.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]] pages: A nested block that describes a page. See Nested page blocks below for details.
        :param pulumi.Input[str] permissions: Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
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

            __props__['account_id'] = account_id
            __props__['description'] = description
            __props__['name'] = name
            if pages is None and not opts.urn:
                raise TypeError("Missing required property 'pages'")
            __props__['pages'] = pages
            __props__['permissions'] = permissions
            __props__['guid'] = None
            __props__['permalink'] = None
        super(OneDashboard, __self__).__init__(
            'newrelic:index/oneDashboard:OneDashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            guid: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]]] = None,
            permalink: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[str]] = None) -> 'OneDashboard':
        """
        Get an existing OneDashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        :param pulumi.Input[str] description: Brief text describing the dashboard.
        :param pulumi.Input[str] guid: The unique entity identifier of the dashboard page in New Relic.
        :param pulumi.Input[str] name: The title of the dashboard.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OneDashboardPageArgs']]]] pages: A nested block that describes a page. See Nested page blocks below for details.
        :param pulumi.Input[str] permalink: The URL for viewing the dashboard.
        :param pulumi.Input[str] permissions: Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["description"] = description
        __props__["guid"] = guid
        __props__["name"] = name
        __props__["pages"] = pages
        __props__["permalink"] = permalink
        __props__["permissions"] = permissions
        return OneDashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Brief text describing the dashboard.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def guid(self) -> pulumi.Output[str]:
        """
        The unique entity identifier of the dashboard page in New Relic.
        """
        return pulumi.get(self, "guid")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The title of the dashboard.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pages(self) -> pulumi.Output[Sequence['outputs.OneDashboardPage']]:
        """
        A nested block that describes a page. See Nested page blocks below for details.
        """
        return pulumi.get(self, "pages")

    @property
    @pulumi.getter
    def permalink(self) -> pulumi.Output[str]:
        """
        The URL for viewing the dashboard.
        """
        return pulumi.get(self, "permalink")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[str]]:
        """
        Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.
        """
        return pulumi.get(self, "permissions")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
