# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['WorkloadArgs', 'Workload']

@pulumi.input_type
class WorkloadArgs:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[int]] = None,
                 entity_guids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 entity_search_queries: Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Workload resource.
        :param pulumi.Input[int] account_id: The New Relic account ID where you want to create the workload.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entity_guids: A list of entity GUIDs manually assigned to this workload.
        :param pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]] entity_search_queries: A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        :param pulumi.Input[str] name: The workload's name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] scope_account_ids: A list of account IDs that will be used to get entities from.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if entity_guids is not None:
            pulumi.set(__self__, "entity_guids", entity_guids)
        if entity_search_queries is not None:
            pulumi.set(__self__, "entity_search_queries", entity_search_queries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scope_account_ids is not None:
            pulumi.set(__self__, "scope_account_ids", scope_account_ids)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        The New Relic account ID where you want to create the workload.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="entityGuids")
    def entity_guids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of entity GUIDs manually assigned to this workload.
        """
        return pulumi.get(self, "entity_guids")

    @entity_guids.setter
    def entity_guids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "entity_guids", value)

    @property
    @pulumi.getter(name="entitySearchQueries")
    def entity_search_queries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]]]:
        """
        A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        """
        return pulumi.get(self, "entity_search_queries")

    @entity_search_queries.setter
    def entity_search_queries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]]]):
        pulumi.set(self, "entity_search_queries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The workload's name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="scopeAccountIds")
    def scope_account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of account IDs that will be used to get entities from.
        """
        return pulumi.get(self, "scope_account_ids")

    @scope_account_ids.setter
    def scope_account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "scope_account_ids", value)


@pulumi.input_type
class _WorkloadState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[int]] = None,
                 composite_entity_search_query: Optional[pulumi.Input[str]] = None,
                 entity_guids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 entity_search_queries: Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]]] = None,
                 guid: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permalink: Optional[pulumi.Input[str]] = None,
                 scope_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 workload_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Workload resources.
        :param pulumi.Input[int] account_id: The New Relic account ID where you want to create the workload.
        :param pulumi.Input[str] composite_entity_search_query: The composite query used to compose a dynamic workload.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entity_guids: A list of entity GUIDs manually assigned to this workload.
        :param pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]] entity_search_queries: A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        :param pulumi.Input[str] guid: The unique entity identifier of the workload in New Relic.
        :param pulumi.Input[str] name: The workload's name.
        :param pulumi.Input[str] permalink: The URL of the workload.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] scope_account_ids: A list of account IDs that will be used to get entities from.
        :param pulumi.Input[int] workload_id: The unique entity identifier of the workload.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if composite_entity_search_query is not None:
            pulumi.set(__self__, "composite_entity_search_query", composite_entity_search_query)
        if entity_guids is not None:
            pulumi.set(__self__, "entity_guids", entity_guids)
        if entity_search_queries is not None:
            pulumi.set(__self__, "entity_search_queries", entity_search_queries)
        if guid is not None:
            pulumi.set(__self__, "guid", guid)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if permalink is not None:
            pulumi.set(__self__, "permalink", permalink)
        if scope_account_ids is not None:
            pulumi.set(__self__, "scope_account_ids", scope_account_ids)
        if workload_id is not None:
            pulumi.set(__self__, "workload_id", workload_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[int]]:
        """
        The New Relic account ID where you want to create the workload.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="compositeEntitySearchQuery")
    def composite_entity_search_query(self) -> Optional[pulumi.Input[str]]:
        """
        The composite query used to compose a dynamic workload.
        """
        return pulumi.get(self, "composite_entity_search_query")

    @composite_entity_search_query.setter
    def composite_entity_search_query(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "composite_entity_search_query", value)

    @property
    @pulumi.getter(name="entityGuids")
    def entity_guids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of entity GUIDs manually assigned to this workload.
        """
        return pulumi.get(self, "entity_guids")

    @entity_guids.setter
    def entity_guids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "entity_guids", value)

    @property
    @pulumi.getter(name="entitySearchQueries")
    def entity_search_queries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]]]:
        """
        A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        """
        return pulumi.get(self, "entity_search_queries")

    @entity_search_queries.setter
    def entity_search_queries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkloadEntitySearchQueryArgs']]]]):
        pulumi.set(self, "entity_search_queries", value)

    @property
    @pulumi.getter
    def guid(self) -> Optional[pulumi.Input[str]]:
        """
        The unique entity identifier of the workload in New Relic.
        """
        return pulumi.get(self, "guid")

    @guid.setter
    def guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The workload's name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permalink(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the workload.
        """
        return pulumi.get(self, "permalink")

    @permalink.setter
    def permalink(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permalink", value)

    @property
    @pulumi.getter(name="scopeAccountIds")
    def scope_account_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        A list of account IDs that will be used to get entities from.
        """
        return pulumi.get(self, "scope_account_ids")

    @scope_account_ids.setter
    def scope_account_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "scope_account_ids", value)

    @property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique entity identifier of the workload.
        """
        return pulumi.get(self, "workload_id")

    @workload_id.setter
    def workload_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "workload_id", value)


class Workload(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 entity_guids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 entity_search_queries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Use this resource to create, update, and delete a New Relic One workload.

        A New Relic User API key is required to provision this resource.  Set the `api_key`
        attribute in the `provider` block or the `NEW_RELIC_API_KEY` environment
        variable with your User API key.

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

        ## Import

        New Relic One workloads can be imported using a concatenated string of the format

        `<account_id>:<workload_id>:<guid>`, e.g. bash

        ```sh
         $ pulumi import newrelic:plugins/workload:Workload foo 12345678:1456:MjUyMDUyOHxBUE18QVBRTElDQVRJT058MjE1MDM3Nzk1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: The New Relic account ID where you want to create the workload.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entity_guids: A list of entity GUIDs manually assigned to this workload.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]] entity_search_queries: A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        :param pulumi.Input[str] name: The workload's name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] scope_account_ids: A list of account IDs that will be used to get entities from.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[WorkloadArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to create, update, and delete a New Relic One workload.

        A New Relic User API key is required to provision this resource.  Set the `api_key`
        attribute in the `provider` block or the `NEW_RELIC_API_KEY` environment
        variable with your User API key.

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

        ## Import

        New Relic One workloads can be imported using a concatenated string of the format

        `<account_id>:<workload_id>:<guid>`, e.g. bash

        ```sh
         $ pulumi import newrelic:plugins/workload:Workload foo 12345678:1456:MjUyMDUyOHxBUE18QVBRTElDQVRJT058MjE1MDM3Nzk1
        ```

        :param str resource_name: The name of the resource.
        :param WorkloadArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 entity_guids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 entity_search_queries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
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
            __props__ = WorkloadArgs.__new__(WorkloadArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["entity_guids"] = entity_guids
            __props__.__dict__["entity_search_queries"] = entity_search_queries
            __props__.__dict__["name"] = name
            __props__.__dict__["scope_account_ids"] = scope_account_ids
            __props__.__dict__["composite_entity_search_query"] = None
            __props__.__dict__["guid"] = None
            __props__.__dict__["permalink"] = None
            __props__.__dict__["workload_id"] = None
        super(Workload, __self__).__init__(
            'newrelic:plugins/workload:Workload',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            composite_entity_search_query: Optional[pulumi.Input[str]] = None,
            entity_guids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            entity_search_queries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]]] = None,
            guid: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            permalink: Optional[pulumi.Input[str]] = None,
            scope_account_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            workload_id: Optional[pulumi.Input[int]] = None) -> 'Workload':
        """
        Get an existing Workload resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: The New Relic account ID where you want to create the workload.
        :param pulumi.Input[str] composite_entity_search_query: The composite query used to compose a dynamic workload.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entity_guids: A list of entity GUIDs manually assigned to this workload.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkloadEntitySearchQueryArgs']]]] entity_search_queries: A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        :param pulumi.Input[str] guid: The unique entity identifier of the workload in New Relic.
        :param pulumi.Input[str] name: The workload's name.
        :param pulumi.Input[str] permalink: The URL of the workload.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] scope_account_ids: A list of account IDs that will be used to get entities from.
        :param pulumi.Input[int] workload_id: The unique entity identifier of the workload.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkloadState.__new__(_WorkloadState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["composite_entity_search_query"] = composite_entity_search_query
        __props__.__dict__["entity_guids"] = entity_guids
        __props__.__dict__["entity_search_queries"] = entity_search_queries
        __props__.__dict__["guid"] = guid
        __props__.__dict__["name"] = name
        __props__.__dict__["permalink"] = permalink
        __props__.__dict__["scope_account_ids"] = scope_account_ids
        __props__.__dict__["workload_id"] = workload_id
        return Workload(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        The New Relic account ID where you want to create the workload.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="compositeEntitySearchQuery")
    def composite_entity_search_query(self) -> pulumi.Output[str]:
        """
        The composite query used to compose a dynamic workload.
        """
        return pulumi.get(self, "composite_entity_search_query")

    @property
    @pulumi.getter(name="entityGuids")
    def entity_guids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of entity GUIDs manually assigned to this workload.
        """
        return pulumi.get(self, "entity_guids")

    @property
    @pulumi.getter(name="entitySearchQueries")
    def entity_search_queries(self) -> pulumi.Output[Optional[Sequence['outputs.WorkloadEntitySearchQuery']]]:
        """
        A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.
        """
        return pulumi.get(self, "entity_search_queries")

    @property
    @pulumi.getter
    def guid(self) -> pulumi.Output[str]:
        """
        The unique entity identifier of the workload in New Relic.
        """
        return pulumi.get(self, "guid")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The workload's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permalink(self) -> pulumi.Output[str]:
        """
        The URL of the workload.
        """
        return pulumi.get(self, "permalink")

    @property
    @pulumi.getter(name="scopeAccountIds")
    def scope_account_ids(self) -> pulumi.Output[Sequence[int]]:
        """
        A list of account IDs that will be used to get entities from.
        """
        return pulumi.get(self, "scope_account_ids")

    @property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> pulumi.Output[int]:
        """
        The unique entity identifier of the workload.
        """
        return pulumi.get(self, "workload_id")

