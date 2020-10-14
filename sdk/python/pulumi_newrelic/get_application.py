# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
]

@pulumi.output_type
class GetApplicationResult:
    """
    A collection of values returned by getApplication.
    """
    def __init__(__self__, host_ids=None, id=None, instance_ids=None, name=None):
        if host_ids and not isinstance(host_ids, list):
            raise TypeError("Expected argument 'host_ids' to be a list")
        pulumi.set(__self__, "host_ids", host_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_ids and not isinstance(instance_ids, list):
            raise TypeError("Expected argument 'instance_ids' to be a list")
        pulumi.set(__self__, "instance_ids", instance_ids)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="hostIds")
    def host_ids(self) -> Sequence[int]:
        """
        A list of host IDs associated with the application.
        """
        return pulumi.get(self, "host_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> Sequence[int]:
        """
        A list of instance IDs associated with the application.
        """
        return pulumi.get(self, "instance_ids")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            host_ids=self.host_ids,
            id=self.id,
            instance_ids=self.instance_ids,
            name=self.name)


def get_application(name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    #### DEPRECATED! Use at your own risk. Use the `getEntity` data source instead. This feature may be removed in the next major release.

    Use this data source to get information about a specific application in New Relic that already exists.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_newrelic as newrelic

    app = newrelic.get_application(name="my-app")
    foo_alert_policy = newrelic.AlertPolicy("fooAlertPolicy")
    foo_alert_condition = newrelic.AlertCondition("fooAlertCondition",
        policy_id=foo_alert_policy.id,
        type="apm_app_metric",
        entities=[app.id],
        metric="apdex",
        runbook_url="https://www.example.com",
        terms=[newrelic.AlertConditionTermArgs(
            duration=5,
            operator="below",
            priority="critical",
            threshold=0.75,
            time_function="all",
        )])
    ```


    :param str name: The name of the application in New Relic.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('newrelic:index/getApplication:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        host_ids=__ret__.host_ids,
        id=__ret__.id,
        instance_ids=__ret__.instance_ids,
        name=__ret__.name)
