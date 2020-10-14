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

__all__ = ['NrqlAlertCondition']


class NrqlAlertCondition(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[int]] = None,
                 aggregation_window: Optional[pulumi.Input[int]] = None,
                 baseline_direction: Optional[pulumi.Input[str]] = None,
                 close_violations_on_expiration: Optional[pulumi.Input[bool]] = None,
                 critical: Optional[pulumi.Input[pulumi.InputType['NrqlAlertConditionCriticalArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 expected_groups: Optional[pulumi.Input[int]] = None,
                 expiration_duration: Optional[pulumi.Input[int]] = None,
                 fill_option: Optional[pulumi.Input[str]] = None,
                 fill_value: Optional[pulumi.Input[float]] = None,
                 ignore_overlap: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nrql: Optional[pulumi.Input[pulumi.InputType['NrqlAlertConditionNrqlArgs']]] = None,
                 open_violation_on_expiration: Optional[pulumi.Input[bool]] = None,
                 open_violation_on_group_overlap: Optional[pulumi.Input[bool]] = None,
                 policy_id: Optional[pulumi.Input[int]] = None,
                 runbook_url: Optional[pulumi.Input[str]] = None,
                 terms: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NrqlAlertConditionTermArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_function: Optional[pulumi.Input[str]] = None,
                 violation_time_limit: Optional[pulumi.Input[str]] = None,
                 violation_time_limit_seconds: Optional[pulumi.Input[int]] = None,
                 warning: Optional[pulumi.Input[pulumi.InputType['NrqlAlertConditionWarningArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Use this resource to create and manage NRQL alert conditions in New Relic.

        ## Example Usage
        ## NRQL

        The `nrql` block supports the following arguments:

        - `query` - (Required) The NRQL query to execute for the condition.
        - `evaluation_offset` - (Optional*) Represented in minutes and must be within 1-20 minutes (inclusive). NRQL queries are evaluated in one-minute time windows. The start time depends on this value. It's recommended to set this to 3 minutes. An offset of less than 3 minutes will trigger violations sooner, but you may see more false positives and negatives due to data latency. With `evaluation_offset` set to 3 minutes, the NRQL time window applied to your query will be: `SINCE 3 minutes ago UNTIL 2 minutes ago`.<br>
        <small>\***Note**: One of `evaluation_offset` _or_ `since_value` must be set, but not both.</small>

        - `since_value` - (Optional*)  **DEPRECATED:** Use `evaluation_offset` instead. The value to be used in the `SINCE <X> minutes ago` clause for the NRQL query. Must be between 1-20 (inclusive). <br>
        <small>\***Note**: One of `evaluation_offset` _or_ `since_value` must be set, but not both.</small>

        ## Terms

        > **NOTE:** The direct use of the `term` has been deprecated, and users should use `critical` and `warning` instead.  What follows now applies to the named priority attributes for `critical` and `warning`, but for those attributes the priority is not allowed.

        NRQL alert conditions support up to two terms. At least one `term` must have `priority` set to `critical` and the second optional `term` must have `priority` set to `warning`.

        The `term` block the following arguments:

        - `operator` - (Optional) Valid values are `above`, `below`, or `equals` (case insensitive). Defaults to `equals`. Note that when using a `type` of `outlier`, the only valid option here is `above`.
        - `priority` - (Optional) `critical` or `warning`. Defaults to `critical`.
        - `threshold` - (Required) The value which will trigger a violation. Must be `0` or greater.
        - `threshold_duration` - (Optional) The duration of time, in seconds, that the threshold must violate for in order to create a violation. Value must be a multiple of 60.
        <br>For _baseline_ NRQL alert conditions, the value must be within 120-3600 seconds (inclusive).
        <br>For _static_ NRQL alert conditions, the value must be within 120-7200 seconds (inclusive).

        - `threshold_occurrences` - (Optional) The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: `all` or `at_least_once` (case insensitive).
        - `duration` - (Optional) **DEPRECATED:** Use `threshold_duration` instead. The duration of time, in _minutes_, that the threshold must violate for in order to create a violation. Must be within 1-120 (inclusive).
        - `time_function` - (Optional) **DEPRECATED:** Use `threshold_occurrences` instead. The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: `all` or `any`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
        :param pulumi.Input[int] aggregation_window: The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.
        :param pulumi.Input[str] baseline_direction: The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
        :param pulumi.Input[bool] close_violations_on_expiration: Whether to close all open violations when the signal expires.
        :param pulumi.Input[pulumi.InputType['NrqlAlertConditionCriticalArgs']] critical: A list containing the `critical` threshold values. See Terms below for details.
        :param pulumi.Input[str] description: The description of the NRQL alert condition.
        :param pulumi.Input[bool] enabled: Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[int] expected_groups: Number of expected groups when using `outlier` detection.
        :param pulumi.Input[int] expiration_duration: The amount of time (in seconds) to wait before considering the signal expired.
        :param pulumi.Input[str] fill_option: Which strategy to use when filling gaps in the signal. Possible values are `none`, `last_value` or `static`. If `static`, the `fill_value` field will be used for filling gaps in the signal.
        :param pulumi.Input[float] fill_value: This value will be used for filling gaps in the signal.
        :param pulumi.Input[bool] ignore_overlap: **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[str] name: The title of the condition.
        :param pulumi.Input[pulumi.InputType['NrqlAlertConditionNrqlArgs']] nrql: A NRQL query. See NRQL below for details.
        :param pulumi.Input[bool] open_violation_on_expiration: Whether to create a new violation to capture that the signal expired.
        :param pulumi.Input[bool] open_violation_on_group_overlap: Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[int] policy_id: The ID of the policy where this condition should be used.
        :param pulumi.Input[str] runbook_url: Runbook URL to display in notifications.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NrqlAlertConditionTermArgs']]]] terms: **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
        :param pulumi.Input[str] type: The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
        :param pulumi.Input[str] value_function: Possible values are `single_value`, `sum` (case insensitive).
        :param pulumi.Input[str] violation_time_limit: Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
               <small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>
        :param pulumi.Input[int] violation_time_limit_seconds: **DEPRECATED:** Use `violation_time_limit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.<br>
               <small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>
        :param pulumi.Input[pulumi.InputType['NrqlAlertConditionWarningArgs']] warning: A list containing the `warning` threshold values. See Terms below for details.
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
            __props__['aggregation_window'] = aggregation_window
            __props__['baseline_direction'] = baseline_direction
            __props__['close_violations_on_expiration'] = close_violations_on_expiration
            __props__['critical'] = critical
            __props__['description'] = description
            __props__['enabled'] = enabled
            __props__['expected_groups'] = expected_groups
            __props__['expiration_duration'] = expiration_duration
            __props__['fill_option'] = fill_option
            __props__['fill_value'] = fill_value
            if ignore_overlap is not None:
                warnings.warn("use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true", DeprecationWarning)
                pulumi.log.warn("ignore_overlap is deprecated: use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true")
            __props__['ignore_overlap'] = ignore_overlap
            __props__['name'] = name
            if nrql is None:
                raise TypeError("Missing required property 'nrql'")
            __props__['nrql'] = nrql
            __props__['open_violation_on_expiration'] = open_violation_on_expiration
            __props__['open_violation_on_group_overlap'] = open_violation_on_group_overlap
            if policy_id is None:
                raise TypeError("Missing required property 'policy_id'")
            __props__['policy_id'] = policy_id
            __props__['runbook_url'] = runbook_url
            if terms is not None:
                warnings.warn("use `critical` and `warning` attributes instead", DeprecationWarning)
                pulumi.log.warn("terms is deprecated: use `critical` and `warning` attributes instead")
            __props__['terms'] = terms
            __props__['type'] = type
            __props__['value_function'] = value_function
            __props__['violation_time_limit'] = violation_time_limit
            if violation_time_limit_seconds is not None:
                warnings.warn("use `violation_time_limit` attribute instead", DeprecationWarning)
                pulumi.log.warn("violation_time_limit_seconds is deprecated: use `violation_time_limit` attribute instead")
            __props__['violation_time_limit_seconds'] = violation_time_limit_seconds
            __props__['warning'] = warning
        super(NrqlAlertCondition, __self__).__init__(
            'newrelic:index/nrqlAlertCondition:NrqlAlertCondition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[int]] = None,
            aggregation_window: Optional[pulumi.Input[int]] = None,
            baseline_direction: Optional[pulumi.Input[str]] = None,
            close_violations_on_expiration: Optional[pulumi.Input[bool]] = None,
            critical: Optional[pulumi.Input[pulumi.InputType['NrqlAlertConditionCriticalArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            expected_groups: Optional[pulumi.Input[int]] = None,
            expiration_duration: Optional[pulumi.Input[int]] = None,
            fill_option: Optional[pulumi.Input[str]] = None,
            fill_value: Optional[pulumi.Input[float]] = None,
            ignore_overlap: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nrql: Optional[pulumi.Input[pulumi.InputType['NrqlAlertConditionNrqlArgs']]] = None,
            open_violation_on_expiration: Optional[pulumi.Input[bool]] = None,
            open_violation_on_group_overlap: Optional[pulumi.Input[bool]] = None,
            policy_id: Optional[pulumi.Input[int]] = None,
            runbook_url: Optional[pulumi.Input[str]] = None,
            terms: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NrqlAlertConditionTermArgs']]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value_function: Optional[pulumi.Input[str]] = None,
            violation_time_limit: Optional[pulumi.Input[str]] = None,
            violation_time_limit_seconds: Optional[pulumi.Input[int]] = None,
            warning: Optional[pulumi.Input[pulumi.InputType['NrqlAlertConditionWarningArgs']]] = None) -> 'NrqlAlertCondition':
        """
        Get an existing NrqlAlertCondition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] account_id: The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
        :param pulumi.Input[int] aggregation_window: The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.
        :param pulumi.Input[str] baseline_direction: The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
        :param pulumi.Input[bool] close_violations_on_expiration: Whether to close all open violations when the signal expires.
        :param pulumi.Input[pulumi.InputType['NrqlAlertConditionCriticalArgs']] critical: A list containing the `critical` threshold values. See Terms below for details.
        :param pulumi.Input[str] description: The description of the NRQL alert condition.
        :param pulumi.Input[bool] enabled: Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[int] expected_groups: Number of expected groups when using `outlier` detection.
        :param pulumi.Input[int] expiration_duration: The amount of time (in seconds) to wait before considering the signal expired.
        :param pulumi.Input[str] fill_option: Which strategy to use when filling gaps in the signal. Possible values are `none`, `last_value` or `static`. If `static`, the `fill_value` field will be used for filling gaps in the signal.
        :param pulumi.Input[float] fill_value: This value will be used for filling gaps in the signal.
        :param pulumi.Input[bool] ignore_overlap: **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[str] name: The title of the condition.
        :param pulumi.Input[pulumi.InputType['NrqlAlertConditionNrqlArgs']] nrql: A NRQL query. See NRQL below for details.
        :param pulumi.Input[bool] open_violation_on_expiration: Whether to create a new violation to capture that the signal expired.
        :param pulumi.Input[bool] open_violation_on_group_overlap: Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[int] policy_id: The ID of the policy where this condition should be used.
        :param pulumi.Input[str] runbook_url: Runbook URL to display in notifications.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NrqlAlertConditionTermArgs']]]] terms: **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
        :param pulumi.Input[str] type: The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
        :param pulumi.Input[str] value_function: Possible values are `single_value`, `sum` (case insensitive).
        :param pulumi.Input[str] violation_time_limit: Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
               <small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>
        :param pulumi.Input[int] violation_time_limit_seconds: **DEPRECATED:** Use `violation_time_limit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.<br>
               <small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>
        :param pulumi.Input[pulumi.InputType['NrqlAlertConditionWarningArgs']] warning: A list containing the `warning` threshold values. See Terms below for details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["aggregation_window"] = aggregation_window
        __props__["baseline_direction"] = baseline_direction
        __props__["close_violations_on_expiration"] = close_violations_on_expiration
        __props__["critical"] = critical
        __props__["description"] = description
        __props__["enabled"] = enabled
        __props__["expected_groups"] = expected_groups
        __props__["expiration_duration"] = expiration_duration
        __props__["fill_option"] = fill_option
        __props__["fill_value"] = fill_value
        __props__["ignore_overlap"] = ignore_overlap
        __props__["name"] = name
        __props__["nrql"] = nrql
        __props__["open_violation_on_expiration"] = open_violation_on_expiration
        __props__["open_violation_on_group_overlap"] = open_violation_on_group_overlap
        __props__["policy_id"] = policy_id
        __props__["runbook_url"] = runbook_url
        __props__["terms"] = terms
        __props__["type"] = type
        __props__["value_function"] = value_function
        __props__["violation_time_limit"] = violation_time_limit
        __props__["violation_time_limit_seconds"] = violation_time_limit_seconds
        __props__["warning"] = warning
        return NrqlAlertCondition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[int]:
        """
        The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="aggregationWindow")
    def aggregation_window(self) -> pulumi.Output[Optional[int]]:
        """
        The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.
        """
        return pulumi.get(self, "aggregation_window")

    @property
    @pulumi.getter(name="baselineDirection")
    def baseline_direction(self) -> pulumi.Output[Optional[str]]:
        """
        The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
        """
        return pulumi.get(self, "baseline_direction")

    @property
    @pulumi.getter(name="closeViolationsOnExpiration")
    def close_violations_on_expiration(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to close all open violations when the signal expires.
        """
        return pulumi.get(self, "close_violations_on_expiration")

    @property
    @pulumi.getter
    def critical(self) -> pulumi.Output[Optional['outputs.NrqlAlertConditionCritical']]:
        """
        A list containing the `critical` threshold values. See Terms below for details.
        """
        return pulumi.get(self, "critical")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the NRQL alert condition.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="expectedGroups")
    def expected_groups(self) -> pulumi.Output[Optional[int]]:
        """
        Number of expected groups when using `outlier` detection.
        """
        return pulumi.get(self, "expected_groups")

    @property
    @pulumi.getter(name="expirationDuration")
    def expiration_duration(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of time (in seconds) to wait before considering the signal expired.
        """
        return pulumi.get(self, "expiration_duration")

    @property
    @pulumi.getter(name="fillOption")
    def fill_option(self) -> pulumi.Output[Optional[str]]:
        """
        Which strategy to use when filling gaps in the signal. Possible values are `none`, `last_value` or `static`. If `static`, the `fill_value` field will be used for filling gaps in the signal.
        """
        return pulumi.get(self, "fill_option")

    @property
    @pulumi.getter(name="fillValue")
    def fill_value(self) -> pulumi.Output[Optional[float]]:
        """
        This value will be used for filling gaps in the signal.
        """
        return pulumi.get(self, "fill_value")

    @property
    @pulumi.getter(name="ignoreOverlap")
    def ignore_overlap(self) -> pulumi.Output[Optional[bool]]:
        """
        **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
        """
        return pulumi.get(self, "ignore_overlap")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The title of the condition.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nrql(self) -> pulumi.Output['outputs.NrqlAlertConditionNrql']:
        """
        A NRQL query. See NRQL below for details.
        """
        return pulumi.get(self, "nrql")

    @property
    @pulumi.getter(name="openViolationOnExpiration")
    def open_violation_on_expiration(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to create a new violation to capture that the signal expired.
        """
        return pulumi.get(self, "open_violation_on_expiration")

    @property
    @pulumi.getter(name="openViolationOnGroupOverlap")
    def open_violation_on_group_overlap(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
        """
        return pulumi.get(self, "open_violation_on_group_overlap")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[int]:
        """
        The ID of the policy where this condition should be used.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="runbookUrl")
    def runbook_url(self) -> pulumi.Output[Optional[str]]:
        """
        Runbook URL to display in notifications.
        """
        return pulumi.get(self, "runbook_url")

    @property
    @pulumi.getter
    def terms(self) -> pulumi.Output[Optional[Sequence['outputs.NrqlAlertConditionTerm']]]:
        """
        **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
        """
        return pulumi.get(self, "terms")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="valueFunction")
    def value_function(self) -> pulumi.Output[Optional[str]]:
        """
        Possible values are `single_value`, `sum` (case insensitive).
        """
        return pulumi.get(self, "value_function")

    @property
    @pulumi.getter(name="violationTimeLimit")
    def violation_time_limit(self) -> pulumi.Output[Optional[str]]:
        """
        Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
        <small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>
        """
        return pulumi.get(self, "violation_time_limit")

    @property
    @pulumi.getter(name="violationTimeLimitSeconds")
    def violation_time_limit_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        **DEPRECATED:** Use `violation_time_limit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.<br>
        <small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>
        """
        return pulumi.get(self, "violation_time_limit_seconds")

    @property
    @pulumi.getter
    def warning(self) -> pulumi.Output[Optional['outputs.NrqlAlertConditionWarning']]:
        """
        A list containing the `warning` threshold values. See Terms below for details.
        """
        return pulumi.get(self, "warning")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

