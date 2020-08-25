# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Workload']


class Workload(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[float]] = None,
                 entity_guids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 entity_search_queries: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope_account_ids: Optional[pulumi.Input[List[pulumi.Input[float]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Use this resource to create, update, and delete a New Relic One workload.

        A New Relic Personal API key is required to provision this resource.  Set the `api_key`
        attribute in the `provider` block or the `NEW_RELIC_API_KEY` environment
        variable with your Personal API key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_newrelic as newrelic

        foo = newrelic.plugins.Workload("foo",
            account_id=12345678,
            entity_guids=["MjUyMDUyOHxBUE18QVBQTElDQVRJT058MjE1MDM3Nzk1"],
            entity_search_queries=[newrelic.plugins.WorkloadEntitySearchQueryArgs(
                query="name like 'Example application'",
            )],
            scope_account_ids=[12345678])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] account_id: The New Relic account ID where you want to create the workload.
        :param pulumi.Input[List[pulumi.Input[str]]] entity_guids: A list of entity GUIDs manually assigned to this workload.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]] entity_search_queries: A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        :param pulumi.Input[str] name: The workload's name.
        :param pulumi.Input[List[pulumi.Input[float]]] scope_account_ids: A list of account IDs that will be used to get entities from.
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
            __props__['entity_guids'] = entity_guids
            __props__['entity_search_queries'] = entity_search_queries
            __props__['name'] = name
            __props__['scope_account_ids'] = scope_account_ids
            __props__['composite_entity_search_query'] = None
            __props__['guid'] = None
            __props__['permalink'] = None
            __props__['workload_id'] = None
        super(Workload, __self__).__init__(
            'newrelic:plugins/workload:Workload',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[float]] = None,
            composite_entity_search_query: Optional[pulumi.Input[str]] = None,
            entity_guids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            entity_search_queries: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]]] = None,
            guid: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            permalink: Optional[pulumi.Input[str]] = None,
            scope_account_ids: Optional[pulumi.Input[List[pulumi.Input[float]]]] = None,
            workload_id: Optional[pulumi.Input[float]] = None) -> 'Workload':
        """
        Get an existing Workload resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] account_id: The New Relic account ID where you want to create the workload.
        :param pulumi.Input[str] composite_entity_search_query: The composite query used to compose a dynamic workload.
        :param pulumi.Input[List[pulumi.Input[str]]] entity_guids: A list of entity GUIDs manually assigned to this workload.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]] entity_search_queries: A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        :param pulumi.Input[str] guid: The unique entity identifier of the workload in New Relic.
        :param pulumi.Input[str] name: The workload's name.
        :param pulumi.Input[str] permalink: The URL of the workload.
        :param pulumi.Input[List[pulumi.Input[float]]] scope_account_ids: A list of account IDs that will be used to get entities from.
        :param pulumi.Input[float] workload_id: The unique entity identifier of the workload.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["composite_entity_search_query"] = composite_entity_search_query
        __props__["entity_guids"] = entity_guids
        __props__["entity_search_queries"] = entity_search_queries
        __props__["guid"] = guid
        __props__["name"] = name
        __props__["permalink"] = permalink
        __props__["scope_account_ids"] = scope_account_ids
        __props__["workload_id"] = workload_id
        return Workload(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> float:
        """
        The New Relic account ID where you want to create the workload.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="compositeEntitySearchQuery")
    def composite_entity_search_query(self) -> str:
        """
        The composite query used to compose a dynamic workload.
        """
        return pulumi.get(self, "composite_entity_search_query")

    @property
    @pulumi.getter(name="entityGuids")
    def entity_guids(self) -> List[str]:
        """
        A list of entity GUIDs manually assigned to this workload.
        """
        return pulumi.get(self, "entity_guids")

    @property
    @pulumi.getter(name="entitySearchQueries")
    def entity_search_queries(self) -> Optional[List['outputs.WorkloadEntitySearchQuery']]:
        """
        A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        """
        return pulumi.get(self, "entity_search_queries")

    @property
    @pulumi.getter
    def guid(self) -> str:
        """
        The unique entity identifier of the workload in New Relic.
        """
        return pulumi.get(self, "guid")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The workload's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permalink(self) -> str:
        """
        The URL of the workload.
        """
        return pulumi.get(self, "permalink")

    @property
    @pulumi.getter(name="scopeAccountIds")
    def scope_account_ids(self) -> List[float]:
        """
        A list of account IDs that will be used to get entities from.
        """
        return pulumi.get(self, "scope_account_ids")

    @property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> float:
        """
        The unique entity identifier of the workload.
        """
        return pulumi.get(self, "workload_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

