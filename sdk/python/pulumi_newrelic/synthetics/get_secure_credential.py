# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetSecureCredentialResult',
    'AwaitableGetSecureCredentialResult',
    'get_secure_credential',
]

@pulumi.output_type
class GetSecureCredentialResult:
    """
    A collection of values returned by getSecureCredential.
    """
    def __init__(__self__, created_at=None, description=None, id=None, key=None, last_updated=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if last_updated and not isinstance(last_updated, str):
            raise TypeError("Expected argument 'last_updated' to be a str")
        pulumi.set(__self__, "last_updated", last_updated)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time the secure credential was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The secure credential's description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> str:
        """
        The time the secure credential was last updated.
        """
        return pulumi.get(self, "last_updated")


class AwaitableGetSecureCredentialResult(GetSecureCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecureCredentialResult(
            created_at=self.created_at,
            description=self.description,
            id=self.id,
            key=self.key,
            last_updated=self.last_updated)


def get_secure_credential(key: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecureCredentialResult:
    """
    Use this data source to get information about a specific Synthetics secure credential in New Relic that already exists.

    Note that the secure credential's value is not returned as an attribute for security reasons.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_newrelic as newrelic

    foo = newrelic.synthetics.get_secure_credential(key="MY_KEY")
    ```


    :param str key: The secure credential's key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.
    """
    __args__ = dict()
    __args__['key'] = key
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('newrelic:synthetics/getSecureCredential:getSecureCredential', __args__, opts=opts, typ=GetSecureCredentialResult).value

    return AwaitableGetSecureCredentialResult(
        created_at=__ret__.created_at,
        description=__ret__.description,
        id=__ret__.id,
        key=__ret__.key,
        last_updated=__ret__.last_updated)
