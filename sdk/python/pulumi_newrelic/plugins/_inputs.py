# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'AlertConditionTermArgs',
    'WorkloadEntitySearchQueryArgs',
]

@pulumi.input_type
class AlertConditionTermArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[int],
                 threshold: pulumi.Input[float],
                 time_function: pulumi.Input[str],
                 operator: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "time_function", time_function)
        if operator is not None:
            pulumi.set(__self__, "operator", operator)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[int]:
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[int]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[float]:
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: pulumi.Input[float]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="timeFunction")
    def time_function(self) -> pulumi.Input[str]:
        return pulumi.get(self, "time_function")

    @time_function.setter
    def time_function(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_function", value)

    @property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)


@pulumi.input_type
class WorkloadEntitySearchQueryArgs:
    def __init__(__self__, *,
                 query: pulumi.Input[str]):
        """
        :param pulumi.Input[str] query: The query.
        """
        pulumi.set(__self__, "query", query)

    @property
    @pulumi.getter
    def query(self) -> pulumi.Input[str]:
        """
        The query.
        """
        return pulumi.get(self, "query")

    @query.setter
    def query(self, value: pulumi.Input[str]):
        pulumi.set(self, "query", value)


