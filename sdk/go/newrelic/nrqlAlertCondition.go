// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package newrelic

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this resource to create and manage NRQL alert conditions in New Relic.
//
// ## NRQL
//
// The `nrql` block supports the following arguments:
//
// - `query` - (Required) The NRQL query to execute for the condition.
// - `evaluationOffset` - (Optional) Represented in minutes and must be within 1-20 minutes (inclusive). NRQL queries are evaluated in one-minute time windows. The start time depends on this value. It's recommended to set this to 3 minutes. An offset of less than 3 minutes will trigger violations sooner, but you may see more false positives and negatives due to data latency. With `evaluationOffset` set to 3 minutes, the NRQL time window applied to your query will be: `SINCE 3 minutes ago UNTIL 2 minutes ago`.
// - `sinceValue` - (Optional)  **DEPRECATED:** Use `evaluationOffset` instead. The value to be used in the `SINCE <X> minutes ago` clause for the NRQL query. Must be between 1-20 (inclusive).
//
// ## Terms
//
// > **NOTE:** The direct use of the `term` has been deprecated, and users should use `critical` and `warning` instead.  What follows now applies to the named priority attributes for `critical` and `warning`, but for those attributes the priority is not allowed.
//
// NRQL alert conditions support up to two terms. At least one `term` must have `priority` set to `critical` and the second optional `term` must have `priority` set to `warning`.
//
// The `term` block the following arguments:
//
// - `operator` - (Optional) Valid values are `above`, `below`, or `equals` (case insensitive). Defaults to `equals`. Note that when using a `type` of `outlier`, the only valid option here is `above`.
// - `priority` - (Optional) `critical` or `warning`. Defaults to `critical`.
// - `threshold` - (Required) The value which will trigger a violation. Must be `0` or greater.
// - `thresholdDuration` - (Optional) The duration of time, in seconds, that the threshold must violate for in order to create a violation. Value must be a multiple of 60.
// <br>For _baseline_ NRQL alert conditions, the value must be within 120-3600 seconds (inclusive).
// <br>For _static_ NRQL alert conditions, the value must be within 120-7200 seconds (inclusive).
//
// - `thresholdOccurrences` - (Optional) The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: `all` or `atLeastOnce` (case insensitive).
// - `duration` - (Optional) **DEPRECATED:** Use `thresholdDuration` instead. The duration of time, in _minutes_, that the threshold must violate for in order to create a violation. Must be within 1-120 (inclusive).
// - `timeFunction` - (Optional) **DEPRECATED:** Use `thresholdOccurrences` instead. The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: `all` or `any`.
type NrqlAlertCondition struct {
	pulumi.CustomResourceState

	// The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
	AccountId pulumi.IntPtrOutput `pulumi:"accountId"`
	// The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lowerOnly`, `upperAndLower`, `upperOnly` (case insensitive).
	BaselineDirection pulumi.StringPtrOutput `pulumi:"baselineDirection"`
	// A list containing the `critical` threshold values. See Terms below for details.
	Critical NrqlAlertConditionCriticalPtrOutput `pulumi:"critical"`
	// The description of the NRQL alert condition.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// Number of expected groups when using `outlier` detection.
	ExpectedGroups pulumi.IntPtrOutput `pulumi:"expectedGroups"`
	// **DEPRECATED:** Use `openViolationOnGroupOverlap` instead, but use the inverse value of your boolean - e.g. if `ignoreOverlap = false`, use `openViolationOnGroupOverlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
	//
	// Deprecated: use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true
	IgnoreOverlap pulumi.BoolPtrOutput `pulumi:"ignoreOverlap"`
	// The title of the condition.
	Name pulumi.StringOutput `pulumi:"name"`
	// A NRQL query. See NRQL below for details.
	Nrql NrqlAlertConditionNrqlOutput `pulumi:"nrql"`
	// Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
	OpenViolationOnGroupOverlap pulumi.BoolPtrOutput `pulumi:"openViolationOnGroupOverlap"`
	// The ID of the policy where this condition should be used.
	PolicyId pulumi.IntOutput `pulumi:"policyId"`
	// Runbook URL to display in notifications.
	RunbookUrl pulumi.StringPtrOutput `pulumi:"runbookUrl"`
	// **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
	//
	// Deprecated: use `critical` and `warning` attributes instead
	Terms NrqlAlertConditionTermArrayOutput `pulumi:"terms"`
	// The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
	Type pulumi.StringPtrOutput `pulumi:"type"`
	// Possible values are `singleValue`, `sum` (case insensitive). Defaults to `singleValue`.
	ValueFunction pulumi.StringPtrOutput `pulumi:"valueFunction"`
	// Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
	ViolationTimeLimit pulumi.StringPtrOutput `pulumi:"violationTimeLimit"`
	// **DEPRECATED:** Use `violationTimeLimit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
	//
	// Deprecated: use `violation_time_limit` attribute instead
	ViolationTimeLimitSeconds pulumi.IntPtrOutput `pulumi:"violationTimeLimitSeconds"`
	// A list containing the `warning` threshold values. See Terms below for details.
	Warning NrqlAlertConditionWarningPtrOutput `pulumi:"warning"`
}

// NewNrqlAlertCondition registers a new resource with the given unique name, arguments, and options.
func NewNrqlAlertCondition(ctx *pulumi.Context,
	name string, args *NrqlAlertConditionArgs, opts ...pulumi.ResourceOption) (*NrqlAlertCondition, error) {
	if args == nil || args.Nrql == nil {
		return nil, errors.New("missing required argument 'Nrql'")
	}
	if args == nil || args.PolicyId == nil {
		return nil, errors.New("missing required argument 'PolicyId'")
	}
	if args == nil {
		args = &NrqlAlertConditionArgs{}
	}
	var resource NrqlAlertCondition
	err := ctx.RegisterResource("newrelic:index/nrqlAlertCondition:NrqlAlertCondition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNrqlAlertCondition gets an existing NrqlAlertCondition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNrqlAlertCondition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NrqlAlertConditionState, opts ...pulumi.ResourceOption) (*NrqlAlertCondition, error) {
	var resource NrqlAlertCondition
	err := ctx.ReadResource("newrelic:index/nrqlAlertCondition:NrqlAlertCondition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NrqlAlertCondition resources.
type nrqlAlertConditionState struct {
	// The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
	AccountId *int `pulumi:"accountId"`
	// The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lowerOnly`, `upperAndLower`, `upperOnly` (case insensitive).
	BaselineDirection *string `pulumi:"baselineDirection"`
	// A list containing the `critical` threshold values. See Terms below for details.
	Critical *NrqlAlertConditionCritical `pulumi:"critical"`
	// The description of the NRQL alert condition.
	Description *string `pulumi:"description"`
	// Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// Number of expected groups when using `outlier` detection.
	ExpectedGroups *int `pulumi:"expectedGroups"`
	// **DEPRECATED:** Use `openViolationOnGroupOverlap` instead, but use the inverse value of your boolean - e.g. if `ignoreOverlap = false`, use `openViolationOnGroupOverlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
	//
	// Deprecated: use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true
	IgnoreOverlap *bool `pulumi:"ignoreOverlap"`
	// The title of the condition.
	Name *string `pulumi:"name"`
	// A NRQL query. See NRQL below for details.
	Nrql *NrqlAlertConditionNrql `pulumi:"nrql"`
	// Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
	OpenViolationOnGroupOverlap *bool `pulumi:"openViolationOnGroupOverlap"`
	// The ID of the policy where this condition should be used.
	PolicyId *int `pulumi:"policyId"`
	// Runbook URL to display in notifications.
	RunbookUrl *string `pulumi:"runbookUrl"`
	// **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
	//
	// Deprecated: use `critical` and `warning` attributes instead
	Terms []NrqlAlertConditionTerm `pulumi:"terms"`
	// The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
	Type *string `pulumi:"type"`
	// Possible values are `singleValue`, `sum` (case insensitive). Defaults to `singleValue`.
	ValueFunction *string `pulumi:"valueFunction"`
	// Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
	ViolationTimeLimit *string `pulumi:"violationTimeLimit"`
	// **DEPRECATED:** Use `violationTimeLimit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
	//
	// Deprecated: use `violation_time_limit` attribute instead
	ViolationTimeLimitSeconds *int `pulumi:"violationTimeLimitSeconds"`
	// A list containing the `warning` threshold values. See Terms below for details.
	Warning *NrqlAlertConditionWarning `pulumi:"warning"`
}

type NrqlAlertConditionState struct {
	// The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
	AccountId pulumi.IntPtrInput
	// The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lowerOnly`, `upperAndLower`, `upperOnly` (case insensitive).
	BaselineDirection pulumi.StringPtrInput
	// A list containing the `critical` threshold values. See Terms below for details.
	Critical NrqlAlertConditionCriticalPtrInput
	// The description of the NRQL alert condition.
	Description pulumi.StringPtrInput
	// Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// Number of expected groups when using `outlier` detection.
	ExpectedGroups pulumi.IntPtrInput
	// **DEPRECATED:** Use `openViolationOnGroupOverlap` instead, but use the inverse value of your boolean - e.g. if `ignoreOverlap = false`, use `openViolationOnGroupOverlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
	//
	// Deprecated: use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true
	IgnoreOverlap pulumi.BoolPtrInput
	// The title of the condition.
	Name pulumi.StringPtrInput
	// A NRQL query. See NRQL below for details.
	Nrql NrqlAlertConditionNrqlPtrInput
	// Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
	OpenViolationOnGroupOverlap pulumi.BoolPtrInput
	// The ID of the policy where this condition should be used.
	PolicyId pulumi.IntPtrInput
	// Runbook URL to display in notifications.
	RunbookUrl pulumi.StringPtrInput
	// **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
	//
	// Deprecated: use `critical` and `warning` attributes instead
	Terms NrqlAlertConditionTermArrayInput
	// The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
	Type pulumi.StringPtrInput
	// Possible values are `singleValue`, `sum` (case insensitive). Defaults to `singleValue`.
	ValueFunction pulumi.StringPtrInput
	// Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
	ViolationTimeLimit pulumi.StringPtrInput
	// **DEPRECATED:** Use `violationTimeLimit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
	//
	// Deprecated: use `violation_time_limit` attribute instead
	ViolationTimeLimitSeconds pulumi.IntPtrInput
	// A list containing the `warning` threshold values. See Terms below for details.
	Warning NrqlAlertConditionWarningPtrInput
}

func (NrqlAlertConditionState) ElementType() reflect.Type {
	return reflect.TypeOf((*nrqlAlertConditionState)(nil)).Elem()
}

type nrqlAlertConditionArgs struct {
	// The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
	AccountId *int `pulumi:"accountId"`
	// The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lowerOnly`, `upperAndLower`, `upperOnly` (case insensitive).
	BaselineDirection *string `pulumi:"baselineDirection"`
	// A list containing the `critical` threshold values. See Terms below for details.
	Critical *NrqlAlertConditionCritical `pulumi:"critical"`
	// The description of the NRQL alert condition.
	Description *string `pulumi:"description"`
	// Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// Number of expected groups when using `outlier` detection.
	ExpectedGroups *int `pulumi:"expectedGroups"`
	// **DEPRECATED:** Use `openViolationOnGroupOverlap` instead, but use the inverse value of your boolean - e.g. if `ignoreOverlap = false`, use `openViolationOnGroupOverlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
	//
	// Deprecated: use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true
	IgnoreOverlap *bool `pulumi:"ignoreOverlap"`
	// The title of the condition.
	Name *string `pulumi:"name"`
	// A NRQL query. See NRQL below for details.
	Nrql NrqlAlertConditionNrql `pulumi:"nrql"`
	// Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
	OpenViolationOnGroupOverlap *bool `pulumi:"openViolationOnGroupOverlap"`
	// The ID of the policy where this condition should be used.
	PolicyId int `pulumi:"policyId"`
	// Runbook URL to display in notifications.
	RunbookUrl *string `pulumi:"runbookUrl"`
	// **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
	//
	// Deprecated: use `critical` and `warning` attributes instead
	Terms []NrqlAlertConditionTerm `pulumi:"terms"`
	// The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
	Type *string `pulumi:"type"`
	// Possible values are `singleValue`, `sum` (case insensitive). Defaults to `singleValue`.
	ValueFunction *string `pulumi:"valueFunction"`
	// Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
	ViolationTimeLimit *string `pulumi:"violationTimeLimit"`
	// **DEPRECATED:** Use `violationTimeLimit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
	//
	// Deprecated: use `violation_time_limit` attribute instead
	ViolationTimeLimitSeconds *int `pulumi:"violationTimeLimitSeconds"`
	// A list containing the `warning` threshold values. See Terms below for details.
	Warning *NrqlAlertConditionWarning `pulumi:"warning"`
}

// The set of arguments for constructing a NrqlAlertCondition resource.
type NrqlAlertConditionArgs struct {
	// The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
	AccountId pulumi.IntPtrInput
	// The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lowerOnly`, `upperAndLower`, `upperOnly` (case insensitive).
	BaselineDirection pulumi.StringPtrInput
	// A list containing the `critical` threshold values. See Terms below for details.
	Critical NrqlAlertConditionCriticalPtrInput
	// The description of the NRQL alert condition.
	Description pulumi.StringPtrInput
	// Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// Number of expected groups when using `outlier` detection.
	ExpectedGroups pulumi.IntPtrInput
	// **DEPRECATED:** Use `openViolationOnGroupOverlap` instead, but use the inverse value of your boolean - e.g. if `ignoreOverlap = false`, use `openViolationOnGroupOverlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
	//
	// Deprecated: use `open_violation_on_group_overlap` attribute instead, but use the inverse of your boolean - e.g. if ignore_overlap = false, use open_violation_on_group_overlap = true
	IgnoreOverlap pulumi.BoolPtrInput
	// The title of the condition.
	Name pulumi.StringPtrInput
	// A NRQL query. See NRQL below for details.
	Nrql NrqlAlertConditionNrqlInput
	// Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
	OpenViolationOnGroupOverlap pulumi.BoolPtrInput
	// The ID of the policy where this condition should be used.
	PolicyId pulumi.IntInput
	// Runbook URL to display in notifications.
	RunbookUrl pulumi.StringPtrInput
	// **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See Terms below for details.
	//
	// Deprecated: use `critical` and `warning` attributes instead
	Terms NrqlAlertConditionTermArrayInput
	// The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
	Type pulumi.StringPtrInput
	// Possible values are `singleValue`, `sum` (case insensitive). Defaults to `singleValue`.
	ValueFunction pulumi.StringPtrInput
	// Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS` (case insensitive).
	ViolationTimeLimit pulumi.StringPtrInput
	// **DEPRECATED:** Use `violationTimeLimit` instead. Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `3600`, `7200`, `14400`, `28800`, `43200`, and `86400`.
	//
	// Deprecated: use `violation_time_limit` attribute instead
	ViolationTimeLimitSeconds pulumi.IntPtrInput
	// A list containing the `warning` threshold values. See Terms below for details.
	Warning NrqlAlertConditionWarningPtrInput
}

func (NrqlAlertConditionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*nrqlAlertConditionArgs)(nil)).Elem()
}
