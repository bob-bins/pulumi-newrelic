# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import _utilities, _tables


class NrqlAlertCondition(pulumi.CustomResource):
    account_id: pulumi.Output[float]
    """
    The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
    """
    baseline_direction: pulumi.Output[str]
    """
    The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
    """
    critical: pulumi.Output[dict]
    """
    A list containing the `critical` threshold values. See Terms below for details.

      * `duration` (`float`)
      * `operator` (`str`)
      * `threshold` (`float`)
      * `thresholdDuration` (`float`)
      * `thresholdOccurrences` (`str`)
      * `timeFunction` (`str`)
    """
    description: pulumi.Output[str]
    """
    The description of the NRQL alert condition.
    """
    enabled: pulumi.Output[bool]
    """
    Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
    """
    expected_groups: pulumi.Output[float]
    """
    Number of expected groups when using `outlier` detection.
    """
    ignore_overlap: pulumi.Output[bool]
    """
    **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
    """
    name: pulumi.Output[str]
    """
    The title of the condition.
    """
    nrql: pulumi.Output[dict]
    """
    A NRQL query. See NRQL below for details.

      * `evaluationOffset` (`float`)
      * `query` (`str`)
      * `sinceValue` (`str`)
    """
    open_violation_on_group_overlap: pulumi.Output[bool]
    """
    Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
    """
    policy_id: pulumi.Output[float]
    """
    The ID of the policy where this condition should be used.
    """
    runbook_url: pulumi.Output[str]
    """
    Runbook URL to display in notifications.
    """
    terms: pulumi.Output[list]
    """
    **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.

      * `duration` (`float`)
      * `operator` (`str`)
      * `priority` (`str`)
      * `threshold` (`float`)
      * `thresholdDuration` (`float`)
      * `thresholdOccurrences` (`str`)
      * `timeFunction` (`str`)
    """
    type: pulumi.Output[str]
    """
    The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
    """
    value_function: pulumi.Output[str]
    """
    Possible values are `single_value`, `sum` (case insensitive). Defaults to `single_value`.
    """
    violation_time_limit: pulumi.Output[str]
    """
    Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
    """
    violation_time_limit_seconds: pulumi.Output[float]
    """
    **DEPRECATED:** Use `violation_time_limit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
    """
    warning: pulumi.Output[dict]
    """
    A list containing the `warning` threshold values. See Terms below for details.

      * `duration` (`float`)
      * `operator` (`str`)
      * `threshold` (`float`)
      * `thresholdDuration` (`float`)
      * `thresholdOccurrences` (`str`)
      * `timeFunction` (`str`)
    """
    def __init__(__self__, resource_name, opts=None, account_id=None, baseline_direction=None, critical=None, description=None, enabled=None, expected_groups=None, ignore_overlap=None, name=None, nrql=None, open_violation_on_group_overlap=None, policy_id=None, runbook_url=None, terms=None, type=None, value_function=None, violation_time_limit=None, violation_time_limit_seconds=None, warning=None, __props__=None, __name__=None, __opts__=None):
        """
        Use this resource to create and manage NRQL alert conditions in New Relic.

        ## NRQL

        The `nrql` block supports the following arguments:

        - `query` - (Required) The NRQL query to execute for the condition.
        - `evaluation_offset` - (Optional) Represented in minutes and must be within 1-20 minutes (inclusive). NRQL queries are evaluated in one-minute time windows. The start time depends on this value. It's recommended to set this to 3 minutes. An offset of less than 3 minutes will trigger violations sooner, but you may see more false positives and negatives due to data latency. With `evaluation_offset` set to 3 minutes, the NRQL time window applied to your query will be: `SINCE 3 minutes ago UNTIL 2 minutes ago`.
        - `since_value` - (Optional)  **DEPRECATED:** Use `evaluation_offset` instead. The value to be used in the `SINCE <X> minutes ago` clause for the NRQL query. Must be between 1-20 (inclusive).

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
        :param pulumi.Input[float] account_id: The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
        :param pulumi.Input[str] baseline_direction: The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
        :param pulumi.Input[dict] critical: A list containing the `critical` threshold values. See Terms below for details.
        :param pulumi.Input[str] description: The description of the NRQL alert condition.
        :param pulumi.Input[bool] enabled: Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[float] expected_groups: Number of expected groups when using `outlier` detection.
        :param pulumi.Input[bool] ignore_overlap: **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[str] name: The title of the condition.
        :param pulumi.Input[dict] nrql: A NRQL query. See NRQL below for details.
        :param pulumi.Input[bool] open_violation_on_group_overlap: Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[float] policy_id: The ID of the policy where this condition should be used.
        :param pulumi.Input[str] runbook_url: Runbook URL to display in notifications.
        :param pulumi.Input[list] terms: **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
        :param pulumi.Input[str] type: The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
        :param pulumi.Input[str] value_function: Possible values are `single_value`, `sum` (case insensitive). Defaults to `single_value`.
        :param pulumi.Input[str] violation_time_limit: Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
        :param pulumi.Input[float] violation_time_limit_seconds: **DEPRECATED:** Use `violation_time_limit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
        :param pulumi.Input[dict] warning: A list containing the `warning` threshold values. See Terms below for details.

        The **critical** object supports the following:

          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `thresholdDuration` (`pulumi.Input[float]`)
          * `thresholdOccurrences` (`pulumi.Input[str]`)
          * `timeFunction` (`pulumi.Input[str]`)

        The **nrql** object supports the following:

          * `evaluationOffset` (`pulumi.Input[float]`)
          * `query` (`pulumi.Input[str]`)
          * `sinceValue` (`pulumi.Input[str]`)

        The **terms** object supports the following:

          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `priority` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `thresholdDuration` (`pulumi.Input[float]`)
          * `thresholdOccurrences` (`pulumi.Input[str]`)
          * `timeFunction` (`pulumi.Input[str]`)

        The **warning** object supports the following:

          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `thresholdDuration` (`pulumi.Input[float]`)
          * `thresholdOccurrences` (`pulumi.Input[str]`)
          * `timeFunction` (`pulumi.Input[str]`)
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
            __props__['baseline_direction'] = baseline_direction
            __props__['critical'] = critical
            __props__['description'] = description
            __props__['enabled'] = enabled
            __props__['expected_groups'] = expected_groups
            if ignore_overlap is not None:
                warnings.warn("use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true", DeprecationWarning)
                pulumi.log.warn("ignore_overlap is deprecated: use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true")
            __props__['ignore_overlap'] = ignore_overlap
            __props__['name'] = name
            if nrql is None:
                raise TypeError("Missing required property 'nrql'")
            __props__['nrql'] = nrql
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
    def get(resource_name, id, opts=None, account_id=None, baseline_direction=None, critical=None, description=None, enabled=None, expected_groups=None, ignore_overlap=None, name=None, nrql=None, open_violation_on_group_overlap=None, policy_id=None, runbook_url=None, terms=None, type=None, value_function=None, violation_time_limit=None, violation_time_limit_seconds=None, warning=None):
        """
        Get an existing NrqlAlertCondition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] account_id: The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
        :param pulumi.Input[str] baseline_direction: The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
        :param pulumi.Input[dict] critical: A list containing the `critical` threshold values. See Terms below for details.
        :param pulumi.Input[str] description: The description of the NRQL alert condition.
        :param pulumi.Input[bool] enabled: Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
        :param pulumi.Input[float] expected_groups: Number of expected groups when using `outlier` detection.
        :param pulumi.Input[bool] ignore_overlap: **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[str] name: The title of the condition.
        :param pulumi.Input[dict] nrql: A NRQL query. See NRQL below for details.
        :param pulumi.Input[bool] open_violation_on_group_overlap: Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
        :param pulumi.Input[float] policy_id: The ID of the policy where this condition should be used.
        :param pulumi.Input[str] runbook_url: Runbook URL to display in notifications.
        :param pulumi.Input[list] terms: **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
        :param pulumi.Input[str] type: The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
        :param pulumi.Input[str] value_function: Possible values are `single_value`, `sum` (case insensitive). Defaults to `single_value`.
        :param pulumi.Input[str] violation_time_limit: Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
        :param pulumi.Input[float] violation_time_limit_seconds: **DEPRECATED:** Use `violation_time_limit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
        :param pulumi.Input[dict] warning: A list containing the `warning` threshold values. See Terms below for details.

        The **critical** object supports the following:

          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `thresholdDuration` (`pulumi.Input[float]`)
          * `thresholdOccurrences` (`pulumi.Input[str]`)
          * `timeFunction` (`pulumi.Input[str]`)

        The **nrql** object supports the following:

          * `evaluationOffset` (`pulumi.Input[float]`)
          * `query` (`pulumi.Input[str]`)
          * `sinceValue` (`pulumi.Input[str]`)

        The **terms** object supports the following:

          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `priority` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `thresholdDuration` (`pulumi.Input[float]`)
          * `thresholdOccurrences` (`pulumi.Input[str]`)
          * `timeFunction` (`pulumi.Input[str]`)

        The **warning** object supports the following:

          * `duration` (`pulumi.Input[float]`)
          * `operator` (`pulumi.Input[str]`)
          * `threshold` (`pulumi.Input[float]`)
          * `thresholdDuration` (`pulumi.Input[float]`)
          * `thresholdOccurrences` (`pulumi.Input[str]`)
          * `timeFunction` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["baseline_direction"] = baseline_direction
        __props__["critical"] = critical
        __props__["description"] = description
        __props__["enabled"] = enabled
        __props__["expected_groups"] = expected_groups
        __props__["ignore_overlap"] = ignore_overlap
        __props__["name"] = name
        __props__["nrql"] = nrql
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

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
